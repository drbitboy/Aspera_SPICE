import math as m
import spiceypy as sp

def ramangle(utc, target, galaxy_targ):
    """Calculates ram angle, which is measured between velocity vector of Aspera & vector from Aspera
    to galaxy.

    Args:
        mkfile (str): metakernel containg data on Aspera, nearby bodies, and M82
        utc (str): date and time at which altitude will be found
        galaxy_targ (str): body ID for galaxy contained in mkfile

    Returns:
        float: ram angle
    """

    # # # # # PART 1: ANGLE BETWEEN VELOCITY AND POSITION VECTORS # # # # #

    et = sp.str2et(utc)
    ref = 'J2000'
    abcorr = 'NONE'

    # Generate velocity vector of Aspera wrt Earth
    aspera_state, lt = sp.spkezr(target, et, ref, abcorr, 'EARTH')
    vel = aspera_state[3:]

    # Generate position vector of galaxy wrt Aspera
    galaxy_state, lt = sp.spkezr(galaxy_targ, et, ref, abcorr, target)
    pos = galaxy_state[0:3]

    # Find angle between velocity and position vectors, convert from rad to deg
    ram_rad = sp.vsep(vel, pos)
    ram_deg = sp.convrt(ram_rad, 'RADIANS', 'DEGREES')

    # # # # # PART 2: S/C VELOCITY COMPONENT WRT TARGET # # # # #

    vel_sc_los = sp.vnorm(vel) * m.cos(ram_rad)
    return ram_deg, vel_sc_los

def ramangle_instr(utc, target, instr):
    """Calculates ram angle, which is measured between velocity vector of Aspera & vector from Aspera
    to galaxy.

    Args:
        mkfile (str): metakernel containg data on Aspera, nearby bodies, and M82
        utc (str): date and time at which altitude will be found
        galaxy_targ (str): body ID for galaxy contained in mkfile

    Returns:
        float: ram angle
    """

    # # # # # PART 1: ANGLE BETWEEN VELOCITY AND POSITION VECTORS # # # # #

    et = sp.str2et(utc)
    ref = 'J2000'
    abcorr = 'NONE'

    # Generate velocity vector of Aspera wrt Earth
    aspera_state, lt = sp.spkezr(target, et, ref, abcorr, 'EARTH')
    vel = aspera_state[3:]

    # Get Aspera's boresight vector in J2000
    instid = sp.bodn2c(instr)
    shape, frame, bsight, n, bounds = sp.getfov(instid,99,99,99)
    rotation_matrix = sp.pxform(frame, 'J2000', et)
    vboreJ2k = sp.mxv(rotation_matrix,bsight)

    # Find angle between velocity and position vectors, convert from rad to deg
    ra,dec = sp.recrad(vboreJ2k)[1:]
    # ram_rad = sp.vsep(vel, pos)
    # ram_deg = sp.convrt(ram_rad, 'RADIANS', 'DEGREES')

    # # # # # PART 2: S/C VELOCITY COMPONENT WRT TARGET # # # # #

    # vel_sc_los = sp.vnorm(vel) * m.cos(ram_rad)
    return ra, dec
