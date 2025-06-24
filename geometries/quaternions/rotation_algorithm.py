import spiceypy as sp

def rotation_matrix_sclk(sclkdp, Target):  #btc replace with sp.pxform?
    inst_id = -1999000
    sc_id = sp.bodn2c(Target)#btc frinfo(getfov(inst_id...))) can do it
    #print(sc_id) 
    tolerance = sp.sctiks(sc_id,"1:90")#btc sc_id not needed with pxform
    ref = 'J2000'
    cmat = sp.ckgp(inst_id,sclkdp,tolerance,ref)
    return cmat

def rotation_matrix_utc(utc, Target):  #btc replace with sp.pxform?
    sc_id = sp.bodn2c(Target)
    sclkdp = sp.sce2t(sc_id,sp.utc2et(utc))
    return rotation_matrix_sclk(sclkdp,Target)

def make_quart(rotation_matrix):
    return (sp.m2q(rotation_matrix))
