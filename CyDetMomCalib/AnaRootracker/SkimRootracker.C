void SkimRootracker(TString inFilePath, TString outFilePath) {
  
  //
  // Get input file and input RooTrackerTree
  //
  TFile* inputFile = TFile::Open(inFilePath);
  TTree* inTree = (TTree*)inputFile->Get("RooTrackerTree");
  
  //
  // Setup to read inTree
  //
  static const int kNPmax = 50;
  int fStdHepN;
  int fStdHepPdg[kNPmax];
  int fStdHepStatus[kNPmax]; 
  double fStdHepX4[kNPmax][4];
  inTree->SetBranchAddress("StdHepN", &fStdHepN);
  inTree->SetBranchAddress("StdHepPdg", fStdHepPdg);
  inTree->SetBranchAddress("StdHepX4", fStdHepX4);
  inTree->SetBranchAddress("StdHepStatus", fStdHepStatus);

  //
  // Make a new output file and store new RooTrackerTree
  //
  bool saveInNewTree = true; //Set to false for debugging

  TFile* outputFile = nullptr;
  TTree* outTree = nullptr;
  if (saveInNewTree){
    outputFile = TFile::Open(outFilePath, "RECREATE");
    outTree = inTree->CloneTree(0);
  }

  //
  // Loop over events
  //
  bool hasPionPrimary = false;
  unsigned int nEntries = inTree->GetEntries();

  for(int i = 0; i < nEntries; ++i) {
    inTree->GetEntry(i);

    if (i%5000 == 0){
      std::cout << "Event: "<< i << "/" << nEntries<< std::endl;
    }
    // if (i > 1000000) break;
    
    //
    // Loop over primary particles ands see if we have a pion-Minus
    //
    //
    hasPionPrimary=false;
    for(int cnt = 0; cnt < fStdHepN; ++cnt) {
      if (fStdHepPdg[cnt] == -211 ){
        hasPionPrimary = true; 
      }
    }
    //
    //
    //
    if (hasPionPrimary){
      if (saveInNewTree && outTree){
        outTree->Fill();
      }
    }
  }

  //
  // Close output file
  //
  if (saveInNewTree && outputFile){
    outputFile->Write();
    outputFile->Close();
  }
}