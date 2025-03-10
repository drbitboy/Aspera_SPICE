import spiceypy as sp

def moonboresight(utc, target, galaxy_targ):
    """Calculates angle between Moon's unit vector wrt Aspera and boresight vector.

    Args:
        utc (str): date and time at which moon boresight angle will be found
        target (str): observer that carries instrument
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
        utc (str): date and time at which moon boresight angle will be found
        target (str): observer that carries instrument
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

#btc simpler approach?
def moonboresight_instr_btc(utc, instr):
    """Calculates angle between Moon's unit vector wrt boresight vector.

    Args:
        utc (str): date and time at which moon boresight angle will be found
        instr (str): instrument name on observer
        N.B. observer extracted from instrument frame information

    Returns:
        float: moon boresight angle
    """


    et = sp.str2et(utc)
    abcorr = 'NONE'

    # # # # # PART 1: FRAME AND BORESIGHT VECTOR # # # # #

    # Get instrument reference frame, and boresight vector in that frame
    frame, bsight = sp.getfov(sp.bodn2c(instr),99,99,99)[1:3]

    # # # # # PART 2: POSITION VECTOR FROM TARGET TO MOON IN INSTRUMENT FRAME # # # # #

    # Get frame ID from kernel pool e.g. FRAME_ASP_SLIT1 = -1999301, and
    # convert to target ID of frame e.g. FRAME_-1999301_CENTER = -1999
    frameID  = sp.gipool(f"FRAME_{frame}",0,1)[0]
    targetID = sp.gipool(f"FRAME_{frameID}_CENTER",0,1)[0]

    # Find position vector of Aspera wrt Moon in instrument frame
    starg, lt = sp.spkpos('MOON', et, frame, abcorr, f"{targetID}")

    # # # # # PART 3: MOON BORESIGHT ANGLE # # # # #

    # Return angle between vectors, converted to degrees
    return sp.vsep(starg, bsight) * sp.dpr()
