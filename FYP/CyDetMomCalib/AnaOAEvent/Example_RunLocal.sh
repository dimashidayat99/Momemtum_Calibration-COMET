#!/bin/bash
MACRONAME="Analyzer.C"
TXTFILEDIR="../../SampleList/umhpc/mc5a02/root/"
TXTFILE="mc5a02_oaEventTree_rootfiles_part0"
NFILES=3

python -u RunLocal.py -m $MACRONAME -d $TXTFILEDIR -t $TXTFILE -n $NFILES
