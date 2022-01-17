import sys
import glob
import os
import subprocess

cwd = os.getcwd()
#
# NOTE: Specify your own ICEDUST setup script
#
setupEnvPath = "/scratch/nurfikri/comet/SetupEnv.sh"
#
#
#
NEVENTS=5000 #Each skimmed rootracker files should have about less than 2000 events. 
#
#
#
JOBS = [
  ("default",         "./config/rootrackerMC5A01_skimPiMinus_default.cfg",           "workdir_default"),
  ("polystyrene",     "./config/rootrackerMC5A01_skimPiMinus_polystyrene.cfg",       "workdir_polystyrene"),
  ("polyethylene",    "./config/rootrackerMC5A01_skimPiMinus_polyethylene.cfg",      "workdir_polyethylene"),
  ("polypropylene",   "./config/rootrackerMC5A01_skimPiMinus_polypropylene.cfg",     "workdir_polypropylene"),
  ("polyvinyltoluene","./config/rootrackerMC5A01_skimPiMinus_polyvinyltoluene.cfg",  "workdir_polyvinyltoluene"),
]
#
# Get list of skimmed rootracker files.
# NOTE: You should specify the path to your own skimmed rootracker files if you made them yourself.
# This is Fikri's version. 
#
inFileList = [f for f in glob.glob("/scratch/comet/nurfikri/data/mc5a01_rootracker_skimPiMinus/*.rootracker")]
inFileList.sort()
# inFileList = inFileList[5:]

#
# Make the bash script
#
for job in JOBS:
  JOB_NAME = job[0]
  CFG_FILE = job[1]
  WORK_DIR = job[2]
  #
  # Loop over input file
  #
  for iFile, inFilePath in enumerate(inFileList):
    #
    # Specify random seed.
    #
    rndmSeed = (5<<16)+2
    #
    #
    #
    INPUT_FILE=inFilePath
    iFileStr = str(iFile).zfill(3)
    #
    #
    #
    fName      = 'Job_{:s}_{:s}.sh'.format(JOB_NAME,iFileStr)
    SUBJOB_DIR = 'Job_{:s}_{:s}'.format(JOB_NAME,iFileStr)
    #
    #
    #
    # if "default" in JOB_NAME:
    #     if iFile not in [7,17,23]: continue
    # elif "polystyrene" in JOB_NAME:
    #     if iFile not in [186]: continue
    # else:
    #     continue
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
    f.write('cd {:s} \n'.format(cwd))
    f.write('source {:s} \n'.format(setupEnvPath))
    f.write('export SH_NUM_EVENTS={:s}\n'.format(str(NEVENTS)))
    f.write('export SH_RUN_NUMBER={:s}\n'.format(str(0)))
    f.write('export SH_SUBRUN={:s}\n'.format(str(iFile)))
    f.write('export SH_RANDOM_SEED={:s}\n'.format(str(rndmSeed)))
    f.write('export INPUT_FILE={:s}\n'.format(INPUT_FILE))
    f.write('export ICEDUSTCONTROLPATH=$ICEDUSTINSTALLPATH/IcedustControl\n')
    f.write('cd {:s} \n'.format(WORK_DIR))
    f.write('mkdir -p {:s} \n'.format(SUBJOB_DIR))
    f.write('cd {:s} \n'.format(SUBJOB_DIR))
    command = '$ICEDUSTCONTROLPATH/app/RunIcedustControl -c {:s}/{:s}'.format(cwd, CFG_FILE)
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
