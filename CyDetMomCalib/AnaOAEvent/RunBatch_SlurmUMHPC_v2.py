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

# JOBS=[
#   ("default",            "skimPiMinus_SimG4_default"),
#   ("polystyrene",        "skimPiMinus_SimG4_polystyrene"),
#   ("polyethylene",       "skimPiMinus_SimG4_polyethylene"),
#   ("polypropylene",      "skimPiMinus_SimG4_polypropylene"),
#   ("polyvinyltoluene",   "skimPiMinus_SimG4_polyvinyltoluene"),
# ]
JOBS=[
  ("piMinusGun_default_part0",      "piMinusGunRooTrackHist_SimG4_default_part0"),
  ("piMinusGun_default_part1",      "piMinusGunRooTrackHist_SimG4_default_part1"),
  ("piMinusGun_default_part2",      "piMinusGunRooTrackHist_SimG4_default_part2"),
 # ("piMinusGun_default_part3",      "piMinusGunRooTrackHist_SimG4_default_part3"),
 # ("piMinusGun_default_part4",      "piMinusGunRooTrackHist_SimG4_default_part4"),
  ("piMinusGun_polyethylene_part0", "piMinusGunRooTrackHist_SimG4_polyethylene_part0"),
  ("piMinusGun_polyethylene_part1", "piMinusGunRooTrackHist_SimG4_polyethylene_part1"),
  ("piMinusGun_polyethylene_part2", "piMinusGunRooTrackHist_SimG4_polyethylene_part2"),
 # ("piMinusGun_polyethylene_part3", "piMinusGunRooTrackHist_SimG4_polyethylene_part3"),
 # ("piMinusGun_polyethylene_part4", "piMinusGunRooTrackHist_SimG4_polyethylene_part4"),
]

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
  fName = 'Batch_{:s}.sh'.format(jobName)
  f = open(fName, 'w')
  f.write('#!/bin/bash -l\n')  
  f.write('#SBATCH --partition=cpu-opteron\n')
  f.write('#SBATCH --output=BatchLog/%x.%j.out\n')
  f.write('#SBATCH --error=BatchLog/%x.%j.err\n')
  f.write('#SBATCH --mem=4G\n')
  f.write('#SBATCH --ntasks=1\n')
  f.write('#SBATCH --nodes=1\n')
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
  sendBatchScript_command = 'sbatch %s' % fName
  os.system(sendBatchScript_command)
  #
  os.system('rm -f ' + fName)
