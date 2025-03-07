import spiceypy as sp

def rotation_matrix_sclk(sclkdp, Target):
    inst_id = -1999000
    sc_id = sp.bodn2c(Target)
    #print(sc_id) 
    tolerance = sp.sctiks(sc_id,"1:90")
    ref = 'J2000'
    cmat = sp.ckgp(inst_id,sclkdp,tolerance,ref)
    return cmat

def make_quart(rotation_matrix):
    return (sp.m2q(rotation_matrix))