import os
from pathlib import Path
import spiceypy as sp
import numpy as np

def slitradec(utc, instr):
    """Calculates right ascension and declination of spacecraft instrument(s).

    Args:
        utc (str): date and time at which altitude will be found
        instr (str): frame ID for spacecraft's instrument

    Returns:
        float: ram angle
    """

    # Get instrument ID & boresight vector from frame name
    instr_id = sp.bodn2c(instr)
    shape, frame, bsight, n, bounds = sp.getfov(instr_id, 99, 99, 99)

    et = sp.str2et(utc)

    # Create rotation matrix, transform boresight vector from instrument frame to J2000
    rotation_matrix = sp.pxform(frame, 'J2000', et)
    bsight_trans = sp.mxv(rotation_matrix, bsight)

    # Convert new boresight vector into right ascension and declination
    x, y, z = bsight_trans

    # Replace 2 lines below with SPICE functions, delete Numpy functions
    ra = np.degrees(np.arctan2(y, x)) % 360
    dec = np.degrees(np.arcsin(z))

    # # #
    [ptarg, lt] = sp.spkpos('ASPERA', et, 'J2000', 'NONE', 'EARTH')
    [range, asp_ra_rad, asp_dec_rad] = sp.recrad(ptarg)
    asp_ra_deg = sp.convrt(asp_ra_rad, 'RADIANS', 'DEGREES')
    asp_dec_deg = sp.convrt(asp_dec_rad, 'RADIANS', 'DEGREES')
    # # #

    return ra, dec, asp_ra_deg, asp_dec_deg