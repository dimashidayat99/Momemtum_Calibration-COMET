import sys
import os
import subprocess

cwd = os.getcwd()
setupEnvPath = "/home/user/mdimas/comet/SetupEnv.sh"
#
# Specify macro name
#
macroName = "Analyzer.C"

txtFileDir  = './TempSampleLists/'

JOBS=[]
JOBS += [("piMinusGun_default_part"+str(i),"piMinusGunRooTrackHist_SimG4_default_part"+str(i)) for i in xrange(0,20)]
JOBS += [("piMinusGun_polyethylene_part"+str(i),"piMinusGunRooTrackHist_SimG4_polyethylene_part"+str(i)) for i in xrange(0,20)]

print("Here are the jobs to be sent")
for j in JOBS:
  print(j)

print("\n\n")
#
# Make the bash script
#
for iJob,Job in enumerate(JOBS):
  jobName = Job[0]
  txtFileName = Job[1]
  #
  #
  #
  outDir="./histos_{:s}/".format(jobName)
  #
  #
  #
  CPUTIME="00:20:00"
  #
  #
  #
  fName = 'Batch_{:s}.sh'.format(jobName)
  f = open(fName, 'w')
  f.write('#!/usr/bin/env bash\n')  
  f.write('#PBS -l h_rt={:s}\n'.format(CPUTIME))
  f.write('#PBS -l s_rss=1G\n')
  f.write('#PBS -l -P P_comet\n')
  f.write('#PBS -l sps=1\n')
  f.write('\n')
  f.write('cd {:s} \n'.format(cwd))
  f.write('source {:s} \n'.format(setupEnvPath))
  command = 'python -u RunLocal.py -m {:s} -d {:s} -t {:s} -o {:s}'.format(macroName,txtFileDir,txtFileName,outDir)
  f.write(command + ' \n')
  f.close()
  #
  preliminary_command = 'chmod +x {:s}'.format(fName)
  os.system(preliminary_command)
  #
  print 'Sending Job Name: {:s}'.format(fName)
  sendBatchScript_command = 'qsub -r n -o {:s}/BatchLog/ -e {:s}/BatchLog/ {:s}'.format(cwd,cwd,fName)
  os.system(sendBatchScript_command)
  #
  os.system('rm -f ' + fName)
