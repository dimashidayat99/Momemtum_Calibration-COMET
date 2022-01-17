import os
import sys
import glob
import optparse
import subprocess
import argparse
from datetime import datetime

TIME_START_PROCESS=datetime.now()

parser = argparse.ArgumentParser("")
parser.add_argument('-t','--txtFileList',    type=str, default="")
parser.add_argument('-d','--txtFileListDir', type=str, default="")
parser.add_argument('-n','--nFilesToRun',    type=int, default=-1)
parser.add_argument('-i','--inputFile',      type=str, default="")
parser.add_argument('-o','--outDir',         type=str, default="")
parser.add_argument('-m','--macroName',      type=str, default="")
args = parser.parse_args()

################################################
#
# Specify macro name
#
################################################
if args.macroName != "":
  macroName = args.macroName
else:
  raise Exception('Must specify macroName')

################################################
#
# Get list of files
#
################################################
fileList = []
#
# Get path to txt file contiaining list of root files
#
if args.txtFileListDir != "" and args.txtFileList != "":
  txtFilePath = args.txtFileListDir + "/" + args.txtFileList + ".txt";
  #
  # If the txt file exist, store the root files paths into a list
  #
  if os.path.exists(txtFilePath):
    with open(txtFilePath) as f:
      fileList = f.read().splitlines()
  else:
    raise Exception('Cannot find text file containing input list! Here is the specified path: {}'.format(txtFilePath))
#
# If we want to run over EXACTLY one root file
#
elif args.inputFile != "":
  fileList.append(args.inputFile)

#
#
#
print("List of root files from txt file:")
for iF, inFilePath in enumerate(fileList):
  print(str(iF)+" | "+inFilePath)
print("\n")

#
# 
#
fileListToRun = []
if args.nFilesToRun > 0: 
  print("Will process the first "+str(args.nFilesToRun)+" root files")
  fileListToRun = fileList[0:args.nFilesToRun]
else:
  print("Will process all root files")
  fileListToRun = fileList

print("List of root files to process:")
for iF, inFilePath in enumerate(fileListToRun):
  print(str(iF)+ " | "+inFilePath)
print("\n")
################################################
#
# Specify output directory
#
################################################
OUTDIR      = "./histos"
OUTPUTFILEPOSTFIX = "histos"

if args.outDir != "":
  OUTDIR=args.outDir
#
# Make output directory if it doesn't exist
#
if not os.path.exists(OUTDIR):
  os.makedirs(OUTDIR)
################################################
#
# Run macro per input root file
#
################################################
print("Using macro: "+macroName)

for iF, inFilePath in enumerate(fileListToRun):
  # 
  # input
  # 
  inFileName = inFilePath.split("/")[-1] 
  fileName   = inFileName.replace(".root","")
  # 
  # output
  # 
  outFilePath = OUTDIR+"/"+fileName+"_"+OUTPUTFILEPOSTFIX+".root";
  #
  #
  #

  print ("====================")
  print (str(iF)+"/"+str(len(fileListToRun)))
  print ("MACRO  :"+macroName)
  print ("INPUT  :"+inFilePath)
  print ("OUTPUT :"+outFilePath )
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
  print ("TIME_CURRENT: "+str(datetime.now()))
  print ("\n\n")
#
#
#
print("=================================================================")
TIME_END_PROCESS=datetime.now()
print("TIME_START_PROCESS : "+str(TIME_START_PROCESS))
print("TIME_END_PROCESS   : "+str(TIME_END_PROCESS))
print("JOB::DONE")