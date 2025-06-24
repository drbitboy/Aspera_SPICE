import spiceypy as sp

def ramangle(utc, instr):
    """Calculates ram angle, which is measured between Earth-relative
    velocity vector of Aspera & boresight vector of instrument

    Args:
        utc (str): date and time at which altitude will be found
        instr (str): instrument from which to extract frame & boresight

    Returns:
        float: ram angle
    """

    # # # # # PART 1: ANGLE BETWEEN EARTH-RELATIVE VELOCITY AND BORESIGHT VECTORS # # # # #

    et = sp.str2et(utc)
    abcorr = 'NONE'

    #btc get instrument frame and borsight, also instrument frame center
    ref,vbore = sp.getfov(sp.bods2c(instr),99,99,99)[1:3]
    target = sp.bodc2s(sp.frinfo(sp.namfrm(ref))[0])

    # Generate velocity vector of Aspera wrt Earth
    #btc ... in instrument frame
    aspera_state, lt = sp.spkezr(target, et, ref, abcorr, 'EARTH')
    vel = aspera_state[3:]

    #btc galaxy target is irrelevant

    # Find angle between velocity and bore vectors, convert from rad to deg
    #btc velocity and boresight vectors are already in instrument frame
    ram_rad = sp.vsep(vel, vbore)
    ram_deg = sp.convrt(ram_rad, 'RADIANS', 'DEGREES')

    # # # # # PART 2: S/C VELOCITY COMPONENT ALONG BORESIGHT # # # # #
    vel_sc_los = sp.vdot(sp.vhat(vbore), vel)
    return ram_deg

"""#btc removed incomplete function:
def ramangle_instr(utc, target, instr):
"""
