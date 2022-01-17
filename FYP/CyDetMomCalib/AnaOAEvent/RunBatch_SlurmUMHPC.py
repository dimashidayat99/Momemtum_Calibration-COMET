import sys
import os
import subprocess

cwd = os.getcwd()
setupEnvPath = "/scratch/nurfikri/comet/SetupEnv.sh"
#
# Specify macro name
#
macroName = "Analyzer.C"

#
# Check how many groups we split for the sample in ../../SampleList/
#
nParts = 20 #Default is 20

#
# Make the bash script
#
for iPart in range(0, nParts):
  #
  #
  #
  fName = 'Batch_part%d.sh' %(iPart)
  #
  #
  #
  txtFileDir  = '../../SampleList/umhpc/mc5a02/root'
  txtFileName = 'mc5a02_oaEventTree_rootfiles_part%d' %(iPart)
  #
  #
  #
  f = open(fName, 'w')
  f.write('#!/bin/bash -l\n')  
  f.write('#SBATCH --partition=cpu-standard\n')
  f.write('#SBATCH --output=BatchLog/%x.%j.out\n')
  f.write('#SBATCH --error=BatchLog/%x.%j.err\n')
  f.write('#SBATCH --mem=4G\n')
  f.write('#SBATCH --ntasks=1\n')
  f.write('#SBATCH --nodes=1\n')
  f.write('\n')
  # f.write('echo \"START TIME\" \n')
  f.write('cd {:s} \n'.format(cwd))
  f.write('source {:s} \n'.format(setupEnvPath))
  # command = 'python -u RunLocal.py -m {:s} -t {:s} | tee ./logfiles/logfile_part{:d}.log'.format(macroName,txtFileName,iPart)
  command = 'python -u RunLocal.py -m {:s} -d {:s} -t {:s} '.format(macroName,txtFileDir,txtFileName)
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