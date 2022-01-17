import itertools
import os
import glob

def chunks(l, n):
  """Yield successive n-sized chunks from l."""
  for i in range(0, len(l), n):
    yield l[i:i + n]

def main(inDir, txtFileName, nGroupFiles=10):
  listOfTxtFiles = glob.glob(inDir+"/"+txtFileName)

  print (listOfTxtFiles)

  for txtFile in listOfTxtFiles: 
    sampleName = txtFile.replace(".txt","")
    sampleName = sampleName.replace(inDir+"/","")
    with open(txtFile) as f:
      files = f.read().splitlines()
      filesChunks = list(chunks(files,nGroupFiles))
      i=0
      for fileChunk in filesChunks:
        txtFileSplitName = inDir+"/"+sampleName+"_part"+str(i)+".txt"
        fOut = open(txtFileSplitName, "w")
        for line in fileChunk:
          # write line to output file
          fOut.write(line + "\n")
        fOut.close()
        i += 1

if __name__ == "__main__":

  # inDir="./ccin2p3/mc5a02/root"
  # txtFileName="mc5a02_oaEventTree_rootfiles.txt"
  # nGroupFiles=10

  # inDir="./ccin2p3/mc5a02/rootracker"
  # txtFileName="mc5a02_rootrackerfiles.txt"
  # nGroupFiles=10

  # inDir="./umhpc/mc5a02/root"
  # txtFileName="mc5a02_oaEventTree_rootfiles.txt"
  # nGroupFiles=10

  # inDir="./umhpc/mc5a02/rootracker"
  # txtFileName="mc5a02_rootrackerfiles.txt"
  # nGroupFiles=10

  # inDir="./umhpc/piMinusParticleGun/root"
  # txtFileName="piMinusParticleGun_oaEventTree.txt"
  # nGroupFiles=100

  main(inDir,txtFileName,nGroupFiles)
