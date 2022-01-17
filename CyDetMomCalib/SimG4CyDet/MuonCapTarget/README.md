# Muon Stopping Target Material studies

This directory contains the scripts needed to run SimG4 simulation of CyDet with different Muon Stopping Target material.
This is done in the context of studying the effect of different target material on the pion-minus capture rate in order 
to increase the number of POT events with radiative pion capture (RPC) processes.

The inputs to the SimG4 simulation are [MC5A01](https://gitlab.in2p3.fr/comet/ICEDUST_productions/-/wikis/MC5A01) output 
rootracker files. The list of rootracker files located at `ccin2p3` and `umhpc` can be found in the `SampleList` 
[directory](SampleList/) in the main repo.


Rather than simulating all POT events in MC5A01, we use a skimmed collection of MC5A01 rootracker files where we save 
POT events with at least one pion minus in the list of primary particles. This will speed up the SimG4 production 
greatly because we are only interested with events with pion minus entering the CyDet. The code for performing this 
skim can be found in `CyDetMomCalib/AnaRootracker` [directory](CyDetMomCalib/AnaRootracker).
