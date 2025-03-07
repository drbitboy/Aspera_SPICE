import spiceypy as sp

def vel_sc_los(utc, target, galaxy_targ, instr):
    """S/C LOS velocity wrt boresight direction due to S/C orbit around Earth. Should be positive
    when S/C and target are receding from each other, and negative otherwise.

    Args:
        utc (str): date and time at which S/C LOS velocity will be found
        target (str): S/C name
        galaxy_targ (str): body ID for galaxy contained in mkfile
        instr (str): slit name of S/C

    Returns:
        tuple: S/C LOS velocity
    """

    # # # # # PART 1: UNIT VECTOR (DIRECTION) OF BORESIGHT # # # # #

    et = sp.utc2et(utc)
    ref = 'J2000'
    abcorr = 'NONE'
    instr_id = sp.bodn2c(instr)
    galaxy_targ_id = int(galaxy_targ)
    target_id = sp.bodn2c(target)

    # Generate boresight vector of slit
    fov_slit = sp.getfov(instr_id, 4, 32, 32)
    bsight_slit = fov_slit[2]

    # # # # # PART 2: VELOCITY VECTOR FROM S/C POINT SOURCE TO GALAXY # # # # #

    # Generate state vectors from S/C to galaxy target; extract velocity vector
    [starg, lt] = sp.spkez(galaxy_targ_id, et, ref, abcorr, target_id)
    vel_sc = starg[3:6]

    # # # # # PART 3: VELOCITY COMPONENT WRT BORESIGHT DIRECTION # # # # #

    # Velocity vector dot boresight direction = speed wrt boresight
    vel_mag = sp.vdot(vel_sc, bsight_slit) / sp.vnorm(bsight_slit)

    # Direction along which velocity component acts
    vel_vector = sp.vscl(vel_mag, bsight_slit)

    return vel_mag
