import spiceypy as sp

def moonboresight(utc, target, galaxy_targ):
    """Calculates angle between Moon's unit vector wrt Aspera and boresight vector.

    Args:
        mkfile (str): metakernel containg data on Aspera, nearby bodies, and M82
        utc (str): date and time at which moon boresight angle will be found
        galaxy_targ (str): body ID for galaxy contained in mkfile

    Returns:
        float: moon boresight angle
    """

    # # # # # PART 1: POSITION VECTOR FROM ASPERA TO MOON # # # # #

    et = sp.str2et(utc)
    ref = 'J2000'
    abcorr = 'NONE'

    # Find position vector of Aspera wrt Moon
    starg, lt = sp.spkpos('MOON', et, ref, abcorr, target)

    # # # # # PART 2: BORESIGHT VECTOR # # # # #

    # Find position vector of Aspera wrt galaxy
    gtarg, lt = sp.spkpos(galaxy_targ, et, ref, abcorr, target)

    # # # # # PART 3: MOON BORESIGHT ANGLE # # # # #

    # Calculate angle between vectors
    sb_rad = sp.vsep(starg, gtarg)
    sb_deg = sp.convrt(sb_rad, 'RADIANS', 'DEGREES')

    return sb_deg

def moonboresight_instr(utc, target, instr):
    """Calculates angle between Moon's unit vector wrt Aspera and boresight vector.

    Args:
        mkfile (str): metakernel containg data on Aspera, nearby bodies, and M82
        utc (str): date and time at which moon boresight angle will be found
        instr (str): instrument name on Aspera

    Returns:
        float: moon boresight angle
    """

    # # # # # PART 1: POSITION VECTOR FROM ASPERA TO MOON # # # # #

    et = sp.str2et(utc)
    ref = 'J2000'
    abcorr = 'NONE'

    # Find position vector of Aspera wrt Moon
    starg, lt = sp.spkpos('MOON', et, ref, abcorr, target)

    # # # # # PART 2: BORESIGHT VECTOR # # # # #

    # Find Aspera's boresight vector in J2000
    instid = sp.bodn2c(instr)
    shape, frame, bsight, n, bounds = sp.getfov(instid,99,99,99)
    rotation_matrix = sp.pxform(frame, ref, et)
    vboreJ2k = sp.mxv(rotation_matrix,bsight)

    # # # # # PART 3: MOON BORESIGHT ANGLE # # # # #

    # Calculate angle between vectors
    sb_rad = sp.vsep(starg, vboreJ2k)
    sb_deg = sp.convrt(sb_rad, 'RADIANS', 'DEGREES')

    return sb_deg
