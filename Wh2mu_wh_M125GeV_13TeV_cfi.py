import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

source = cms.Source("EmptySource")

generator = cms.EDFilter("Pythia8GeneratorFilter",
	comEnergy = cms.double(13000.0),
	crossSection = cms.untracked.double(6.44),
	filterEfficiency = cms.untracked.double(1),
	maxEventsToPrint = cms.untracked.int32(1),
	pythiaHepMCVerbosity = cms.untracked.bool(False),
	pythiaPylistVerbosity = cms.untracked.int32(1),
	PythiaParameters = cms.PSet(
		pythia8CommonSettingsBlock,
		pythia8CUEP8M1SettingsBlock,
		processParameters = cms.vstring(
			'Main:timesAllowErrors = 10000',
			'HiggsSM:ffbar2HW=on', #produce SM W h0 via s-channel W^+- exchange
			'25:m0 = 125.09', #set h0 mass to 125.09 GeV
			'25:onMode = off', #switch off all h0 decay channels
			'25:onIfMatch 13 -13', #switch on the h0->mu-mu+ decay mode only
			'24:m0 = 80.4', #set W0 mass to 80.4 GeV
		),
		parameterSets = cms.vstring('pythia8CommonSettings',
			'pythia8CUEP8M1Settings',
			'processParameters')
		)
	)

ProductionFilterSequence = cms.Sequence(generator)
