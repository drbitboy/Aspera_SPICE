import spiceypy as sp

def sunboresight_instr(utc, instr):
    """Calculates the angle between the Sun's unit vector wrt Aspera as seen from Aspera and the
    boresight vector.

    Args:
        utc (str): date and time at which altitude will be found
        instr (str): instrument name on Aspera

    Returns:
        float: sun-boresight angle
    """

    # # # # # PART 1: INSTRUMENT FRAME AND BORESIGHT VECTOR, AND OBSERVER THAT HAS INSTRUMENT # # # # #

    frame, bsight = sp.getfov(sp.bodn2c(instr),99,99,99)[1:3]
    observer = sp.bodc2s(sp.frinfo(sp.namfrm(frame))[0])

    # # # # # PART 2: POSITION VECTOR FROM ASPERA TO SUN IN INSTRUMENT FRAME # # # # #

    et = sp.str2et(utc)
    abcorr = 'NONE'
    pos, lt = sp.spkpos('SUN', et, frame, abcorr, observer)

    # # # # # PART 3: SUN-BORESIGHT ANGLE # # # # #

    # Calculate angle between position vectors
    sb_rad = sp.vsep(pos, bsight)
    sb_deg = sp.convrt(sb_rad, 'RADIANS', 'DEGREES')

    return sb_deg

    #btc alternative:  return sp.vsep(pos, bsight) * sp.dpr()
