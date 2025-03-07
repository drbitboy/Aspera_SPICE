import spiceypy as sp

def sunboresight(utc, target, galaxy_targ):
    """Calculates the angle between the Sun's unit vector wrt Aspera as seen from Aspera and the
    boresight vector.

    Args:
        mkfile (str): metakernel containg data on Aspera, nearby bodies, and M82
        utc (str): date and time at which altitude will be found
        galaxy_targ (str): body ID for galaxy contained in mkfile

    Returns:
        float: sun boresight angle
    """

    # # # # # PART 1: POSITION VECTOR FROM ASPERA TO SUN # # # # #

    et = sp.str2et(utc)
    ref = 'J2000'
    abcorr = 'NONE'

    # Generate position vector of Aspera wrt Sun
    [sun_state, lt] = sp.spkpos('SUN', et, ref, abcorr, target)
    pos = sun_state[0:3]

    # # # # # PART 2: BORESIGHT VECTOR # # # # #

    # Find position vector of Aspera wrt galaxy
    [gtarg, lt] = sp.spkpos(galaxy_targ, et, ref, abcorr, target)

    # # # # # PART 3: SUN BORESIGHT ANGLE # # # # #

    # Calculate angle between position vectors
    sb_rad = sp.vsep(pos, gtarg)
    sb_deg = sp.convrt(sb_rad, 'RADIANS', 'DEGREES')

    return sb_deg

def sunboresight_instr(utc, target, instr):
    """Calculates the angle between the Sun's unit vector wrt Aspera as seen from Aspera and the
    boresight vector.

    Args:
        mkfile (str): metakernel containg data on Aspera, nearby bodies, and M82
        utc (str): date and time at which altitude will be found
        instr (str): instrument name on Aspera

    Returns:
        float: sun boresight angle
    """

    # # # # # PART 1: POSITION VECTOR FROM ASPERA TO SUN # # # # #

    et = sp.str2et(utc)
    ref = 'J2000'
    abcorr = 'NONE'

    # Generate position vector of Aspera wrt Sun
    [sun_state, lt] = sp.spkpos('SUN', et, ref, abcorr, target)
    pos = sun_state[0:3]

    # # # # # PART 2: BORESIGHT VECTOR # # # # #

    # Find Aspera's boresight vector in J2000
    instid = sp.bodn2c(instr)
    shape, frame, bsight, n, bounds = sp.getfov(instid,99,99,99)
    rotation_matrix = sp.pxform(frame, ref, et)
    vboreJ2k = sp.mxv(rotation_matrix,bsight)

    # # # # # PART 3: SUN BORESIGHT ANGLE # # # # #

    # Calculate angle between position vectors
    sb_rad = sp.vsep(pos, vboreJ2k)
    sb_deg = sp.convrt(sb_rad, 'RADIANS', 'DEGREES')

    return sb_deg
