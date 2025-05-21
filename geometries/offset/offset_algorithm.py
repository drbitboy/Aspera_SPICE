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

    # # # # # PART 0: RETRIEVE ASPERA BORESIGHT VECTOR AND GALAXY VECTOR # # # # #
    # # # # #         - N.B. BOTH VECTORS WILL BE IN INSTRUMENT FRAME    # # # # #

    et = sp.str2et(utc)

    # Instrument => Instrument ID => Reference Frame Name and boresight
    # => Reference frame ID => Spacecraft ID => Spacecraft name (bodc2s)
    # => Vector to galaxy from spacecraft
    ref,vbore = sp.getfov(sp.bods2c(instr),99,99,99)[1:3]
    refID  = sp.gipool(f"FRAME_{ref}",0,1)[0]
    scID = sp.gipool(f"FRAME_{refID}_CENTER",0,1)[0]
    glx_vec = sp.spkezr(galaxy_targ, et, ref, 'NONE', sp.bodc2s(scID))[0][:3]

    # Angle btw thse vectors in instrument reference frame, degrees
    return sp.convrt(sp.vsep(vbore, glx_vec), 'RADIANS', 'DEGREES')
