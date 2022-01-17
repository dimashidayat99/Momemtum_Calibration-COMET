import sys
import os
import subprocess

cwd = os.getcwd()

#
# NOTE: Setup your COMET path
#
setupEnvPath = "/scratch/nurfikri/comet/SetupEnv.sh" 

TXTFILELISTDIR    = "../../SampleList/umhpc/mc5a01/rootracker/"
TXTFILELIST       = "mc5a01_rootrackerfiles"
OUTDIR            = "./output/"
OUTPUTFILEPOSTFIX = "skimmedPiMinus"

################################################
#
# Get list of rootracker files
#
################################################
fileListToRun = []

txtFilePath = TXTFILELISTDIR + "/" + TXTFILELIST + ".txt";
#
# If the txt file exist, store the root files paths into a list
#
if os.path.exists(txtFilePath):
  with open(txtFilePath) as f:
    fileListToRun = f.read().splitlines()
else:
  raise Exception('Cannot find text file containing input list! Here is the specified path: {}'.format(txtFilePath))

#
# Make output directory if it doesn't exist
#
if not os.path.exists(OUTDIR):
  os.makedirs(OUTDIR)
#
# Make BatchLog directory if it doesn't exist
#
if not os.path.exists("./BatchLog"):
  os.makedirs("./BatchLog")

#
# Make the bash script
#
for iPart, inFilePath in enumerate(fileListToRun):
  # 
  # input
  # 
  inFileName = inFilePath.split("/")[-1] 
  fileName   = inFileName.replace(".rootracker","")
  # 
  # output
  # 
  outFilePath = OUTDIR+"/"+fileName+"_"+OUTPUTFILEPOSTFIX+".rootracker"
  #
  # 
  #
  fName = 'Batch_%s.sh' %(fileName)
  #
  #
  #
  f = open(fName, 'w')
  f.write('#!/bin/bash -l\n')  
  f.write('#SBATCH --partition=cpu-standard\n')
  f.write('#SBATCH --output=BatchLog/%x.%j.out\n')
  f.write('#SBATCH --error=BatchLog/%x.%j.err\n')
  f.write('#SBATCH --mem=2G\n')
  f.write('#SBATCH --ntasks=1\n')
  f.write('#SBATCH --nodes=1\n')
  f.write('\n')
  # f.write('echo \"START TIME\" \n')
  f.write('cd {:s} \n'.format(cwd))
  f.write('source {:s} \n'.format(setupEnvPath))
  command = 'root -l -b -q SkimRootracker.C\\(\\\"{:s}\\\",\\\"{:s}\\\"\\)'.format(inFilePath,outFilePath)
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

