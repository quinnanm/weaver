# Import Statements
import numpy as np
import uproot
import matplotlib.pyplot as plt


# Load Data files - this takes forever to complete
events_QCD = uproot.concatenate('/data/shared/cmantill/training/ak15_Jul9/train/QCD*/*.root:Events')
events_graviton = uproot.concatenate('/data/shared/cmantill/training/ak15_Jul9/train/Graviton*/*.root:Events')


#np.save('events_QCD', events_QCD)
#np.save('events_graviton', events_graviton)


# Save QCD and graviton variables as needed and cut based on selection criteria
target_mass_QCD = np.array(events_QCD.arrays()['target_mass'], "(fj_pt>200) & (fj_pt<2500) &
    (fj_genjetmsd<260) &
    ( ( ( (fj_isQCDb==1) |
     (fj_isQCDbb==1) | (fj_isQCDc==1) | (fj_isQCDcc==1) | (fj_isQCDlep == 1) |
     (fj_isQCDothers == 1) ) & (fj_genRes_mass<0) ) |
     (fj_isTop == 1) | (fj_isToplep==1) |
     ((fj_H_WW_4q==1) & (fj_maxdR_HWW_daus<2.0)) |
     ((fj_H_WW_elenuqq==1) & (fj_maxdR_HWW_daus<2.0)) |
     ((fj_H_WW_munuqq==1) & (fj_maxdR_HWW_daus<2.0)) |
     ((fj_H_WW_taunuqq==1) & (fj_maxdR_HWW_daus<2.0)) )")
target_mass_grav = np.array(events_graviton.arrays()['target_mass'], "(fj_pt>200) & (fj_pt<2500) &      
    (fj_genjetmsd<260) &                                                                          
    ( ( ( (fj_isQCDb==1) |                                                                        
     (fj_isQCDbb==1) | (fj_isQCDc==1) | (fj_isQCDcc==1) | (fj_isQCDlep == 1) |                    
     (fj_isQCDothers == 1) ) & (fj_genRes_mass<0) ) |                                             
     (fj_isTop == 1) | (fj_isToplep==1) |                                                         
     ((fj_H_WW_4q==1) & (fj_maxdR_HWW_daus<2.0)) |                                                
     ((fj_H_WW_elenuqq==1) & (fj_maxdR_HWW_daus<2.0)) |                                           
     ((fj_H_WW_munuqq==1) & (fj_maxdR_HWW_daus<2.0)) |                                            
     ((fj_H_WW_taunuqq==1) & (fj_maxdR_HWW_daus<2.0)) )")
fj_genjetmsd_QCD = np.array(events_QCD.arrays()['fj_genjetmsd'], "(fj_pt>200) & (fj_pt<2500) &      
    (fj_genjetmsd<260) &                                                                          
    ( ( ( (fj_isQCDb==1) |                                                                        
     (fj_isQCDbb==1) | (fj_isQCDc==1) | (fj_isQCDcc==1) | (fj_isQCDlep == 1) |                    
     (fj_isQCDothers == 1) ) & (fj_genRes_mass<0) ) |                                             
     (fj_isTop == 1) | (fj_isToplep==1) |                                                         
     ((fj_H_WW_4q==1) & (fj_maxdR_HWW_daus<2.0)) |                                                
     ((fj_H_WW_elenuqq==1) & (fj_maxdR_HWW_daus<2.0)) |                                           
     ((fj_H_WW_munuqq==1) & (fj_maxdR_HWW_daus<2.0)) |                                            
     ((fj_H_WW_taunuqq==1) & (fj_maxdR_HWW_daus<2.0)) )")
fj_genjetmsd_grav = np.array(events_graviton.arrays()['fj_genjetmsd'], "(fj_pt>200) & (fj_pt<2500) &      
    (fj_genjetmsd<260) &                                                                          
    ( ( ( (fj_isQCDb==1) |                                                                        
     (fj_isQCDbb==1) | (fj_isQCDc==1) | (fj_isQCDcc==1) | (fj_isQCDlep == 1) |                    
     (fj_isQCDothers == 1) ) & (fj_genRes_mass<0) ) |                                             
     (fj_isTop == 1) | (fj_isToplep==1) |                                                         
     ((fj_H_WW_4q==1) & (fj_maxdR_HWW_daus<2.0)) |                                                
     ((fj_H_WW_elenuqq==1) & (fj_maxdR_HWW_daus<2.0)) |                                           
     ((fj_H_WW_munuqq==1) & (fj_maxdR_HWW_daus<2.0)) |                                            
     ((fj_H_WW_taunuqq==1) & (fj_maxdR_HWW_daus<2.0)) )")
fj_pt_QCD = np.array(events_QCD.arrays()['fj_pt'], "(fj_pt>200) & (fj_pt<2500) &      
    (fj_genjetmsd<260) &                                                                          
    ( ( ( (fj_isQCDb==1) |                                                                        
     (fj_isQCDbb==1) | (fj_isQCDc==1) | (fj_isQCDcc==1) | (fj_isQCDlep == 1) |                    
     (fj_isQCDothers == 1) ) & (fj_genRes_mass<0) ) |                                             
     (fj_isTop == 1) | (fj_isToplep==1) |                                                         
     ((fj_H_WW_4q==1) & (fj_maxdR_HWW_daus<2.0)) |                                                
     ((fj_H_WW_elenuqq==1) & (fj_maxdR_HWW_daus<2.0)) |                                           
     ((fj_H_WW_munuqq==1) & (fj_maxdR_HWW_daus<2.0)) |                                            
     ((fj_H_WW_taunuqq==1) & (fj_maxdR_HWW_daus<2.0)) )")
fj_pt_grav = np.array(events_graviton.arrays()['fj_pt'], "(fj_pt>200) & (fj_pt<2500) &      
    (fj_genjetmsd<260) &                                                                          
    ( ( ( (fj_isQCDb==1) |                                                                        
     (fj_isQCDbb==1) | (fj_isQCDc==1) | (fj_isQCDcc==1) | (fj_isQCDlep == 1) |                    
     (fj_isQCDothers == 1) ) & (fj_genRes_mass<0) ) |                                             
     (fj_isTop == 1) | (fj_isToplep==1) |                                                         
     ((fj_H_WW_4q==1) & (fj_maxdR_HWW_daus<2.0)) |                                                
     ((fj_H_WW_elenuqq==1) & (fj_maxdR_HWW_daus<2.0)) |                                           
     ((fj_H_WW_munuqq==1) & (fj_maxdR_HWW_daus<2.0)) |                                            
     ((fj_H_WW_taunuqq==1) & (fj_maxdR_HWW_daus<2.0)) )")
fj_isQCDb_QCD = np.array(events_QCD.arrays()['fj_isQCDb'], "(fj_pt>200) & (fj_pt<2500) &      
    (fj_genjetmsd<260) &                                                                          
    ( ( ( (fj_isQCDb==1) |                                                                        
     (fj_isQCDbb==1) | (fj_isQCDc==1) | (fj_isQCDcc==1) | (fj_isQCDlep == 1) |                    
     (fj_isQCDothers == 1) ) & (fj_genRes_mass<0) ) |                                             
     (fj_isTop == 1) | (fj_isToplep==1) |                                                         
     ((fj_H_WW_4q==1) & (fj_maxdR_HWW_daus<2.0)) |                                                
     ((fj_H_WW_elenuqq==1) & (fj_maxdR_HWW_daus<2.0)) |                                           
     ((fj_H_WW_munuqq==1) & (fj_maxdR_HWW_daus<2.0)) |                                            
     ((fj_H_WW_taunuqq==1) & (fj_maxdR_HWW_daus<2.0)) )")
fj_isQCDb_grav = np.array(events_graviton.arrays()['fj_isQCDb'], "(fj_pt>200) & (fj_pt<2500) &      
    (fj_genjetmsd<260) &                                                                          
    ( ( ( (fj_isQCDb==1) |                                                                        
     (fj_isQCDbb==1) | (fj_isQCDc==1) | (fj_isQCDcc==1) | (fj_isQCDlep == 1) |                    
     (fj_isQCDothers == 1) ) & (fj_genRes_mass<0) ) |                                             
     (fj_isTop == 1) | (fj_isToplep==1) |                                                         
     ((fj_H_WW_4q==1) & (fj_maxdR_HWW_daus<2.0)) |                                                
     ((fj_H_WW_elenuqq==1) & (fj_maxdR_HWW_daus<2.0)) |                                           
     ((fj_H_WW_munuqq==1) & (fj_maxdR_HWW_daus<2.0)) |                                            
     ((fj_H_WW_taunuqq==1) & (fj_maxdR_HWW_daus<2.0)) )")
fj_genRes_mass_QCD = np.array(events_QCD.arrays()['fj_genRes_mass'], "(fj_pt>200) & (fj_pt<2500) &      
    (fj_genjetmsd<260) &                                                                          
    ( ( ( (fj_isQCDb==1) |                                                                        
     (fj_isQCDbb==1) | (fj_isQCDc==1) | (fj_isQCDcc==1) | (fj_isQCDlep == 1) |                    
     (fj_isQCDothers == 1) ) & (fj_genRes_mass<0) ) |                                             
     (fj_isTop == 1) | (fj_isToplep==1) |                                                         
     ((fj_H_WW_4q==1) & (fj_maxdR_HWW_daus<2.0)) |                                                
     ((fj_H_WW_elenuqq==1) & (fj_maxdR_HWW_daus<2.0)) |                                           
     ((fj_H_WW_munuqq==1) & (fj_maxdR_HWW_daus<2.0)) |                                            
     ((fj_H_WW_taunuqq==1) & (fj_maxdR_HWW_daus<2.0)) )")
fj_genRes_mass_grav = np.array(events_graviton.arrays()['fj_genRes_mass'], "(fj_pt>200) & (fj_pt<2500) &      
    (fj_genjetmsd<260) &                                                                          
    ( ( ( (fj_isQCDb==1) |                                                                        
     (fj_isQCDbb==1) | (fj_isQCDc==1) | (fj_isQCDcc==1) | (fj_isQCDlep == 1) |                    
     (fj_isQCDothers == 1) ) & (fj_genRes_mass<0) ) |                                             
     (fj_isTop == 1) | (fj_isToplep==1) |                                                         
     ((fj_H_WW_4q==1) & (fj_maxdR_HWW_daus<2.0)) |                                                
     ((fj_H_WW_elenuqq==1) & (fj_maxdR_HWW_daus<2.0)) |                                           
     ((fj_H_WW_munuqq==1) & (fj_maxdR_HWW_daus<2.0)) |                                            
     ((fj_H_WW_taunuqq==1) & (fj_maxdR_HWW_daus<2.0)) )")
fj_msoftdrop_QCD = np.array(events_QCD.arrays()['fj_msoftdrop'], "(fj_pt>200) & (fj_pt<2500) &      
    (fj_genjetmsd<260) &                                                                          
    ( ( ( (fj_isQCDb==1) |                                                                        
     (fj_isQCDbb==1) | (fj_isQCDc==1) | (fj_isQCDcc==1) | (fj_isQCDlep == 1) |                    
     (fj_isQCDothers == 1) ) & (fj_genRes_mass<0) ) |                                             
     (fj_isTop == 1) | (fj_isToplep==1) |                                                         
     ((fj_H_WW_4q==1) & (fj_maxdR_HWW_daus<2.0)) |                                                
     ((fj_H_WW_elenuqq==1) & (fj_maxdR_HWW_daus<2.0)) |                                           
     ((fj_H_WW_munuqq==1) & (fj_maxdR_HWW_daus<2.0)) |                                            
     ((fj_H_WW_taunuqq==1) & (fj_maxdR_HWW_daus<2.0)) )")
fj_msoftdrop_grav = np.array(events_graviton.arrays()['fj_msoftdrop'], "(fj_pt>200) & (fj_pt<2500) &      
    (fj_genjetmsd<260) &                                                                          
    ( ( ( (fj_isQCDb==1) |                                                                        
     (fj_isQCDbb==1) | (fj_isQCDc==1) | (fj_isQCDcc==1) | (fj_isQCDlep == 1) |                    
     (fj_isQCDothers == 1) ) & (fj_genRes_mass<0) ) |                                             
     (fj_isTop == 1) | (fj_isToplep==1) |                                                         
     ((fj_H_WW_4q==1) & (fj_maxdR_HWW_daus<2.0)) |                                                
     ((fj_H_WW_elenuqq==1) & (fj_maxdR_HWW_daus<2.0)) |                                           
     ((fj_H_WW_munuqq==1) & (fj_maxdR_HWW_daus<2.0)) |                                            
     ((fj_H_WW_taunuqq==1) & (fj_maxdR_HWW_daus<2.0)) )")

# Make plots of each parameter for QCD and graviton
# Target Mass
plt.figure()
plt.hist(target_mass_QCD, bins = 'auto', histtype = 'step', label='QCD')
plt.hist(target_mass_grav, bins = 'auto', histtype = 'step', label='Graviton')
plt.xlabel("Target Mass (GeV)")
plt.ylabel('Jets')
plt.legend()
plt.savefig('target_mass.png', bbox_inches='tight')

# fj_genjetmsd
plt.figure()
plt.hist(fj_genjetmsd_QCD, bins = 'auto', histtype = 'step', label='QCD')
plt.hist(fj_genjetmsd_grav, bins = 'auto', histtype = 'step', label='Graviton')
plt.xlabel("fj_genjetmsd")
plt.ylabel('Jets')
plt.legend()
plt.savefig('genjetmsd.png', bbox_inches='tight')

# fj_pt
plt.figure()
plt.hist(fj_pt_QCD, bins = 'auto', histtype = 'step', label='QCD')
plt.hist(fj_pt_grav, bins = 'auto', histtype = 'step', label='Graviton')
plt.xlabel("fj_pt")
plt.ylabel('Jets')
plt.legend()
plt.savefig('pt.png', bbox_inches='tight')

# fj_isQCDb
plt.figure()
plt.hist(fj_isQCDb_QCD, bins = 'auto', histtype = 'step', label='QCD')
plt.hist(fj_isQCDb_grav, bins = 'auto', histtype = 'step', label='Graviton')
plt.xlabel("fj_isQCDb")
plt.ylabel('Jets')
plt.legend()
plt.savefig('isQCDb.png', bbox_inches='tight')

# fj_genRes_mass
plt.figure()
plt.hist(fj_genRes_mass_QCD, bins = 'auto', histtype = 'step', label='QCD')
plt.hist(fj_genRes_mass_grav, bins = 'auto', histtype = 'step', label='Graviton')
plt.xlabel("fj_genRes_mass")
plt.ylabel('Jets')
plt.legend()
plt.savefig('genRes_mass.png', bbox_inches='tight')

# fj_msoftdrop
plt.figure()
plt.hist(fj_msoftdrop_QCD, bins = 'auto', histtype = 'step', label='QCD')
plt.hist(fj_msoftdrop_grav, bins = 'auto', histtype = 'step', label='Graviton')
plt.xlabel("fj_msoftdrop")
plt.ylabel('Jets')
plt.legend()
plt.savefig('msoftdrop.png', bbox_inches='tight')

