import os
import glob

def main():

  # txtFilePath="./ccin2p3/mc5a02/root/mc5a02_oaEventTree_rootfiles.txt"
  # filesToGlob="/sps/hep/comet/cometmgr/icedust_mc5/MC5A02/data/root/oa_g4_*.root"
  # MakeLists(txtFilePath,filesToGlob)

  # txtFilePath="./ccin2p3/mc5a02/rootracker/mc5a02_rootrackerfiles.txt"
  # filesToGlob="/sps/hep/comet/cometmgr/icedust_mc5/MC5A02/data/rootracker/oa_g4_*.rootracker"
  # MakeLists(txtFilePath,filesToGlob)

  # txtFilePath="./ccin2p3/mc5a02/root/mc5a02_oaEventTree_mergedbunches_rootfiles.txt"
  # filesToGlob="/scratch/comet/samplesFromCCIN2P3/icedust_mc5/MC5A02/data/root/merged_1b_*.root"
  # MakeLists(txtFilePath,filesToGlob)

  # txtFilePath="./umhpc/mc5a02/root/mc5a02_oaEventTree_rootfiles.txt"
  # filesToGlob="/lustre/project/comet/samplesFromCCIN2P3/icedust_mc5/MC5A02/data/root/oa_g4_*.root"
  # MakeLists(txtFilePath,filesToGlob)

  # txtFilePath="./umhpc/mc5a02/rootracker/mc5a02_rootrackerfiles.txt"
  # filesToGlob="/lustre/project/comet/samplesFromCCIN2P3/icedust_mc5/MC5A02/data/rootracker/oa_g4_*.rootracker"
  # MakeLists(txtFilePath,filesToGlob)

  # txtFilePath="./umhpc/mc5a02/root_mergedbunch/mc5a02_oaEventTree_mergedbunches_rootfiles.txt"
  # filesToGlob="/lustre/project/comet/samplesFromCCIN2P3/icedust_mc5/MC5A02/data/root/merged_1b_*.root"
  # MakeLists(txtFilePath,filesToGlob)

  # txtFilePath="./umhpc/mc5a01/rootracker/mc5a01_rootrackerfiles.txt"
  # filesToGlob="/lustre/project/comet/samplesFromCCIN2P3/icedust_mc5/MC5A01/rootracker_merged_by_100/*.rootracker"
  # MakeLists(txtFilePath,filesToGlob)

  # txtFilePath="./umhpc/piMinusParticleGun/root/piMinusParticleGun_oaEventTree.txt"
  # filesToGlob="/scratch/comet/nurfikri/data/piMinusParticleGun/root/oa_g4_pim_*.root"
  # MakeLists(txtFilePath,filesToGlob)
  
  txtFilePath="/home/user/mdimas/basic_studies/CyDetMomCalib/AnaOAEvent/TempSampleLists/piMinusGunRooTrackHist_SimG4_default.txt"
  filesToGlob="/lustre/project/comet/nurfikri/data/piMinusParticleGun_fromRooTrackHistMC5A01/workdir_default/oa_g4_pim_*.root"
  MakeLists(txtFilePath,filesToGlob)

  txtFilePath="/home/user/mdimas/basic_studies/CyDetMomCalib/AnaOAEvent/TempSampleLists/piMinusGunRooTrackHist_SimG4_polyethylene.txt"
  filesToGlob="/lustre/project/comet/nurfikri/data/piMinusParticleGun_fromRooTrackHistMC5A01/workdir_polyethylene/oa_g4_pim_*.root"
  MakeLists(txtFilePath,filesToGlob)

def MakeLists(txtFilePath,filesToGlob):

  #
  # Get the files list by globbing
  #
  filesList = glob.glob(filesToGlob)
  filesListFinal = [files for files in filesList]
  filesListFinal = sorted(filesListFinal)
  #
  #
  #
  print "Make list", len(filesListFinal), " files"
  with open(txtFilePath, 'w') as f:
    f.writelines("%s\n" % file for file in filesListFinal)

if __name__== "__main__":
  main()



