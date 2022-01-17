import ROOT
print "Using %s" % __file__

# whitening
ROOT.gStyle.SetFrameBorderMode(0)
ROOT.gStyle.SetFrameFillColor(0)
ROOT.gStyle.SetFrameLineColor(0)
ROOT.gStyle.SetFrameLineWidth(0)
ROOT.gStyle.SetCanvasBorderMode(0)
ROOT.gStyle.SetCanvasColor(0)
ROOT.gStyle.SetPadBorderMode(0)
ROOT.gStyle.SetPadColor(0)
ROOT.gStyle.SetStatColor(0)
ROOT.gStyle.SetDrawBorder(0)

# pad margins
# ROOT.gStyle.SetPadTopMargin(0.05)
# ROOT.gStyle.SetPadRightMargin(0.05)
# ROOT.gStyle.SetPadBottomMargin(0.16)
# ROOT.gStyle.SetPadLeftMargin(0.16)

ROOT.gStyle.SetPadTopMargin(0.05)
ROOT.gStyle.SetPadRightMargin(0.05)
ROOT.gStyle.SetPadBottomMargin(0.00)
ROOT.gStyle.SetPadLeftMargin(0.15)

ROOT.gStyle.SetTitleOffset(1.3, 'x')
ROOT.gStyle.SetTitleOffset(1.4, 'y')

# fonts
font = 42
ROOT.gStyle.SetTextFont(font)
ROOT.gStyle.SetLabelFont(font, 'xyz')
ROOT.gStyle.SetTitleFont(font, 'xyz')
ROOT.gStyle.SetTitleFont(font, 't')
ROOT.gStyle.SetStatFont(font)

# text sizes
ROOT.gStyle.SetTextSize(0.05)
ROOT.gStyle.SetLabelSize(0.05, 'xyz')
ROOT.gStyle.SetTitleSize(0.05, 'xyz')
ROOT.gStyle.SetTitleSize(0.05, 't')
ROOT.gStyle.SetStatFontSize(0.04)

# stat box
ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetStatH(0.2)
ROOT.gStyle.SetStatW(0.2)
ROOT.gStyle.SetStatX(0.99)

# title
ROOT.gStyle.SetOptTitle(0)
ROOT.gStyle.SetTitleColor(1)
ROOT.gStyle.SetTitleFillColor(0)
ROOT.gStyle.SetTitleStyle(0)
ROOT.gStyle.SetTitleBorderSize(0)
ROOT.gStyle.SetTitleY(0.99)
ROOT.gStyle.SetTitleX(.1)

# get rid of error bar caps
ROOT.gStyle.SetEndErrorSize(0.)

#get rid of x error
#ROOT.gStyle.SetErrorX(0)

# more ticks
ROOT.gStyle.SetPadTickX(1)
ROOT.gStyle.SetPadTickY(1)
