import ROOT
import collections

ROOT.gROOT.SetBatch(True)

def PrintCutFlow(inFileName):

  print("Opening File: "+inFileName)
  inFile    = ROOT.TFile.Open(inFileName)
  h_cutflow = inFile.Get("h_cutflow")

  nbins = h_cutflow.GetNbinsX()
  count = collections.OrderedDict()
  eff   = collections.OrderedDict()

  denomLabel = "InitialEvents"

  for iBin in xrange(1,nbins+1):
    binLabel = h_cutflow.GetXaxis().GetBinLabel(iBin)
    count[binLabel] = h_cutflow.GetBinContent(iBin)
    eff[binLabel]   = (count[binLabel] / count[denomLabel])


  for label in eff:
    if eff[binLabel] >= 1:
      print("{:40s}:{:.10f} %({:.0f})".format(label, eff[label], count[label]))
    else:
      print("{:40s}:{:.1e} % ({:.0f})".format(label, eff[label], count[label]))

  inFile.Close()
  print("\n\n")

tags = [
  # "CombineHistos_default.root",
  # "CombineHistos_polystyrene.root", 
  # "CombineHistos_polyethylene.root",
  # "CombineHistos_polypropylene.root",
  # "CombineHistos_polyvinyltoluene.root",
  "CombineHistos_piMinusGun_default.root",
  "CombineHistos_piMinusGun_polyethylene.root",
]

for tag in tags:
  PrintCutFlow(tag)
