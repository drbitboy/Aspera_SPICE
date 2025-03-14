import spiceypy as sp

def vel_earth_los(utc, instr):
    """Earth LOS velocity wrt, and against, boresight due to Earth's
    orbit around Sun. Should be negative when Earth is moving toward
    boresight i.e. target side of image plane, be positive when Earth is
    receding from boresight side of image plane, and zero when Earth is
    moving within image plane

    Args:
        utc (str): date and time at which Earth LOS velocity is found
        instr (str): instrument name e.g. ASP_SLIT_0 or ASP_SLIT_0

    Returns:
        tuple: EARTH LOS velocity
    """

    # # # # # PART 1: INSTRUMENT FRAME AND BORESIGHT VECTOR # # # # #

    ref, bsight = sp.getfov(sp.bodn2c(instr),99,99,99)[1:3]
    
    # # # # # PART 2: EARTH VELOCITY WRT SUN IN INSTRUMENT FRAME # # # # #

    et = sp.utc2et(utc)
    abcorr = 'NONE'

    earth_state, lt = sp.spkezr('EARTH', et, ref, abcorr, 'SUN')
    v_earth = earth_state[3:]

    # # # # # PART 3: VELOCITY OF EARTH AGAINST BORESIGHT # # # # #

    #btc Sun-relative Earth velocity vector dotted with boresight gives
    #btc negative value when Earth is receding from "target" i.e. when
    #btc Earth projection onto boresight-fixed-wrt-Sun is moving
    #btc backwards along boresight vector, so inverted sign to return
    #btc positive value for that case as required in specification
    v_los = sp.vdot(v_earth, sp.vhat(bsight))

    return -v_los
