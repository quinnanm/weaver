import uproot
import matplotlib.pyplot as plt
import numpy as np

events = uproot.open('/storage/af/user/cmantill/training/weaver/output/3_v04_ak15_regression_hwwQCD_Jul21_ep19.root:Events')

output_mass = np.array(events.arrays()['output'])
softdrop = np.array(events.arrays()['fj_msoftdrop'])
genjetmsd = np.array(events.arrays()['fj_genjetmsd'])
fj_H_WW_4q = np.array(events.arrays()['fj_H_WW_4q'])
fj_H_WW_elenuqq = np.array(events.arrays('fj_H_WW_elenuqq'))
fj_H_WW_munuqq = np.array(events.arrays('fj_H_WW_munuqq'))
fj_isQCDb = np.array(events.arrays('fj_isQCDb'))
fj_isQCDbb = np.array(events.arrays('fj_isQCDbb'))
fj_isQCDc = np.array(events.arrays('fj_isQCDc'))
fj_isQCDcc = np.array(events.arrays('fj_isQCDcc'))
fj_isQCDlep = np.array(events.arrays('fj_isQCDlep'))
fj_isQCDothers = np.array(events.arrays('fj_isQCDothers'))
size = len(output_mass)

output_mass_4q = output_mass[np.nonzero(fj_H_WW_4q)]
output_mass_elenuqq = output_mass[np.nonzero(fj_H_WW_elenuqq)]
output_mass_munuqq = output_mass[np.nonzero(fj_H_WW_munuqq)]
output_mass_isQCDb = output_mass[np.nonzero(fj_isQCDb)]
output_mass_isQCDbb = output_mass[np.nonzero(fj_isQCDbb)]
output_mass_isQCDc = output_mass[np.nonzero(fj_isQCDc)]
output_mass_isQCDcc = output_mass[np.nonzero(fj_isQCDcc)]
output_mass_isQCDlep = output_mass[np.nonzero(fj_isQCDlep)]
output_mass_isQCDothers = output_mass[np.nonzero(fj_isQCDothers)]

target_mass = np.maximum(1, np.where(events.arrays()["fj_genRes_mass"]>0, events.arrays()["fj_genRes_mass"], events.arrays()["fj_genjetmsd"]))
target_mass_4q = target_mass[np.nonzero(fj_H_WW_4q)]
target_mass_elenuqq = target_mass[np.nonzero(fj_H_WW_elenuqq)]
target_mass_munuqq = target_mass[np.nonzero(fj_H_WW_munuqq)]
target_mass_isQCDb = target_mass[np.nonzero(fj_isQCDb)]
target_mass_isQCDbb = target_mass[np.nonzero(fj_isQCDbb)]
target_mass_isQCDc = target_mass[np.nonzero(fj_isQCDc)]
target_mass_isQCDcc = target_mass[np.nonzero(fj_isQCDcc)]
target_mass_isQCDlep = target_mass[np.nonzero(fj_isQCDlep)]
target_mass_isQCDothers = target_mass[np.nonzero(fj_isQCDothers)]



softdrop_4q = softdrop[np.nonzero(fj_H_WW_4q)]
softdrop_elenuqq = softdrop[np.nonzero(fj_H_WW_elenuqq)]
softdrop_munuqq = softdrop[np.nonzero(fj_H_WW_munuqq)]
softdrop_isQCDb = softdrop[np.nonzero(fj_isQCDb)]
softdrop_isQCDbb = softdrop[np.nonzero(fj_isQCDbb)]
softdrop_isQCDc = softdrop[np.nonzero(fj_isQCDc)]
softdrop_isQCDcc = softdrop[np.nonzero(fj_isQCDcc)]
softdrop_isQCDlep = softdrop[np.nonzero(fj_isQCDlep)]
softdrop_isQCDothers = softdrop[np.nonzero(fj_isQCDothers)]


genjetmsd_4q = genjetmsd[np.nonzero(fj_H_WW_4q)]
genjetmsd_elenuqq = genjetmsd[np.nonzero(fj_H_WW_elenuqq)]
genjetmsd_munuqq = genjetmsd[np.nonzero(fj_H_WW_munuqq)]
genjetmsd_isQCDb = genjetmsd[np.nonzero(fj_isQCDb)]
genjetmsd_isQCDbb = genjetmsd[np.nonzero(fj_isQCDbb)]
genjetmsd_isQCDc = genjetmsd[np.nonzero(fj_isQCDc)]
genjetmsd_isQCDcc = genjetmsd[np.nonzero(fj_isQCDcc)]
genjetmsd_isQCDlep = genjetmsd[np.nonzero(fj_isQCDlep)]
genjetmsd_isQCDothers = genjetmsd[np.nonzero(fj_isQCDothers)]




# HWW reco
plt.figure()
#plt.hist(output_mass, bins='auto', histtype="step", label = 'All')
plt.hist(output_mass_4q, bins='auto', histtype="step", label = 'qqqq')
plt.hist(output_mass_elenuqq, bins='auto', histtype="step", label = 'enuqq')
plt.hist(output_mass_munuqq, bins='auto', histtype="step", label = 'munuqq')
plt.xlabel('Regressed Mass (GeV)')
plt.ylabel('Jets')
plt.legend()
plt.savefig('output_mass_hist.png', bbox_inches = 'tight')

# HWW reco/target                                                                                                                                                                                                                   
plt.figure() 
plt.hist(output_mass_4q/target_mass_4q, bins='auto', histtype="step", label = 'qqqq')
plt.hist(output_mass_elenuqq/target_mass_elenuqq, bins='auto', histtype="step", label = 'enuqq')
plt.hist(output_mass_munuqq/target_mass_munuqq, bins='auto', histtype="step", label = 'munuqq')
plt.xlabel('m_reco/m_target')
plt.ylabel('Jets')
plt.legend()
plt.xlim(0,2)
plt.savefig("output_mass_reco_by_target.png", bbox_inches = 'tight')


# HWW reco QCD
plt.figure()
plt.hist(output_mass_isQCDb, bins='auto', histtype="step", label = 'QCDb')
plt.hist(output_mass_isQCDbb, bins='auto', histtype="step", label = 'QCDbb')
plt.hist(output_mass_isQCDc, bins='auto', histtype="step", label = 'QCDc')
plt.hist(output_mass_isQCDcc, bins='auto', histtype="step", label = 'QCDcc')
plt.hist(output_mass_isQCDlep, bins='auto', histtype="step", label = 'QCDlep')
plt.hist(output_mass_isQCDothers, bins='auto', histtype="step", label = 'QCDothers')
plt.xlabel('Regressed Mass (GeV)')
plt.ylabel('Jets')
plt.legend()
plt.savefig('output_mass_QCD_hist.png', bbox_inches = 'tight')



# HWW reco QCD/ target QCD 
plt.figure()
#plt.hist(output_mass, bins='auto', histtype="step", label = 'All')                                                                                                                                                                
plt.hist(output_mass_isQCDb/target_mass_isQCDb, bins='auto', histtype="step", label = 'QCDb')
plt.hist(output_mass_isQCDbb/target_mass_isQCDbb, bins='auto', histtype="step", label = 'QCDbb')
plt.hist(output_mass_isQCDc/target_mass_isQCDc, bins='auto', histtype="step", label = 'QCDc')
plt.hist(output_mass_isQCDcc/target_mass_isQCDcc, bins='auto', histtype="step", label = 'QCDcc')
plt.hist(output_mass_isQCDlep/target_mass_isQCDlep, bins='auto', histtype="step", label = 'QCDlep')
plt.hist(output_mass_isQCDothers/target_mass_isQCDothers, bins='auto', histtype="step", label = 'QCDothers')
plt.xlabel('m_reco/m_target')
plt.ylabel('Jets')
plt.legend()
plt.xlim(0,2)
plt.savefig("output_mass_reco_by_target_QCD.png", bbox_inches = 'tight')






plt.figure()
#plt.hist(softdrop, bins='auto', histtype="step", label = 'All')
plt.hist(softdrop_4q, bins='auto', histtype="step", label = 'qqqq')
plt.hist(softdrop_elenuqq, bins='auto', histtype="step", label = 'enuqq')
plt.hist(softdrop_munuqq, bins='auto', histtype="step", label = 'munuqq')
plt.xlabel('fj_msoftdrop (GeV)')
plt.ylabel('Jets')
plt.xlim(0,500)
plt.legend()
plt.savefig('msoftdrop_hist.png', bbox_inches='tight')

plt.figure()
plt.hist(softdrop_isQCDb, bins='auto', histtype="step", label = 'QCDb')
plt.hist(softdrop_isQCDbb, bins='auto', histtype="step", label = 'QCDbb')
plt.hist(softdrop_isQCDc, bins='auto', histtype="step", label = 'QCDc')
plt.hist(softdrop_isQCDcc, bins='auto', histtype="step", label = 'QCDcc')
plt.hist(softdrop_isQCDlep, bins='auto', histtype="step", label = 'QCDlep')
plt.hist(softdrop_isQCDothers, bins='auto', histtype="step", label = 'QCDothers')
plt.xlabel('fj_msoftdrop (GeV)')
plt.ylabel('Jets')
plt.xlim(0,500)
plt.legend()
plt.savefig('msoftdrop_QCD_hist.png', bbox_inches='tight')

plt.figure()
#plt.hist(genjetmsd, bins='auto', histtype="step", label = 'All')
plt.hist(genjetmsd_4q, bins='auto', histtype="step", label = 'qqqq')
plt.hist(genjetmsd_elenuqq, bins='auto', histtype="step", label = 'enuqq')
plt.hist(genjetmsd_munuqq, bins='auto', histtype="step", label = 'munuqq')
plt.xlabel('fj_genjetmsd (GeV)')
plt.ylabel('Jets')
plt.xlim(0,500)
plt.legend()
plt.savefig('genjetmsd_hist.png', bbox_inches='tight')

plt.figure()
plt.hist(genjetmsd_isQCDb, bins='auto', histtype="step", label = 'QCDb')
plt.hist(genjetmsd_isQCDbb, bins='auto', histtype="step", label = 'QCDbb')
plt.hist(genjetmsd_isQCDc, bins='auto', histtype="step", label = 'QCDc')
plt.hist(genjetmsd_isQCDcc, bins='auto', histtype="step", label = 'QCDcc')
plt.hist(genjetmsd_isQCDlep, bins='auto', histtype="step", label = 'QCDlep')
plt.hist(genjetmsd_isQCDothers, bins='auto', histtype="step", label = 'QCDothers')
plt.xlabel('fj_genjetmsd (GeV)')
plt.ylabel('Jets')
plt.xlim(0,500)
plt.legend()
plt.savefig('genjetmsd_QCD_hist.png', bbox_inches='tight')
