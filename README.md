vHmumuGenerator
===============

This program creates vHmumu 13 TeV Monte Carlo sample
Instructions
============

A UF HPC account is highly recommended in order to use this program.

This program has been tested with CMSSW_7_4_2. To use this program, obtain this CMSSW release and move into the source directory.

    cmsrel CMSSW_7_4_2
    cd CMSSW_7_4_2
    cd src
    cmsenv
  
Then, clone this git repository and compile CMSSW

    git clone https://github.com/bregnery/vHmumuGenerator.git
    scram b
    cmsenv
  
Next, move into ttHmumuGenerator. Then, update the email, working directory, and output directory in generator.submit and MINIAODgenerator.submit. Also, update the input and output directories in convertMC_MINIAOD.py. The number of events per job can be adjusted in h2mu_tth_M125GeV_13TeV_FULLSIM_cfg.py and the number of jobs can be adjusted in generator.submit (1-maxJobs).

Then, generate the ttHmumu sample by submitting a job to HPC using the generator.submit script.

    qsub generator.submit

Finally, convert these files to miniAOD format by submitting a job to HPC with the MINIAODgenerator.submit script.

    qsub MINIAODgenerator.submit    

For ntuplizing stages see UfHMuMuCode.

Documentation
=============

The cfg file was created using the following

    cmsDriver.py Configuration/Generator/python/Wh2mu_wh_M125GeV_13TeV_cfi.py \ --step GEN,SIM,DIGI,L1,DIGI2RAW,HLT:GRun,RAW2DIGI,L1Reco,RECO \ --pileup_input dbs:/MinBias_TuneA2MB_13TeV-pythia8/Fall13-POSTLS162_V1-v1/GEN-SIM \ --pileup AVE_20_BX_25ns \ --conditions PHYS14_25_V1 \ --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1 \ --magField 38T_PostLS1 \ --geometry Extended2015 \ --beamspot Realistic8TeVCollision \ --datatier GEN-SIM \ --mc \ --eventcontent AODSIM \ --python_filename h2mu_wh_M125GeV_13TeV_FULLSIM_cfg.py \ -n 10 --no_exec \ --fileout h2mu_wh_M125GeV_13TeV_pythia8_AODSIM_1.root

