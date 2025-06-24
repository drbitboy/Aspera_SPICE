import os
from pathlib import Path
import spiceypy as sp

def sunangle(utc, instr):
    """Calculates the angle between the direction of the Sun as seen from Aspera and the slit
    boresight direction.

    Args:
        utc (str): date and time at which altitude will be found
        targ (str): S/C name
        instr (str): instrument name on Aspera

    Returns:
        float: sun boresight angle
    """

    # # # # # PART 1: POSITION VECTOR FROM ASPERA TO SUN # # # # #

    et = sp.str2et(utc)
    ref = 'ASP_SPACECRAFT'
    abcorr = 'NONE'

    # Generate position vector of Aspera wrt Sun
    [sun_state, lt] = sp.spkpos('SUN', et, ref, abcorr, 'ASPERA')
    sun_pos = sun_state[0:3]
    sun_pos_dir = sp.vhat(sun_pos)

    # # # # # PART 2: BORESIGHT VECTOR # # # # #

    # Get boresight vector of instrument
    instrid = sp.bodn2c(instr)
    shape, frame, bsight, n, bounds = sp.getfov(instrid, 4, 32, 32)

    # Transform boresight vector into s/c frame
    rotation_matrix = sp.pxform(frame, 'ASP_SPACECRAFT', et)
    bsight_sc = sp.mxv(rotation_matrix, bsight)
    
    # # # # # PART 3: SUN BORESIGHT ANGLE # # # # #

    # Calculate angle between position vectors
    sb_rad = sp.vsep(sun_pos_dir, bsight_sc)
    sb_deg = sp.convrt(sb_rad, 'RADIANS', 'DEGREES')

    return sb_deg