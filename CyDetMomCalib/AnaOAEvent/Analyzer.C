#include "ICTHGeom.hxx"
#include "IG4Trajectory.hxx"
#include "IHandle.hxx"

void Analyzer(TString inFileName, TString outFileName) {

  gROOT->SetBatch(1);

  using namespace std;
  using namespace COMET;

  bool debug = false;

  TStopwatch* timer = new TStopwatch();
  timer->Start();
 
  TGeoManager::Import(inFileName);
  // cout << IGeomInfo::CTH().GetNumberOfModules()  << endl;
  // cout << IGeomInfo::CTH().GetNumberOfCounters() << endl;
  // cout << IGeomInfo::CTH().GetNumberOfLayers()   << endl;
  // cout << IGeomInfo::CTH().GetNumberOfSegments() << endl;
  gGeoManager->PushPath();
  gGeoManager->GetTopNode()->cd();
  
  //
  // Open input file and retrieve the COMETEvents TTree
  //
  TFile* inFile = TFile::Open(inFileName); 
  TTree* inTree = (TTree*)inFile->Get("COMETEvents");

  //================================
  //
  //
  //
  //
  //================================
  ICOMETEvent* event = nullptr; // declare event pointer
  inTree->SetBranchAddress("COMETEvent", &event); // set the branch address to the pointer 

  IHandle<IG4TrajectoryContainer> g4Tracks(nullptr);
  IHandle<IG4HitContainer> g4HitsCDC(nullptr);
  IHandle<IG4HitContainer> g4HitsCTH(nullptr);
  IHandle<IHitSelection>   mcHitsCDC(nullptr);

  //================================
  //
  // Initialize histograms
  //
  //================================
  TH1D* h_cutflow = new TH1D("h_cutflow","h_cutflow",50,0,50);
  h_cutflow->GetXaxis()->SetBinLabel(1,"InitialEvents");
  h_cutflow->GetXaxis()->SetBinLabel(2,"PrimaryPionMinus");
  h_cutflow->GetXaxis()->SetBinLabel(3,"StoppedPionMinus");
  h_cutflow->GetXaxis()->SetBinLabel(4,"Pion0");
  h_cutflow->GetXaxis()->SetBinLabel(5,"OneGamma");
  h_cutflow->GetXaxis()->SetBinLabel(6,"TwoGamma");
  h_cutflow->GetXaxis()->SetBinLabel(7,"OneGamma_HasElectron");
  h_cutflow->GetXaxis()->SetBinLabel(8,"OneGamma_HasPositron");
  h_cutflow->GetXaxis()->SetBinLabel(9,"TwoGammaLead_HasElectron");
  h_cutflow->GetXaxis()->SetBinLabel(10,"TwoGammaLead_HasPositron");
  h_cutflow->GetXaxis()->SetBinLabel(11,"TwoGammaSubLead_HasElectron");
  h_cutflow->GetXaxis()->SetBinLabel(12,"TwoGammaSubLead_HasPositron");
  h_cutflow->GetXaxis()->SetBinLabel(13,"AtLeastOneElectronPositronPair");
  h_cutflow->GetXaxis()->SetBinLabel(14,"OneElectronPositronPair");
  h_cutflow->GetXaxis()->SetBinLabel(15,"TwoElectronPositronPair");

  h_cutflow->LabelsDeflate("X");

  TH1D* h_piPrimary_e   = new TH1D("h_piPrimary_e", "h_piPrimary_e",  200, 0., 800.);
  TH1D* h_piPrimary_mom = new TH1D("h_piPrimary_mom","h_piPrimary_mo", 200, 0., 800.);

  TH2D* h2_piPrimaryStopped_yz = new TH2D("h2_piPrimaryStopped_yz","h2_piPrimaryStopped_yz", 100, -250., 250.,  100, -250., 250.);//transverse
  TH2D* h2_piPrimaryStopped_yx = new TH2D("h2_piPrimaryStopped_yx","h2_piPrimaryStopped_yx", 100, -500., 500.,  100, -250., 250.);//cylinder

  TH1D* h_pi0_e   = new TH1D("h_pi0_e","h_pi0_e",     100, 0., 500.);
  TH1D* h_pi0_mom = new TH1D("h_pi0_mom","h_pi0_mom", 100, 0., 500.);

  TH1D* h_onegamma_e         = new TH1D("h_onegamma_e",        "h_onegamma_e",        100, 0., 200);
  TH1D* h_twogamma_lead_e    = new TH1D("h_twogamma_lead_e",   "h_onegamma_lead_e",   100, 0., 200);
  TH1D* h_twogamma_sublead_e = new TH1D("h_twogamma_sublead_e","h_onegamma_sublead_e",100, 0., 200);

  TH1D* h_onegamma_electron_e   = new TH1D("h_onegamma_electron_e",   "h_onegamma_electron_e",   100, 0., 200);
  TH1D* h_onegamma_electron_mom = new TH1D("h_onegamma_electron_mom", "h_onegamma_electron_mom", 100, 0., 200);
  TH1D* h_onegamma_positron_e   = new TH1D("h_onegamma_positron_e",   "h_onegamma_positron_e",   100, 0., 200);
  TH1D* h_onegamma_positron_mom = new TH1D("h_onegamma_positron_mom", "h_onegamma_positron_mom", 100, 0., 200);

  TH1D* h_twogamma_lead_electron_e   = new TH1D("h_twogamma_lead_electron_e",   "h_twogamma_lead_electron_e",   100, 0., 200);
  TH1D* h_twogamma_lead_electron_mom = new TH1D("h_twogamma_lead_electron_mom", "h_twogamma_lead_electron_mom", 100, 0., 200);
  TH1D* h_twogamma_lead_positron_e   = new TH1D("h_twogamma_lead_positron_e",   "h_twogamma_lead_positron_e",   100, 0., 200);
  TH1D* h_twogamma_lead_positron_mom = new TH1D("h_twogamma_lead_positron_mom", "h_twogamma_lead_positron_mom", 100, 0., 200);

  TH1D* h_twogamma_sublead_electron_e   = new TH1D("h_twogamma_sublead_electron_e",   "h_twogamma_sublead_electron_e",   100, 0., 200);
  TH1D* h_twogamma_sublead_electron_mom = new TH1D("h_twogamma_sublead_electron_mom", "h_twogamma_sublead_electron_mom", 100, 0., 200);
  TH1D* h_twogamma_sublead_positron_e   = new TH1D("h_twogamma_sublead_positron_e",   "h_twogamma_sublead_positron_e",   100, 0., 200);
  TH1D* h_twogamma_sublead_positron_mom = new TH1D("h_twogamma_sublead_positron_mom", "h_twogamma_sublead_positron_mom", 100, 0., 200);

  TH1D* h_gamma_decayvtx_r       = new TH1D("h_gamma_decayvtx_r",    "h_gamma_decayvtx_r",     360,      0, 1800.);
  TH1D* h_gamma_decayvtx_z       = new TH1D("h_gamma_decayvtx_z",    "h_gamma_decayvtx_z",     600, -3000., 3000.);

  TH2D* h2_gamma_decayvtx_yx      = new TH2D("h2_gamma_decayvtx_yx",   "h2_gamma_decayvtx_yx",    400, -2000., 2000., 400, -2000., 2000.);
  TH2D* h2_gamma_decayvtx_xz      = new TH2D("h2_gamma_decayvtx_xz",   "h2_gamma_decayvtx_xz",    600, -3000., 3000., 400, -2000., 2000.);
  TH2D* h2_gamma_decayvtx_yz      = new TH2D("h2_gamma_decayvtx_yz",   "h2_gamma_decayvtx_yz",    600, -3000., 3000., 400, -2000., 2000.);
  TH2D* h2_gamma_decayvtx_rz      = new TH2D("h2_gamma_decayvtx_rz",   "h2_gamma_decayvtx_rz",    600, -3000., 3000., 360,      0, 1800.);
  TH2D* h2_gamma_decayvtx_rz_v2   = new TH2D("h2_gamma_decayvtx_rz_v2","h2_gamma_decayvtx_rz_v2",  1000, -5000., 5000., 500, 0, 2500.);
  TH2D* h2_gamma_decayvtx_rz_v3   = new TH2D("h2_gamma_decayvtx_rz_v3","h2_gamma_decayvtx_rz_v3",  400, -2000., 2000., 280, 0, 1400.);


  TH3D* h3_gamma_decayvtx_xyz     = new TH3D("h3_gamma_decayvtx_xyz",  "h3_gamma_decayvtx_xyz",   200, -2000., 2000., 200, -2000., 2000., 300, -3000., 3000.);


  //================================
  //
  //
  // EVENT LOOP
  //
  //
  //================================

  unsigned int nEntries = inTree->GetEntries();

  if (debug){
    int maxEntries = 5000;
    if (nEntries > maxEntries) nEntries = maxEntries;
    cout << "DEBUG: set nEntries to " << nEntries << endl; 
  }


  cout << "Looping over tree with " << nEntries << endl; 
  for (size_t i=0; i<nEntries; ++i)
  {
    inTree->GetEntry(i);
    if (i%10000 == 0){
      std::cout << "Event: "<< i << "/" << nEntries<< std::endl;
    }

    //================================
    //
    //
    //
    //
    //================================
    h_cutflow->Fill("InitialEvents",1);

    g4Tracks = event->Get<IG4TrajectoryContainer>("truth/G4Trajectories");
    if (g4Tracks)
    {      
      // if (g4Tracks->size() > 0){
      //   std::cout << "\n" << std::endl;
      //   std::cout << "Event: "<< i << "/" << nEntries<< std::endl;
      // }

      bool hasPiMinus_Primary = false;
      bool hasPi0 = false;
      bool hasGamma0_Decay = false;
      bool hasGamma1_Decay = false;

      IHandle<IG4Trajectory> track_piMinusPrimary(nullptr);
      IHandle<IG4Trajectory> track_pi0(nullptr);
      IHandle<IG4Trajectory> track_gamma0(nullptr);
      IHandle<IG4Trajectory> track_gamma1(nullptr);
      IHandle<IG4Trajectory> track_electron0(nullptr);
      IHandle<IG4Trajectory> track_positron0(nullptr);
      IHandle<IG4Trajectory> track_electron1(nullptr);
      IHandle<IG4Trajectory> track_positron1(nullptr);

      IHandle<IG4Trajectory> track_gamma_lead(nullptr);
      IHandle<IG4Trajectory> track_gamma_sublead(nullptr);
      IHandle<IG4Trajectory> track_gamma_lead_electron(nullptr);
      IHandle<IG4Trajectory> track_gamma_lead_positron(nullptr);
      IHandle<IG4Trajectory> track_gamma_sublead_electron(nullptr);
      IHandle<IG4Trajectory> track_gamma_sublead_positron(nullptr);

      for (auto& trackMap: *g4Tracks)
      {
        //
        //
        //
        TString thisTrack_partName;
        TString thisTrack_procName;
        IHandle<IG4Trajectory> thisTrack = g4Tracks->GetTrajectory(trackMap.second.GetTrackId());
        int thisTrack_id = thisTrack->GetTrackId();
        thisTrack_partName = TString(thisTrack->GetParticleName());
        if(!(thisTrack_partName.Contains("pi") || thisTrack_partName.Contains("gamma") || thisTrack_partName.Contains("e-") || thisTrack_partName.Contains("e+"))) continue;
        thisTrack_procName = TString(thisTrack->GetProcessName());
        
        //
        //
        //
        IHandle<IG4Trajectory> parentTrack = g4Tracks->GetTrajectory(thisTrack->GetParentId());
        TString parentTrack_partName;
        TString parentTrack_procName;
        if (parentTrack){
          parentTrack_partName = TString(parentTrack->GetParticleName());
          parentTrack_procName = TString(parentTrack->GetProcessName());
        }
        //
        //
        //
        IHandle<IG4Trajectory> grandParentTrack(nullptr);
        if (parentTrack){
          grandParentTrack = g4Tracks->GetTrajectory(parentTrack->GetParentId());
        }
        TString grandParentTrack_partName; 
        TString grandParentTrack_procName;
        if (grandParentTrack){
          grandParentTrack_partName = TString(grandParentTrack->GetParticleName());
          grandParentTrack_procName = TString(grandParentTrack->GetProcessName());
        }
        //
        //
        //
        if (thisTrack_partName.Contains("pi-") && thisTrack_procName.Contains("primary")){ 
          hasPiMinus_Primary = true;
          track_piMinusPrimary = thisTrack;
        }
        //
        //
        //
        if(thisTrack_partName.Contains("pi0") && (thisTrack_procName.Contains("pi-Inelastic") || thisTrack_procName.Contains("hBertiniCaptureAtRest"))){
          hasPi0 = true;
          track_pi0 = thisTrack;
        }
        //
        //
        //
        if (thisTrack_partName.Contains("gamma") && thisTrack_procName.Contains("Decay") && parentTrack_partName.Contains("pi0")){
          if(track_gamma0 == nullptr) track_gamma0 = thisTrack;
          else if(track_gamma1 == nullptr) track_gamma1 = thisTrack;
        }
        //
        //
        //
        if (parentTrack_partName.Contains("gamma") && parentTrack_procName.Contains("Decay") && grandParentTrack_partName.Contains("pi0")){
          if (thisTrack_partName.Contains("e-")){
            if(track_electron0 == nullptr) track_electron0 = thisTrack;
            else if(track_electron1 == nullptr) track_electron1 = thisTrack;
          }
          if (thisTrack_partName.Contains("e+")){
            if(track_positron0 == nullptr) track_positron0 = thisTrack;
            else if(track_positron1 == nullptr) track_positron1 = thisTrack;
          }
        }
      }

      //========================================
      //
      // Sort the gammas by energy
      //
      //========================================
      if (track_gamma0 && !track_gamma1){
        track_gamma_lead = track_gamma0;
      } 
      else if (track_gamma0 && track_gamma1){
        if (track_gamma0->GetInitialMomentum().E() > track_gamma1->GetInitialMomentum().E()){
          track_gamma_lead = track_gamma0;
          track_gamma_sublead = track_gamma1;
        } 
        else{
          track_gamma_lead = track_gamma1;
          track_gamma_sublead = track_gamma0;
        }
      }
      //========================================
      //
      // Sort the e+ e- to the right gammas
      //
      //========================================
      int track_gamma_lead_id = -1;
      int track_gamma_sublead_id = -1;

      if (track_gamma_lead){
        track_gamma_lead_id = track_gamma_lead->GetTrackId();
        if (track_electron0){ 
          if (track_electron0->GetParentId() == track_gamma_lead_id){
            track_gamma_lead_electron = track_electron0;
          }
        }
        if (track_positron0){
          if (track_positron0->GetParentId() == track_gamma_lead_id){
            track_gamma_lead_positron = track_positron0;
          }
        }
        if (track_electron1){ 
          if (track_electron1->GetParentId() == track_gamma_lead_id){
            track_gamma_lead_electron = track_electron1;
          }
        }
        if (track_positron1){
          if (track_positron1->GetParentId() == track_gamma_lead_id){
            track_gamma_lead_positron = track_positron1;
          }
        }
      }

      if (track_gamma_sublead){
        track_gamma_sublead_id = track_gamma_sublead->GetTrackId();
        if (track_electron0){ 
          if (track_electron0->GetParentId() == track_gamma_sublead_id){
            track_gamma_sublead_electron = track_electron0;
          }
        }
        if (track_positron0){
          if (track_positron0->GetParentId() == track_gamma_sublead_id){
            track_gamma_sublead_positron = track_positron0;
          }
        }
        if (track_electron1){ 
          if (track_electron1->GetParentId() == track_gamma_sublead_id){
            track_gamma_lead_electron = track_electron1;
          }
        }
        if (track_positron1){
          if (track_positron1->GetParentId() == track_gamma_sublead_id){
            track_gamma_lead_positron = track_positron1;
          }
        }
      }
      //
      //
      //
      if (hasPiMinus_Primary)
      { 
        // cout << "\n" <<endl;
        // cout << i << "/" << nEntries << endl;
        h_cutflow->Fill("PrimaryPionMinus",1);
        h_piPrimary_e->Fill(track_piMinusPrimary->GetInitialMomentum().E() / unit::MeV, 1);
        h_piPrimary_mom->Fill(track_piMinusPrimary->GetInitialMomentum().P() / unit::MeV,1);
        // cout << "\n" <<endl;
        std::string volumeName = track_piMinusPrimary->GetTrajectoryPoints().back().GetVolumeName();

        if(TString(volumeName).Contains("TargetDisk")) {
          TLorentzVector tlv_piPrimary_finalPos = track_piMinusPrimary->GetFinalPosition();
          h2_piPrimaryStopped_yz->Fill(tlv_piPrimary_finalPos.Z()-7650., tlv_piPrimary_finalPos.Y(),1);
          h2_piPrimaryStopped_yx->Fill(tlv_piPrimary_finalPos.X()-6400., tlv_piPrimary_finalPos.Y(),1);
          h_cutflow->Fill("StoppedPionMinus",1);
        } 

        // if(TString(volumeName).Contains("TargetDisk")) {
        //   cout << "\n\n" << endl;
        //   cout << volumeName <<endl;
        //   // event->ls("dump");
        //   event->ls();
        // }

        //
        //
        //  
        if(hasPi0){
          h_cutflow->Fill("Pion0",1);
          h_pi0_e->Fill(track_pi0->GetInitialMomentum().E() / unit::MeV, 1);
          h_pi0_mom->Fill(track_pi0->GetInitialMomentum().P() / unit::MeV, 1);
          //
          //
          //
          if (track_gamma0 && !track_gamma1){
            h_cutflow->Fill("OneGamma",1);
            h_onegamma_e->Fill(track_gamma0->GetInitialMomentum().E() / unit::MeV,1);
            if (track_gamma_lead_electron) {
              h_cutflow->Fill("OneGamma_HasElectron",1);
              h_onegamma_electron_e->Fill(track_gamma_lead_electron->GetInitialMomentum().E() / unit::MeV,1);
              h_onegamma_electron_mom->Fill(track_gamma_lead_electron->GetInitialMomentum().P() / unit::MeV,1);
            }
            if (track_gamma_lead_positron) {
              h_cutflow->Fill("OneGamma_HasPositron",1);
              h_onegamma_positron_e->Fill(track_gamma_lead_positron->GetInitialMomentum().E() / unit::MeV,1);
              h_onegamma_positron_mom->Fill(track_gamma_lead_positron->GetInitialMomentum().P() / unit::MeV,1);
            }
          }
          else if (track_gamma0 && track_gamma1) {
            h_cutflow->Fill("TwoGamma",1);

            h_twogamma_lead_e->Fill(track_gamma0->GetInitialMomentum().E() / unit::MeV,1);
            h_twogamma_sublead_e->Fill(track_gamma1->GetInitialMomentum().E() / unit::MeV,1);


            if (track_gamma_lead_electron) {
              h_cutflow->Fill("TwoGammaLead_HasElectron",1);
              h_twogamma_lead_electron_e->Fill(track_gamma_lead_electron->GetInitialMomentum().E() / unit::MeV,1);
              h_twogamma_lead_electron_mom->Fill(track_gamma_lead_electron->GetInitialMomentum().P() / unit::MeV,1);
            }
            if (track_gamma_lead_positron) {
              h_cutflow->Fill("TwoGammaLead_HasPositron",1);
              h_twogamma_lead_positron_e->Fill(track_gamma_lead_positron->GetInitialMomentum().E() / unit::MeV,1);
              h_twogamma_lead_positron_mom->Fill(track_gamma_lead_positron->GetInitialMomentum().P() / unit::MeV,1);
            }
            if (track_gamma_sublead_electron){
              h_cutflow->Fill("TwoGammaSubLead_HasElectron",1);
              h_twogamma_sublead_electron_e->Fill(track_gamma_sublead_electron->GetInitialMomentum().E() / unit::MeV,1);
              h_twogamma_sublead_electron_mom->Fill(track_gamma_sublead_electron->GetInitialMomentum().P() / unit::MeV,1);
            }
            if (track_gamma_sublead_positron){
              h_cutflow->Fill("TwoGammaSubLead_HasPositron",1);
              h_twogamma_sublead_positron_e->Fill(track_gamma_sublead_positron->GetInitialMomentum().E() / unit::MeV,1);
              h_twogamma_sublead_positron_mom->Fill(track_gamma_sublead_positron->GetInitialMomentum().P() / unit::MeV,1);
            }

            bool firstPass = true;
  
            TVector3 gamma_pos_local;
            if(track_gamma0){
              COMET::IGeomInfo::DetectorSolenoid().GetDetPositionInDSCoordinate(track_gamma0->GetFinalPosition().Vect(), gamma_pos_local);
              h_gamma_decayvtx_r->Fill(gamma_pos_local.Perp(),1);
              h_gamma_decayvtx_z->Fill(gamma_pos_local.Z(),1);
              h2_gamma_decayvtx_rz->Fill(gamma_pos_local.Z(),gamma_pos_local.Perp(),1);
              h2_gamma_decayvtx_rz_v2->Fill(gamma_pos_local.Z(),gamma_pos_local.Perp(),1);
              h2_gamma_decayvtx_rz_v3->Fill(gamma_pos_local.Z(),gamma_pos_local.Perp(),1);
              h2_gamma_decayvtx_yx->Fill(gamma_pos_local.X(),gamma_pos_local.Y(),1);
              h2_gamma_decayvtx_xz->Fill(gamma_pos_local.Z(),gamma_pos_local.X(),1);
              h2_gamma_decayvtx_yz->Fill(gamma_pos_local.Z(),gamma_pos_local.Y(),1);
              h3_gamma_decayvtx_xyz->Fill(gamma_pos_local.X(),gamma_pos_local.Y(),gamma_pos_local.Z(),1);
              // if (gamma_pos_local.Perp() > 340. && gamma_pos_local.Perp() < 380.){
              //   if ((gamma_pos_local.Z() > 400. && gamma_pos_local.Z() < 1000.)||(gamma_pos_local.Z() < -400. && gamma_pos_local.Z() > -1000.)){
              //     cout << "\n\n" << endl; firstPass = false;
              //     cout << track_gamma0->GetTrajectoryPoints().back().GetVolumeName() << endl; 
              //   }
              // } 
            }
            if(track_gamma1){
              COMET::IGeomInfo::DetectorSolenoid().GetDetPositionInDSCoordinate(track_gamma1->GetFinalPosition().Vect(), gamma_pos_local);
              h_gamma_decayvtx_r->Fill(gamma_pos_local.Perp(),1);
              h_gamma_decayvtx_z->Fill(gamma_pos_local.Z(),1);
              h2_gamma_decayvtx_rz->Fill(gamma_pos_local.Z(),gamma_pos_local.Perp(),1);
              h2_gamma_decayvtx_rz_v2->Fill(gamma_pos_local.Z(),gamma_pos_local.Perp(),1);
              h2_gamma_decayvtx_rz_v3->Fill(gamma_pos_local.Z(),gamma_pos_local.Perp(),1);
              h2_gamma_decayvtx_yx->Fill(gamma_pos_local.X(),gamma_pos_local.Y(),1);
              h2_gamma_decayvtx_xz->Fill(gamma_pos_local.Z(),gamma_pos_local.X(),1);
              h2_gamma_decayvtx_yz->Fill(gamma_pos_local.Z(),gamma_pos_local.Y(),1);
              h3_gamma_decayvtx_xyz->Fill(gamma_pos_local.X(),gamma_pos_local.Y(),gamma_pos_local.Z(),1);

              // if (gamma_pos_local.Perp() > 340. && gamma_pos_local.Perp() < 380.){
              //   if ((gamma_pos_local.Z() > 400. && gamma_pos_local.Z() < 1000.)||(gamma_pos_local.Z() < -400. && gamma_pos_local.Z() > -1000.)){
              //     if (firstPass) cout << "\n\n" << endl;
              //     cout << track_gamma1->GetTrajectoryPoints().back().GetVolumeName() << endl; 
              //   }
              // }              
            }

            // Get the final trajectory momentum.
            // TLorentzVector tlv_gamma0 = track_gamma0.GetFinalPosition();
            // TVector3 finalPos_cm = traj_pos.Vect()*(1/unit::cm); // req. in cm for gGeoManager!
            // TGeoNode* volume = gGeoManager->FindNode(finalPos_cm.X(),finalPos_cm.Y(),finalPos_cm.Z());
            // std::string volumeName = volume->GetName();
            // std::cout << volumeName std::endl;

            // std::cout << "New Event" << std::endl; 
            // std::cout << track_gamma0->GetTrajectoryPoints().front().GetVolumeName() << "|" << track_gamma0->GetTrajectoryPoints().back().GetVolumeName() << std::endl;
            // std::cout << track_gamma1->GetTrajectoryPoints().front().GetVolumeName() << "|" << track_gamma1->GetTrajectoryPoints().back().GetVolumeName() << std::endl;
          }
          //
          //
          //
          bool hasLeadPair    = track_gamma_lead_electron    && track_gamma_lead_positron;
          bool hasSubLeadPair = track_gamma_sublead_electron && track_gamma_sublead_positron;
          if(hasLeadPair || hasSubLeadPair){
            h_cutflow->Fill("AtLeastOneElectronPositronPair",1);
          }
          if((hasLeadPair && !hasSubLeadPair)||(!hasLeadPair && hasSubLeadPair)){
            h_cutflow->Fill("OneElectronPositronPair",1);
          }
          if(hasLeadPair && hasSubLeadPair){
            h_cutflow->Fill("TwoElectronPositronPair",1);
          }
        }
      }
    }
  }
  cout << "End of event loop" << endl; 
  

  TFile* outFile = new TFile(outFileName,"RECREATE");
  outFile->cd();
  h_cutflow->Write();

  h_piPrimary_e->Write();
  h_piPrimary_mom->Write();

  h2_piPrimaryStopped_yz->Write();
  h2_piPrimaryStopped_yx->Write();

  h_pi0_e->Write();
  h_pi0_mom->Write();

  h_onegamma_e->Write();
  h_twogamma_lead_e->Write();
  h_twogamma_sublead_e->Write();

  h_onegamma_electron_e->Write();
  h_onegamma_electron_mom->Write();
  h_onegamma_positron_e->Write();
  h_onegamma_positron_mom->Write();

  h_twogamma_lead_electron_e->Write();
  h_twogamma_lead_electron_mom->Write();
  h_twogamma_lead_positron_e->Write();
  h_twogamma_lead_positron_mom->Write();

  h_twogamma_sublead_electron_e->Write();
  h_twogamma_sublead_electron_mom->Write();
  h_twogamma_sublead_positron_e->Write();
  h_twogamma_sublead_positron_mom->Write();

  h_gamma_decayvtx_r->Write();
  h_gamma_decayvtx_z->Write();

  h2_gamma_decayvtx_yx->Write();
  h2_gamma_decayvtx_xz->Write();
  h2_gamma_decayvtx_yz->Write();
  h2_gamma_decayvtx_rz->Write();
  h2_gamma_decayvtx_rz_v2->Write();
  h2_gamma_decayvtx_rz_v3->Write();

  h3_gamma_decayvtx_xyz->Write();

  outFile->Close();

  inFile->Close();
  timer->Stop();
  timer->Print();

}
