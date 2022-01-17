#!/bin/bash

module load git/git-2.30.1
module load cmake/cmake-3.16.4 

ICEDUSTFULLPATH=/home/user/mdimas/comet/icedust
source ${ICEDUSTFULLPATH}/ICEDUST_install/setup.sh
source ${ICEDUSTFULLPATH}/ICEDUST_fieldmaps/150630_Phase-I_opt/enable.sh
