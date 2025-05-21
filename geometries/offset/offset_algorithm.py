import spiceypy as sp

def offset(utc, instr, galaxy_targ):
    """ Calculates angle offset between boresight vector and
    vector to galaxy target

    Args:
        utc (str): date and time at which altitude will be found
        instr (str): instrument from which to extract frame & boresight
        galaxy_targ (str): name of the galaxy

    Returns:
        float: angle between galaxy vector and boresight vector in degrees
    """

    # # # # # PART 1: RETRIEVE ASPERA BORESIGHT VECTOR AND GALAXY VECTOR # # # # #

    galaxy_id = sp.bodn2c(galaxy_targ)
    et = sp.str2et(utc)

    # get ASPERA's boresight vector
    ref,vbore = sp.getfov(sp.bods2c(instr),99,99,99)[1:3]

    # convert to J2000
    rotation_matrix = sp.pxform(ref, 'J2000', et)
    vboreJ2K = sp.mxv(rotation_matrix, vbore)

    # get galaxy vector
    glx_vec = sp.gdpool(f"SITE{galaxy_id}_XYZ", 0, 3)

    # # # # # PART 2: FIND ANGLE BETWEEN BORESIGHT VECTOR AND GALAXY VECTOR # # # # #

    angle = sp.vsep(vboreJ2K, glx_vec)
    # convert to degrees
    angle = sp.convrt(angle, 'RADIANS', 'DEGREES')

    return angle
