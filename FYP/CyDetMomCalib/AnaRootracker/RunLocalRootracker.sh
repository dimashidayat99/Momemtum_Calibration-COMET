#!/bin/sh

mkdir -p output

INFILE="/scratch/comet/samplesFromCCIN2P3/icedust_mc5/MC5A01/rootracker_merged_by_100/00001-00100.rootracker"
OUTFILE="./output/00001-00100_skimmedPiMinus.rootracker"

root -l -b -q SkimRootracker.C\(\"${INFILE}\",\"${OUTFILE}\"\)
