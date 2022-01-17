import os
import sys
import glob
import optparse
import subprocess
import argparse

################################################
#
# Specify macro name
#
################################################
macroName  = "Analyzer.C"
# inFilePath = "/scratch/nurfikri/comet/particlegun_pion/Backup_NotAllTrajSaved/oa_g4_pim_00000002-0000_mq3ahou6np2h_SG4_000.root"
# inFilePath = "/scratch/nurfikri/comet/particlegun_pion/Backup_AllTrajSaved/oa_g4_pim_00000002-0000_wgktooqmamlj_SG4_000.root"
# inFilePath = "/scratch/comet/samplesFromCCIN2P3/icedust_mc5/MC5A02/data/root/oa_g4_xxx_00000002-0000_ymi6ghuadw6p_SG4BH_000.root"
OUTDIR     = "./"

################################################
#

# Run macro per file
#
################################################
# 
#  input
# 
inFileName = inFilePath.split("/")[-1] 
fileName   = inFileName.replace(".root","")
# 
# output
# 
outFilePath = OUTDIR+"/"+fileName+"_histoTest.root";
#
#
#
print "===================="
print "MACRO  :", macroName
print "INPUT  :", inFilePath
print "OUTPUT :", outFilePath 
#
#
#
cmd  = ["root"]
cmd += ["-b","-q","-l"]
cmd += ["RunMacro.C(\"%s\",\"%s\",\"%s\")" %(macroName, inFilePath, outFilePath)]
#
#
#
subprocess.call(cmd)
