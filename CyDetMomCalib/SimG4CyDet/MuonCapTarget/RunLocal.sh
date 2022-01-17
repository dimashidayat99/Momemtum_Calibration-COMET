#!/bin/sh

export SH_NUM_EVENTS=5000
export SH_RUN_NUMBER=0
export SH_SUBRUN=1
export SH_RANDOM_SEED=327682
export INPUT_FILE=/scratch/comet/nurfikri/data/mc5a01_rootracker_skimPiMinus/00001-00100_skimmedPiMinus.rootracker
export ICEDUSTCONTROLPATH=$ICEDUSTINSTALLPATH/IcedustControl

# mkdir -p workdir_default
# cd workdir_default
# $ICEDUSTCONTROLPATH/app/RunIcedustControl -c ./config/rootrackerMC5A01_skimPiMinus_default.cfg

mkdir -p workdir_polyvinyltoluene
cd workdir_polyvinyltoluene
$ICEDUSTCONTROLPATH/app/RunIcedustControl -c ./config/rootrackerMC5A01_skimPiMinus_polyvinyltoluene.cfg

