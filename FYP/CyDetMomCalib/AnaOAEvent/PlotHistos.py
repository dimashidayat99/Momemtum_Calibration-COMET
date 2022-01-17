import os
import ROOT
import rootlogon
ROOT.gROOT.SetBatch(True)

ROOT.gStyle.SetPalette(ROOT.kCherry) # https://root.cern.ch/doc/master/classTColor.html
ROOT.TColor.InvertPalette()

# ROOT.gStyle.SetPalette(ROOT.kRainBow) # https://root.cern.ch/doc/master/classTColor.html

# ROOT.gStyle.SetPalette(ROOT.kGreyScale) # https://root.cern.ch/doc/master/classTColor.html
# ROOT.TColor.InvertPalette()

# ROOT.gStyle.SetPalette(ROOT.kDarkBodyRadiator) # https://root.cern.ch/doc/master/classTColor.html
# ROOT.TColor.InvertPalette()

def PlotTH1(histo,xaxisname,yaxisname,pdfname,doLogY):
  c = ROOT.TCanvas("c","",800,800)
  c.SetFillStyle( 4000 )
  c.SetLeftMargin(0.15)
  c.SetRightMargin(0.08)
  c.SetTopMargin(0.05)
  c.SetBottomMargin(0.15)

  histoC = histo.Clone()

  histoC.SetLineWidth(2)
  histoC.GetXaxis().SetTitle(xaxisname)
  histoC.GetYaxis().SetTitle(yaxisname)

  histoC.Draw("HIST")

  if doLogY:
    c.SetLogy()
  
  c.Print("./"+pdfname+".pdf")

  del c

def MakePlots(inFileName,plotDir):

  inFile = ROOT.TFile.Open(inFileName)
  doLogY = False

  histos = [

     #["h_piPrimary_e",                   "Primary pion energy [MeV]","Events"],
     #["h_piPrimary_mom",                 "Primary pion momentum [MeV]","Events"],
     #["h_pi0_e",                         "pion0 energy [MeV]","Events"],
     #["h_pi0_mom",                       "pion0 momentum [MeV]","Events"],
     #["h_onegamma_e",                    "(1-photon) photon energy [MeV]","Events"],
     #["h_twogamma_lead_e",               "(2-photon) Lead photon energy [MeV]","Events"],
     #["h_twogamma_sublead_e",            "(2-photon) Sub-lead photon energy [MeV]","Events"],
     #["h_onegamma_electron_e",           "(1-photon) Electron energy [MeV]","Events"],
     #["h_onegamma_electron_mom",         "(1-photon) Electron momentum [MeV]","Events"],
     #["h_onegamma_positron_e",           "(1-photon) Positron energy [MeV]","Events"],
     #["h_onegamma_positron_mom",         "(1-photon) Positron momentum [MeV]","Events"],
     #["h_twogamma_lead_electron_e",      "(2-photons,Lead photon) Electron energy [MeV]","Events"],
     #["h_twogamma_lead_electron_mom",    "(2-photons,Lead photon) Electron momentum [MeV]","Events"],
     #["h_twogamma_lead_positron_e",      "(2-photons,Lead photon) Positron energy [MeV]","Events"],
     #["h_twogamma_lead_positron_mom",    "(2-photons,Lead photon) Positron momentum [MeV]","Events"],
     #["h_twogamma_sublead_electron_e",   "(2-photons,SubLead photon) Electron energy [MeV]","Events"],
     #["h_twogamma_sublead_electron_mom", "(2-photons,SubLead photon) Electron momentum [MeV]","Events"],
     #["h_twogamma_sublead_positron_e",   "(2-photons,SubLead photon) Positron energy [MeV]","Events"],
     #["h_twogamma_sublead_positron_mom", "(2-photons,SubLead photon) Positron momentum [MeV]","Events"],
     ["h_gamma_decayvtx_r", "Transverse distance from z-axis [mm]","Counts"],
     ["h_gamma_decayvtx_z", "z coordinate [mm]","Counts"],
  ]

  #
  # Make output directories
  #
  if not os.path.exists(plotDir):
    os.makedirs(plotDir)

  for histList in histos:
    histName  = histList[0]
    xaxisname = histList[1]
    yaxisname = histList[2]
    pdfname   = histName

    histo = inFile.Get(histName)
    PlotTH1(histo, xaxisname, yaxisname, plotDir+pdfname, doLogY)

  inFile.Close()


def PlotTH2(histo,xaxisname,yaxisname,pdfname):
  c = ROOT.TCanvas("c","",1200,800)
  c.SetFillStyle( 4000 )
  c.SetLeftMargin(0.12)
  c.SetRightMargin(0.10)
  c.SetTopMargin(0.05)
  c.SetBottomMargin(0.12)

  histoC = histo.Clone()

  histoC.GetXaxis().SetTitle(xaxisname)
  histoC.GetYaxis().SetTitle(yaxisname)

  histoC.Draw("COLZ")
  
  c.Print("./"+pdfname+".pdf")

  del c

def MakePlots2D(inFileName,plotDir):

  inFile = ROOT.TFile.Open(inFileName)
  # keys =  inFile.GetListOfKeys()
  # for k in keys:
  #   print(k.GetName())

  histos = [
    #["h2_gamma_decayvtx_yx", "",
    #["h2_gamma_decayvtx_xz", "",
    #["h2_gamma_decayvtx_yz", "",
    ["h2_gamma_decayvtx_rz" ,"z[mm]", "Transverse distance from z-axis [mm]"],
    ["h2_gamma_decayvtx_rz_v3" ,"z[mm]", "Transverse distance from z-axis [mm]"],
    ["h3_gamma_decayvtx_xyz","x[mm]","y[mm]","z[mm]"] 
  ]

  #
  # Make output directories
  #
  if not os.path.exists(plotDir):
    os.makedirs(plotDir)

  for histList in histos:
    histName  = histList[0]
    xaxisname = histList[1]
    yaxisname = histList[2]
    pdfname   = histName

    histo = inFile.Get(histName)
    PlotTH2(histo, xaxisname, yaxisname, plotDir+pdfname)

  inFile.Close()

tags = [
  #("CombineHistos_piMinusGun_default.root",        "plots_piMinusGun_default/"),
  ("CombineHistos_piMinusGun_polyethylene.root",   "plots_piMinusGun_polyethylene/"),
]

for tag in tags:
  MakePlots(tag[0],tag[1])

for tag in tags:
  MakePlots2D(tag[0],tag[1])
