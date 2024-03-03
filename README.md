# Introduction

![]()

The Standard Model (SM) of particle physics is excellent theory that explain the basic building blocks of the universe. It explains how the quarks and leptons build all known matter. In addition, it describes how three of four known fundamental forces (electromagnetic force, strong force and weak force and except for gravity) work by exchange of force-carrier particles known as boson. The biggest success of the SM is the prediction of Higgs boson which then experimentally observed at Large Hadron Collider in 2012. The Higgs boson is the last particle predicted in SM meaning there is no other particle is predicted by SM in the future. For a decade, through many experiment the SM become establish as a well-tested physics theory. However, the SM still far be considered as a complete model since it unable to solve some problems in particle physics such as hierarchy problem between the Planck scale of gravity and electroweak scale, the quantization of gravity, fine tuning of certain SM parameter and more. Other than that, SM also unable to predict some physical phenomena in particle physics such as neutrino oscillation which resulting in Lepton Flavor Violation (LFV) that can induce Charged
Lepton Flavor Violation (CLFV).

![]()

The existence of a more complete theoretical models than the SM known as New Physics (NP) that may explain and predict some physical phenomena such as neutrino oscillation and CLFV. Originally, CLFV is not allowed in SM, however, with existance of neutrino oscillation, CLFV may occur but in extremely low probability or branching ratio which is around order of -54. Therefore, searching for CLFV process signal may give us a hint of the physics beyond the SM and some NP models may be considered as extension of the SM. The CLFV process in muonic channel have been search since the discovery of muon and still continue until now. The COMET experiment is the one of the future experiment that seek for CLFV process in muonic channel of neutrino-less muon to electron conversion. Due to the rarity of CLFV process to occur, the COMET must be designed to suppressed all the possible background to get accurate data. The accuracy of the data can be increase by calibrating the detector before taking the data, this can help to reduce the uncertainty by reducing the error that may come from various source such as detector error. The objective of this study is to study pion capture process for the momentum calibration by observing the detectability of pion capture process in the detector in COMET experiment. It is crucial to check the detectability of the interest process to know if this process is possible to be used for calibration. If pion capture process is detectable, the study will continue to the calibration measurement. In addition, the study also need to estimate and analyse the pion capture process for the calibration run.

# Objective

Objective of momentum Calibration study:
1. Calibrate the well-known process in the Cylindrical Drift Chamber (CDC) in Cylindrical Detector System (CyDet).
   
The requirement of suitable process:
1. Well-known and trusted theoretical value.
2. Reconstructible process in the COMET experiment.

# Methodology

The momentum calibration study used Pionic Pion Capture process for calibration. The momentum of final product of this process which are of electron and positron will be used for calibration.

## ICEDUST Software

The word ICEDUST is stand for Integrated COMET Experiment Data User Software Toolkit which is the COMET experiment’s official software framework. The ICEDUST has been used to handle and analyse the COMET data. In addition, it has been designed to treat the real data and simulated data in the same way by using the exact same software algorithm. The MIDAS file format where the real data is stored will be converted using the oaRawData and oaUnpack packages to create the data structures mimicked by SimDetectorResponse. Then, both real data and simulation data are calibrated, reconstructed, and analysed. The oaEvent package provide the core event structure of ICEDUST, which means that the data flow in ICEDUST is built around the oaEvent data format. The data stored in the oaEvent format are created by a hierarchical structure of objects from the TNamed class of ROOT. The geometry description is stored with the data, it can be in the form of a hash-tag pointing to a particular archived geometry that is automatically retrieved as needed or as a persisted ROOT object. The various TGeo classes is used by ROOT format that implement all geometry needs which means that all packages throughout the framework use a usual geometry description including providing an easy book-keeping mechanism.

![]()

In the ICEDUST framework, there is a host of simulation packages known as Monte Carlo packages that have been incorporated into ICEDUST. These include PHITS, MARS, Fluka and Geant4 which handle the simulations of hadronic physics inside the Pion Production Target. The usual simulation chain that produce Monte Carlo data can be done by simple step. Firstly, simulate the production target. This can be done apart so that the package of different hadron production models can be used. Secondly, the particle tracking. The details of the resulting particles flux out of the pion Production Target are read into a data format which is defined by oaRooTracker package. The Geant4 plays important role here, where the SimG4 package which is the Geant4-based particle tracking will read the data and track the particles from the Pion Production Target to the detectors and creates simulated energy deposits. Then, data from many events was combined into one event by using the SimHitMerger. Finally, The Rare process selection. To study the rare process or background signal since they are rare, the SimHitMerger is used to merge hits from rare process together to artificially increase the statistics.


## The COMET Simulation

The simulation begins with the propagation of 8 GeV protons beam which produce proton through proton beam line that feeds COMET experiment by using the TURTLE software framework. The results of this simulation are sampled just as the protons enter the Pion Production section and saved in an oaRooTracker file.This simulation has been done by the collaboration. For calibration study, the Geant 4 based simulation is run where the oaRooTracker file is used as input for the simulation. The SimG4 read the description from the oaRooTracker files to continue the simulation. The simulation is done in full by Geant4 through the Muon Transport section and into the detector section. The hits produced in SimG4 describe the time and magnitude of all energy deposits in the detectors. They are referred to as "truth" hits.

![]()

The individual Proton On Target (POT) events from SimG4 simulation is combines by using SimHitMerger package to form bunch-like timing structure. The bunch-like events are created by shifting the timing of each of the 1.6 × 107 POT events in the bunch by random value in range from -50 ns to 50 ns and combining the results. The pulsed beam is simulated using a handful of bunch-events, where each is separated by 1170 ns to form "bunch-train" events. The steps of ICEDUST simulation. Starting the simulation from the beginning is very time consuming. Due to this reason, the initial step in calibration study is to find a way to minimize the simulation duration. This can be done by skimming the negative charge pion which is the parent particle form PPC process.

## Momentum Calibration Study Work Flow

![]()

The work flow in this study is to skim the pion to produce input of the simulation,
running the simulation for current configuration. After that the simulation is rerun by
modifying the configuration of the experiment. The output data is then visualized from
extracted data from each simulation output.

## Algorithm 

The interest process in the calibration study is pion capture process specifically Pionic Pion Capture (PPC). Realistically, some of the pion that does not decay to muon in transport solenoid will enter the CyDet. This pion will be captured by the nucleus in the stopping target. The captured pion will interact with the proton from the nucleus. This interaction will produce pion neutral and neutron. The pion neutron will later decay into two photons and these photons produce electron-positron pair. Finally, using the electron-positron pair momentum distribution for the calibration. 

![]()

### Data Samples

#### ICEDUST Setup

The work is start from building ICEDUST on the DICC HPC Cluster or known as UMHPC server. The installation and simulation is using the Linux Operating System. The Ubuntu software is installed and used to building ICEDUST as well as to run the simulation the COMET experiment. The installation of ICEDUST can be done in either interactive mode or batch mode. ICEDUST require a lot of space, by using interactive mode to building the ICEDUST is very time consuming. Therefore, Batch mode was used by sending batch script to SLURM of the DICC HPC cluster. The ICEDUST Software was setup using the following this [command](https://github.com/dimashidayat99/Momemtum_Calibration-COMET/blob/main/Instructions/UMHPC_ICEDUST_Setup.md) for UMHPC server and this [command](https://github.com/dimashidayat99/Momemtum_Calibration-COMET/blob/main/Instructions/Deprecated/DICC_COMET_Setup.md) for DICC server.


#### Pion Skimming

The Geant4 based simulation read the oaRooTracker as input to continue the simulation and this simulation will give five output files which are log file, mac file, root file, dat file and rootracker file. The output files that is important in this study is root file and rootracker file, while the rest of files is not being used in this study. The oaRootracker files is classify into two types which are MC5A01 and MC5A02. The MC5A01 and MC5A02 is just oaRooTracker that contain particles before entering CyDet and after entering CyDet, respectively. This study is to used MC5A01 oaRooTracker to run the simulation. Since there are a lot of oaRooTracker files from MC5A01, the 100 oaRooTracker files was merge into 1 merged oaRooTracker file and there are total of 200 merged oaRooTracker files. The combination of oaRooTracker code can be seen in the `CyDetMomCalib
/MakeRooTrackHist/` [directory](https://github.com/dimashidayat99/Momemtum_Calibration-COMET/tree/main/CyDetMomCalib/MakeRooTrackHist). Running the simulation with 200 merged oaRooTracker will be very time consuming. To run 1 unmerged oaRooTracker usually take about 1 days to complete. The long duration of the simulation is because of the simulation will run for all particles contain in the oaRooTracker. Due to the simulation is very time consuming, the duration of the simulation is reduced by removing all non related particle that is not important in this study. Since the PPC process is the interests process in this study, the pion (negative charge pion) is the only important parent particle. Therefore, every oaRooTracker will be filtered or skimmed to remove all the particles except for pion. The code for performing this skim can be found in `CyDetMomCalib/AnaRootracker` [directory](https://github.com/dimashidayat99/Momemtum_Calibration-COMET/tree/main/CyDetMomCalib/AnaRootracker). Using this method, simulation was made to be more efficient. Now, there are total of 200 skimmed pion oaRooTracker that will be used as input in the simulation. The simulation was run using 200 skimmed pion oaRooTracker as input by using the original (current) configuration of the COMET experiment.

### Modifying the Experiment Configuration

In the Geant4 based simulation, the user can modify the configuration of the COMET experiment in the simulation by changing the macro of ICEDUST package. Changing the configuration can be done by creating custom configuration file which can used to configure the parameter and initial setting of the simulation or programs. In other words, the configuration files is a file that is used to specify anything that is needed by the user to run the simulation based on the study needs. The code of performing the modification of experiment configuration can be found in the `CyDetMomCalib/SimG4CyDet/MuonCapTarget` [directory](https://github.com/dimashidayat99/Momemtum_Calibration-COMET/tree/main/CyDetMomCalib/SimG4CyDet/MuonCapTarget).

#### Hydrocarbon Material Target Configuration

The default configuration of material target (muon stopping target) in COMET experiment is Aluminium. The muon stopping target material of Aluminium need to be change to hydrocarbon based material. Consequently, the muon stopping target is changed by modifying the configuration of the simulation in the COMET experiment simulation. There are 4 additional configuration of hydrocarbon material target is created which are [polyethylene](https://github.com/dimashidayat99/Momemtum_Calibration-COMET/blob/main/CyDetMomCalib/SimG4CyDet/MuonCapTarget/config/rootrackerMC5A01_skimPiMinus_polyethylene.cfg), [polypropylene](https://github.com/dimashidayat99/Momemtum_Calibration-COMET/blob/main/CyDetMomCalib/SimG4CyDet/MuonCapTarget/config/rootrackerMC5A01_skimPiMinus_polypropylene.cfg), [polystyrene](https://github.com/dimashidayat99/Momemtum_Calibration-COMET/blob/main/CyDetMomCalib/SimG4CyDet/MuonCapTarget/config/rootrackerMC5A01_skimPiMinus_polystyrene.cfg) and [polyvinyl toluene](https://github.com/dimashidayat99/Momemtum_Calibration-COMET/blob/main/CyDetMomCalib/SimG4CyDet/MuonCapTarget/config/rootrackerMC5A01_skimPiMinus_polyvinyltoluene.cfg) as muon stopping target. The simulation was run for 4 different configuration of hydrocarbon target by using 200 skimmed pion oaRooTracker as input for each configuration.

#### Pion Particle Gun Configuration

The project utilized pion particle gun configuration. In principle, the particle gun will fire the pion directly to the material target in the CDC. Using pion gun configuration, the input samples is inessential in the simulation because the pion gun is actually act as input samples. The simulation was run using pion gun configuration along with the default configuration and polyethylene configuration.

### Event Reconstruction and Track Finding

The simulation of this study is based on the PPC process flow as discussed before. The idea is to find the electron and positron pair parameters (e.g. number of events, momentum, energy) without event selection criteria for the parameters. The track of all particle (pion, photon, electron and positron) involve in PPC process will find by finding the trajectory of each particle involve in PPC process in CyDet. The event reconstruction is done when the trajectory of pion, photon, electron and positron was found. This reconstruction of event will provide the information about their (pion, photon, electron and positrons) parents particle. Using the track finding and event reconstruction, the main algorithm was created based on the pair production process, pion neutral decay process, and proton-pion interaction process from the PPC process. The code of performing the event reconstruction and track finding can be found in `CyDetMomCalib/AnaOAEvent/` [directory](https://github.com/dimashidayat99/Momemtum_Calibration-COMET/tree/main/CyDetMomCalib/AnaOAEvent) where the main event reconstruction and track finding code is named as `Ananlyzer.C` which filter out all the event and focus only desired event in this study which is PPC.

# Result




