# Introduction
<p align="middle">
<img src="https://github.com/dimashidayat99/Momemtum_Calibration-COMET/blob/main/image/sm.png"  width="800" />
</p>
<p align="middle">
    <em>Standard model of particle physics.</em>
    <a href="https://www.google.com/imgres?imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2F0%2F00%2FStandard_Model_of_Elementary_Particles.svg&tbnid=P8QhfKkjydp_QM&vet=12ahUKEwjCjfbSuNqEAxXMUGwGHZSnAkMQMygAegQIARBK..i&imgrefurl=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FStandard_Model&docid=7RVBQ4xyx2vmTM&w=1390&h=1330&itg=1&q=standard%20model&ved=2ahUKEwjCjfbSuNqEAxXMUGwGHZSnAkMQMygAegQIARBK">Figure source.</a>
</p>

The Standard Model (SM) of particle physics is excellent theory that explain the basic building blocks of the universe. It explains how the quarks and leptons build all known matter. In addition, it describes how three of four known fundamental forces (electromagnetic force, strong force and weak force and except for gravity) work by exchange of force-carrier particles known as boson. The biggest success of the SM is the prediction of Higgs boson which then experimentally observed at Large Hadron Collider in 2012. The Higgs boson is the last particle predicted in SM meaning there is no other particle is predicted by SM in the future. For a decade, through many experiment the SM become establish as a well-tested physics theory. However, the SM still far be considered as a complete model since it unable to solve some problems in particle physics such as hierarchy problem between the Planck scale of gravity and electroweak scale, the quantization of gravity, fine tuning of certain SM parameter and more. Other than that, SM also unable to predict some physical phenomena in particle physics such as neutrino oscillation which resulting in Lepton Flavor Violation (LFV) that can induce Charged
Lepton Flavor Violation (CLFV) process which is shown in figure below.

<p align="middle">
<img src="https://github.com/dimashidayat99/Momemtum_Calibration-COMET/blob/main/image/CLFVprocess.jpg"  width="800"/>
</p>
<p align="middle">
<em>CLFV Process.</em>
<a href = "https://www.semanticscholar.org/paper/Lepton-Flavour-Violation-Experiments-Cei-Nicol%C3%B3/7285364ec2e82b7b8c1275cd967f931807f1f1af/figure/0">Figure source. </a>
</p>

The existence of a more complete theoretical models than the SM known as New Physics (NP) that may explain and predict some physical phenomena such as neutrino oscillation and CLFV. Originally, CLFV is not allowed in SM, however, with existance of neutrino oscillation, CLFV may occur but in extremely low probability or branching ratio which is around order of -54. Therefore, searching for CLFV process signal may give us a hint of the physics beyond the SM and some NP models may be considered as extension of the SM. The CLFV process in muonic channel have been search since the discovery of muon and still continue until now. 

<p align="middle">
<img src="https://github.com/dimashidayat99/Momemtum_Calibration-COMET/blob/main/image/comet_layout.png" width ="800" /> 
</p>
<p align="middle">
    <em>The COMET experiment schematic layout.</em>
<a href = "https://doi.org/10.1093/ptep/pts089">Figure source.</a>
</p>

The COMET experiment is the one of the future experiment that seek for CLFV process in muonic channel of neutrino-less muon to electron conversion. Due to the rarity of CLFV process to occur, the COMET must be designed to suppressed all the possible background to get accurate data. The accuracy of the data can be increase by calibrating the detector before taking the data, this can help to reduce the uncertainty by reducing the error that may come from various source such as detector error. The objective of this study is to study pion capture process for the momentum calibration by observing the detectability of pion capture process in the detector in COMET experiment. It is crucial to check the detectability of the interest process to know if this process is possible to be used for calibration. If pion capture process is detectable, the study will continue to the calibration measurement. In addition, the study also need to estimate and analyse the pion capture process for the calibration run.


# Objective

Objective of momentum Calibration study:
1. Calibrate the well-known process in the Cylindrical Drift Chamber (CDC) in Cylindrical Detector System (CyDet).
   
The requirement of suitable process:
1. Well-known and trusted theoretical value.
2. Reconstructible process in the COMET experiment.

# Methodology

The momentum calibration study used Pionic Pion Capture process for calibration. The momentum of final product of this process which are of electron and positron will be used for calibration.

## ICEDUST Software

The word ICEDUST is stand for Integrated COMET Experiment Data User Software Toolkit which is the COMET experiment’s official software framework. The ICEDUST has been used to handle and analyse the COMET data. In addition, it has been designed to treat the real data and simulated data in the same way by using the exact same software algorithm. The MIDAS file format where the real data is stored will be converted using the oaRawData and oaUnpack packages to create the data structures mimicked by SimDetectorResponse. Then, both real data and simulation data are calibrated, reconstructed, and analysed. The oaEvent package provide the core event structure of ICEDUST, which means that the data flow in ICEDUST is built around the oaEvent data format. The data stored in the oaEvent format are created by a hierarchical structure of objects from the TNamed class of ROOT. The geometry description is stored with the data, it can be in the form of a hash-tag pointing to a particular archived geometry that is automatically retrieved as needed or as a persisted ROOT object. The various TGeo classes is used by ROOT format that implement all geometry needs which means that all packages throughout the framework use a usual geometry description including providing an easy book-keeping mechanism.

<p align="middle">
<img src="https://github.com/dimashidayat99/Momemtum_Calibration-COMET/blob/main/image/ICEDUST%20Framework.png"  width="800"/>
</p>
<p align="middle">
<em>ICEDUST software framework.</em>
<a href = "http://hdl.handle.net/10044/1/45365">Figure source. </a>
</p>

In the ICEDUST framework, there is a host of simulation packages known as Monte Carlo packages that have been incorporated into ICEDUST. These include PHITS, MARS, Fluka and Geant4 which handle the simulations of hadronic physics inside the Pion Production Target. The usual simulation chain that produce Monte Carlo data can be done by simple step. Firstly, simulate the production target. This can be done apart so that the package of different hadron production models can be used. Secondly, the particle tracking. The details of the resulting particles flux out of the pion Production Target are read into a data format which is defined by oaRooTracker package. The Geant4 plays important role here, where the SimG4 package which is the Geant4-based particle tracking will read the data and track the particles from the Pion Production Target to the detectors and creates simulated energy deposits. Then, data from many events was combined into one event by using the SimHitMerger. Finally, The Rare process selection. To study the rare process or background signal since they are rare, the SimHitMerger is used to merge hits from rare process together to artificially increase the statistics.


## The COMET Simulation

The simulation begins with the propagation of 8 GeV protons beam which produce proton through proton beam line that feeds COMET experiment by using the TURTLE software framework. The results of this simulation are sampled just as the protons enter the Pion Production section and saved in an oaRooTracker file.This simulation has been done by the collaboration. For calibration study, the Geant 4 based simulation is run where the oaRooTracker file is used as input for the simulation. The SimG4 read the description from the oaRooTracker files to continue the simulation. The simulation is done in full by Geant4 through the Muon Transport section and into the detector section. The hits produced in SimG4 describe the time and magnitude of all energy deposits in the detectors. They are referred to as "truth" hits.

<p align="middle">
<img src="https://github.com/dimashidayat99/Momemtum_Calibration-COMET/blob/main/image/comet_simulation.png"  width="500"/>
</p>
<p align="middle">
<em>Overview of the COMET experiment simulation.</em>
<a href = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.mdpi.com%2F2218-1997%2F8%2F4%2F196&psig=AOvVaw242Qk7AtjGSU93NqTUIJ3Y&ust=1709638846393000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCNjAwZLD2oQDFQAAAAAdAAAAABAF">Figure source. </a>
</p>

The individual Proton On Target (POT) events from SimG4 simulation is combines by using SimHitMerger package to form bunch-like timing structure. The bunch-like events are created by shifting the timing of each of the 1.6 × 107 POT events in the bunch by random value in range from -50 ns to 50 ns and combining the results. The pulsed beam is simulated using a handful of bunch-events, where each is separated by 1170 ns to form "bunch-train" events. The steps of ICEDUST simulation. Starting the simulation from the beginning is very time consuming. Due to this reason, the initial step in calibration study is to find a way to minimize the simulation duration. This can be done by skimming the negative charge pion which is the parent particle form PPC process.

## Momentum Calibration Study Work Flow

![](https://github.com/dimashidayat99/Momemtum_Calibration-COMET/blob/main/image/WorkFlow.png)

The work flow in this study is to skim the pion to produce input of the simulation,
running the simulation for current configuration. After that the simulation is rerun by
modifying the configuration of the experiment. The output data is then visualized from
extracted data from each simulation output.

## Algorithm 

The interest process in the calibration study is pion capture process specifically Pionic Pion Capture (PPC). Realistically, some of the pion that does not decay to muon in transport solenoid will enter the CyDet. This pion will be captured by the nucleus in the stopping target. The captured pion will interact with the proton from the nucleus. This interaction will produce pion neutral and neutron. The pion neutron will later decay into two photons and these photons produce electron-positron pair. Finally, using the electron-positron pair momentum distribution for the calibration. 

<p align="middle">
<img src="https://github.com/dimashidayat99/Momemtum_Calibration-COMET/blob/main/image/ppc.png"  width="500"/>
</p>
<p align="middle">
    <em>Pionic pion capture process.</em>
</p>

### Data Samples

#### ICEDUST Setup

The work is start from building ICEDUST on the DICC HPC Cluster or known as UMHPC server. The installation and simulation is using the Linux Operating System. The Ubuntu software is installed and used to building ICEDUST as well as to run the simulation the COMET experiment. The installation of ICEDUST can be done in either interactive mode or batch mode. ICEDUST require a lot of space, by using interactive mode to building the ICEDUST is very time consuming. Therefore, Batch mode was used by sending batch script to SLURM of the DICC HPC cluster. The ICEDUST Software was setup using the following this [command](https://github.com/dimashidayat99/Momemtum_Calibration-COMET/blob/main/Instructions/UMHPC_ICEDUST_Setup.md) for UMHPC server and this [command](https://github.com/dimashidayat99/Momemtum_Calibration-COMET/blob/main/Instructions/Deprecated/DICC_COMET_Setup.md) for DICC server.


#### Pion Skimming

The Geant4 based simulation read the oaRooTracker as input to continue the simulation and this simulation will give five output files which are log file, mac file, root file, dat file and rootracker file. The output files that is important in this study is root file and rootracker file, while the rest of files is not being used in this study. The oaRootracker files is classify into two types which are MC5A01 and MC5A02. The MC5A01 and MC5A02 is just oaRooTracker that contain particles before entering CyDet and after entering CyDet, respectively. This study is to used MC5A01 oaRooTracker to run the simulation. Since there are a lot of oaRooTracker files from MC5A01, the 100 oaRooTracker files was merge into 1 merged oaRooTracker file and there are total of 200 merged oaRooTracker files. The combination of oaRooTracker code can be seen in the `CyDetMomCalib/MakeRooTrackHist/` [directory](https://github.com/dimashidayat99/Momemtum_Calibration-COMET/tree/main/CyDetMomCalib/MakeRooTrackHist). Running the simulation with 200 merged oaRooTracker will be very time consuming. To run 1 unmerged oaRooTracker usually take about 1 days to complete. The long duration of the simulation is because of the simulation will run for all particles contain in the oaRooTracker. Due to the simulation is very time consuming, the duration of the simulation is reduced by removing all non related particle that is not important in this study. Since the PPC process is the interests process in this study, the pion (negative charge pion) is the only important parent particle. Therefore, every oaRooTracker will be filtered or skimmed to remove all the particles except for pion. The code for performing this skim can be found in `CyDetMomCalib/AnaRootracker` [directory](https://github.com/dimashidayat99/Momemtum_Calibration-COMET/tree/main/CyDetMomCalib/AnaRootracker). Using this method, simulation was made to be more efficient. Now, there are total of 200 skimmed pion oaRooTracker that will be used as input in the simulation. The simulation was run using 200 skimmed pion oaRooTracker as input by using the original (current) configuration of the COMET experiment.

### Modifying the Experiment Configuration

In the Geant4 based simulation, the user can modify the configuration of the COMET experiment in the simulation by changing the macro of ICEDUST package. Changing the configuration can be done by creating custom configuration file which can used to configure the parameter and initial setting of the simulation or programs. In other words, the configuration files is a file that is used to specify anything that is needed by the user to run the simulation based on the study needs. The code of performing the modification of experiment configuration can be found in the `CyDetMomCalib/SimG4CyDet/MuonCapTarget` [directory](https://github.com/dimashidayat99/Momemtum_Calibration-COMET/tree/main/CyDetMomCalib/SimG4CyDet/MuonCapTarget).

#### Hydrocarbon Material Target Configuration

The default configuration of material target (muon stopping target) in COMET experiment is Aluminium. The muon stopping target material of Aluminium need to be change to hydrocarbon based material. Consequently, the muon stopping target is changed by modifying the configuration of the simulation in the COMET experiment simulation. There are 4 additional configuration of hydrocarbon material target is created which are [polyethylene](https://github.com/dimashidayat99/Momemtum_Calibration-COMET/blob/main/CyDetMomCalib/SimG4CyDet/MuonCapTarget/config/rootrackerMC5A01_skimPiMinus_polyethylene.cfg), [polypropylene](https://github.com/dimashidayat99/Momemtum_Calibration-COMET/blob/main/CyDetMomCalib/SimG4CyDet/MuonCapTarget/config/rootrackerMC5A01_skimPiMinus_polypropylene.cfg), [polystyrene](https://github.com/dimashidayat99/Momemtum_Calibration-COMET/blob/main/CyDetMomCalib/SimG4CyDet/MuonCapTarget/config/rootrackerMC5A01_skimPiMinus_polystyrene.cfg) and [polyvinyl toluene](https://github.com/dimashidayat99/Momemtum_Calibration-COMET/blob/main/CyDetMomCalib/SimG4CyDet/MuonCapTarget/config/rootrackerMC5A01_skimPiMinus_polyvinyltoluene.cfg) as muon stopping target. The simulation was run for 4 different configuration of hydrocarbon target by using 200 skimmed pion oaRooTracker as input for each configuration.

#### Pion Particle Gun Configuration

The project utilized pion particle gun configuration. In principle, the particle gun will fire the pion directly to the material target in the CDC. Using pion gun configuration, the input samples is inessential in the simulation because the pion gun is actually act as input samples. The simulation was run using pion gun configuration along with the default configuration and polyethylene configuration.

### Event Reconstruction and Track Finding

The simulation of this study is based on the PPC process flow as discussed before. The idea is to find the electron and positron pair parameters (e.g. number of events, momentum, energy) without event selection criteria for the parameters. The track of all particle (pion, photon, electron and positron) involve in PPC process will find by finding the trajectory of each particle involve in PPC process in CyDet. The event reconstruction is done when the trajectory of pion, photon, electron and positron was found. This reconstruction of event will provide the information about their (pion, photon, electron and positrons) parents particle. Using the track finding and event reconstruction, the main algorithm was created based on the pair production process, pion neutral decay process, and proton-pion interaction process from the PPC process. The code of performing the event reconstruction and track finding can be found in `CyDetMomCalib/AnaOAEvent/` [directory](https://github.com/dimashidayat99/Momemtum_Calibration-COMET/tree/main/CyDetMomCalib/AnaOAEvent) where the main event reconstruction and track finding code is named as `Ananlyzer.C` which filter out all the event and focus only desired event in this study which is PPC.

# Result

There are total 7 simulations were run in this study: 1 simulation was done by using default configuration, 4 simulation were done by using hydrocarbon target configuration and two simulation were done by using pion gun configuration. The output of the 7 simulations then was extracted for the number of event of involving particle in PPC process, momentum and vertex position distribution for pair production was created.

## Default Configuration

For given current configuration of the COMET experiment, from 990678399 POT, there are only 12 electron-positron pair that is produced from PPC process. As expected, the pair production from PPC process is suppressed by the design of COMET experiment itself. This is because the electron pair production from PPC process is also one of the background event that is related with the pion capture process. To perform the momentum calibration, the distribution of momentum for electron and positron pair from PPC process is needed. With only 12 events, the distribution of momentum will be imperfect and have high statistical error. Some strategy is needed to increase the statistics of pair production.

<p align="middle">
<img src="https://github.com/dimashidayat99/Momemtum_Calibration-COMET/blob/main/Results/ppc_event_count/default_conf.png"  width="500"/>
</p>
<p align="middle">
    <em>PPC event counts for default configuration.</em>
</p>

## Hydrocarbon Target Configuration

The low statistics from simulation before must be improve in order to reduce the statistical uncertainty when generating the momentum distribution. The strategy that is used for this study to increase the statistics of pair production from PPC process is to change muon stopping target material from aluminium to the hydrocarbon based material. In principle, the PPC process require interaction of pion and proton to occur. Therefore, more pions will interact with proton if there are more number of proton of the stopping target. For this reason, the material with rich proton number will be used. Therefore, the hydrocarbon material is chosen in this study. The chosen hydrocarbon material must be available in the ICEDUST package, the available material chosen is polystyrene, polyethylene, polypropylene and polyvinyl toluene.

<p align="middle">
  <img src="https://github.com/dimashidayat99/Momemtum_Calibration-COMET/blob/main/Results/ppc_event_count/polyethylene_conf.png" width="500" />
    <p align="middle">
    <em>PPC event counts for polyethylene configuration</em>
    </p>
  <img src="https://github.com/dimashidayat99/Momemtum_Calibration-COMET/blob/main/Results/ppc_event_count/polypropylene_conf.png" width ="500" />
    <p align="middle">
    <em>PPC event counts for polypropylene configuration.</em>
    </p>
</p>

<p align="middle">
  <img src="https://github.com/dimashidayat99/Momemtum_Calibration-COMET/blob/main/Results/ppc_event_count/polystyrene_conf.png" width="500" />
    <p align="middle">
    <em>PPC event counts for polystyrene configuration.</em>
    </p>
  <img src="https://github.com/dimashidayat99/Momemtum_Calibration-COMET/blob/main/Results/ppc_event_count/polyvinyltoluene_conf.png" width="500" /> 
    <p align="middle">
    <em>PPC event counts for polyvinyltoluene configuration.</em>
    </p>
</p>

Compared with all the hydrocarbon based material target, It was found that the highest number of pair production from PPC process is 85 events by using polyethylene material target. The statistics is increase by factor of 7 from 12 events for [aluminium](https://github.com/dimashidayat99/Momemtum_Calibration-COMET/blob/main/Results/ppc_event_count/default_conf.png) target to 85 events for [polyethylene](https://github.com/dimashidayat99/Momemtum_Calibration-COMET/blob/main/Results/ppc_event_count/polyethylene_conf.png) target. The reason why polyethylene target produce highest number of events compared to other hydrocarbon material such as polystyrene, polypropylene and polyvinyl toluene is not fully understand yet and require more time for understanding about the molecular structure of hydrocarbon material. However, the 85 pair production also not enough to produce good momentum distribution, so that another strategy must be used to increase the statistics.

## Pion Gun Configuration

The momentum calibration study utilize the pion gun configuration (negatively charge pion gun) to increase the statistics. The pion gun was used to fire the pion directly to the material target in CyDet. Using this technique, the number of pions that initiate the PPC process will increase. Obviously, the pion gun configuration will produce significantly more pair production compare to the original configuration of the experiment, where the pion is produced by bombarding the proton to the pion production target.

<p align="middle">
  <img src="https://github.com/dimashidayat99/Momemtum_Calibration-COMET/blob/main/Results/ppc_event_count/pigun_default_conf.png" width="500" />
    <p align="middle">
    <em>PPC event counts for pi gun and aluminium target (default) configuration.</em>
    </p>
  <img src="https://github.com/dimashidayat99/Momemtum_Calibration-COMET/blob/main/Results/ppc_event_count/pigun_polyethylene_conf.png" width="500" /> 
    <p align="middle">
    <em>PPC event counts for pi gun and polyethylene configuration.</em>
    </p>
</p>

By using pion gun configuration, the pair production from PPC process is increase drastically by factor of 511, from 12 events to 6127 events for aluminium target (left figure). While the using polyethylene, the pair production from PPC process is also increase drastically by factor of 2484, from 85 events to 21178 events (right figure). Due to the sufficiently high of number of samples, the momentum distributions for the pair production were created.

<p align="middle">
  <img src="https://github.com/dimashidayat99/Momemtum_Calibration-COMET/blob/main/Results/momentum_pair_distribution/h_twogamma_lead_electron_mom.png" width="500" />
    <p align="middle">
    <em>Momentum distribution of electron.</em>
    </p>
  <img src="https://github.com/dimashidayat99/Momemtum_Calibration-COMET/blob/main/Results/momentum_pair_distribution/h_twogamma_lead_positron_mom.png" width="500" /> 
    <p align="middle">
    <em>Momentum distribution of positron.</em>
    </p>
</p>


## Vertex Position of Pair Production

In this study, the analysis was done only at truth level which refer to real physics simulation and not realistic compared to the SimDetectorResponse. Therefore, momentum distribution of pair production does not show where exactly the electron and positron pair is produced in CyDet. Therefore, the vertex of the pair production was plotted by using electron-positron pair initial position with implemented the main algorithm. The initial position of electron-positron pair (vertex) was plotted for transverse distance from z-axis at the z coordinate. The diagram of schematic layout of CDC with the vertex position as shown figure below. It was found that the CDC is denoted by rectangular shape that is located at 496 mm to 835 mm of transverse distance from z-axis while the radius of the CDC is in between 835 mm to 496 mm. In order for electron and positron leave the hits in CDC, the vertex must be produced inside the CDC radius which optimally at 200 mm to 400 mm. If the vertex is produced inside the CDC radius, the electron and positron will move toward the CDC resulting in increasing probability of electron and positron leave the hits in CDC. If the vertex is produced outside the CDC radius, the electron and positron will move far from CDC and never leave the hits in the CDC.

<p align="middle">
<img src="https://github.com/dimashidayat99/Momemtum_Calibration-COMET/blob/main/Results/vertex_position/h2_gamma_decayvtx_rz.png" width="600" />
</p>
<p align="middle">
    <em>Vertex position in the CyDet for transverse distance from z-axis against z coordinate.</em>
</p>

In figure above, there is no number of vertex is shown. Therefore, to observe how many vertex is produce at particular transverse distance from z-axis, the distribution of number of vertex against the transverse distance from z-axis is plotted as shown in figure below. Using this figure, the number of pair production vertex produced in CyDet can be estimated. By looking to the distribution of vertex in figure below, Most of the pair production vertex is produced outside the CDC radius while around 25% of the pair production vertex is produced inside the CDC radius (Noted that the CDC radius is at around 835 mm to 496 mm from the z-axis). From this observation, it simply said that only around 25% of total of the pair production vertex can be detected because only around 25% vertex that produced inside the CDC radius will leave the hits in CDC. The position of pair production vertex is important in this study to know if the pair production from PPC process is detectable or not. Although most of the pair production vertex is outside the CDC radius, the pair production from PPC process is still visible and detectable by the CDC. Imagine if all of the pair production is produced outside the CDC radius, there will be no signal is produced for this process and there is no point to continue this study if this (vertex production is outside CDC radius) is happening.

<p align="middle">
<img src="https://github.com/dimashidayat99/Momemtum_Calibration-COMET/blob/main/Results/vertex_position/h_gamma_decayvtx_r.png" width="600" />
</p>
<p align="middle">
    <em> Number of vertex produce at particular transverse distance from z-axis.</em>
</p>

## Event Estimation for Calibration Run of COMMET Experiment for Currrent Configuration

From the simulation result for current configuration, some analysis and event estimation for the calibration run can be calculated. In phase-I, the COMET experiment is expected to run for 146 days which equivalent to $1.26 × 10^7$ second and expected to have total POT of $3.2 × 10^19$. From this information, the rate of POT per second is given by

$$ Rate_{POT} = \frac{3.2 \times 10^{19}}{1.26 \times 10^7 } \approx 2.5397 \times 10^{12} POT s^{-1}$$

From result of [default](https://github.com/dimashidayat99/Momemtum_Calibration-COMET/blob/main/Results/ppc_event_count/default_conf.png) configuration event count, the number of pair production from PPC process with respect to POT is $1.2 × 10^{−8}$ per second. From this value, the rate of the pair production is given by rate of POT times the number of pair production with respect to POT

$$ Rate_{e^{+}e^{-}} = (2.5397 \times 10^{12})(1.2 \times 10^{-8}) = 30476 Pairs^{-1}$$

The rate of pair production from PPC process was calculated to be 30476 per second. The 30476 pair production per second will tell us on how long the beam and the detector should be run for calibration run. The idea is to run beam and detector until the statistical uncertainty is greatly reduce. As known, the more the statistics, the less the uncertainty. From the momentum distribution for [electron](https://github.com/dimashidayat99/Momemtum_Calibration-COMET/blob/main/Results/momentum_pair_distribution/h_twogamma_lead_electron_mom.png) and [positron](https://github.com/dimashidayat99/Momemtum_Calibration-COMET/blob/main/Results/momentum_pair_distribution/h_twogamma_lead_positron_mom.png) which have number of events of 21178 of pair productions, I will say that around 20000 and above specifically around 50000 is good enough to reduce the uncertainty. But this assumption is still early to make. The rate of pair production of 30476 is actually quite high for COMET experiment because of COMET experiment is design to suppressed the background events until the very small number of background events is expected to observed. The high number of rate of pair production is because of the calculation is naive estimation that based on many assumption such as not taking account the acceptance. For more complex analysis the acceptance and efficiency must be included in the analysis. The event estimation for calibration run require advanced understanding on the detector and more strategy increase the samples for the calibration run.

# Summary

The momentum calibration study in COMET experiment has been performed until the estimation of vertex of pair production position of PPC process in CyDet for simulation analysis and events estimation of pair production of PPC process for the calibration run for given current cpnfiguration. Although, there is no momentum calibration is done in this study, some of the objective of this study is achieved by successfully observed the visibility of PPC process in the CDC in CyDet. The calibration study require more complex analysis to become realistic enough to ensure the momentum calibration can be done in calibration run before the data taking of the COMET phase-I run. My suggestion for the future study is to put some thin layer material inside the CDC radius around 200 mm from z-axis as shown in figure below as denoted as red dotted line. It is because in principle, the photon must be near to a nucleus in order for photon conversion process to occur because of the conservation of the momentum and energy is satisfy. The photon conversion cannot occur in free space because of momentum and energy conservation cannot be satisfy. By putting some cylindrical material inside CDC radius, the probability of photon conversion will be increase and produce significant samples of pair production from PPC process. For the calibration run, the analysis of the event estimation of PPC process must include the acceptance and efficiency. My suggestion for calibration run is not to use the momentum cut (momentum window) only for calibration run. From the momentum distribution for[electron](https://github.com/dimashidayat99/Momemtum_Calibration-COMET/blob/main/Results/momentum_pair_distribution/h_twogamma_lead_electron_mom.png) and [positron](https://github.com/dimashidayat99/Momemtum_Calibration-COMET/blob/main/Results/momentum_pair_distribution/h_twogamma_lead_positron_mom.png) that is shown above, the number of electron that have momentum near 100 MeV/c is very low. Based on the average, most of the electron have momentum around 40 to 60 MeV/c. Therefore, to make observable event, the momentum window of 103.6 MeV/c < $P_e$ < 106.0 MeV/c should not be used in the calibration run. More advanced approaches may be implemented to improve the studies by a higher extend since the current study is only at truth level. More research and improvisations are required in the momentum calibration study.

<p align="middle">
<img src ="https://github.com/dimashidayat99/Momemtum_Calibration-COMET/blob/main/Results/vertex_position/suggestion.png" width="600" />
</p>
<p align="middle">
    <em> Proposed cylindrical thin material inside CDC around 200 mm from z-axis to increase the probability of photon conversion process.</em>
</p>
