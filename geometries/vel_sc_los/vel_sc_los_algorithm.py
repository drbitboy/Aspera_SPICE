import spiceypy as sp

def vel_sc_los(utc, instr):
    """S/C LOS velocity wrt boresight direction due to S/C orbit around
    Earth. Should be positive when S/C and target are receding from each
    other, and negative otherwise.

    Args:
        utc (str): date and time at which S/C LOS velocity will be found
        instr (str): instrument name

    Returns:
        float: S/C LOS velocity
    """

    # # # # # PART o: INSTRUMENT FRAME AND BORESIGHT VECTOR, AND OBSERVER THAT HAS INSTRUMENT # # # # #

    ref, bsight = sp.getfov(sp.bodn2c(instr),99,99,99)[1:3]
    obs = sp.bodc2s(sp.frinfo(sp.namfrm(ref))[0])  #btc frame center

    # # # # # PART 2: VELOCITY VECTOR FROM S/C WRT EARTH IN INSTRUMENT FRAME # # # # #

    #btc [0] = state wrt Earth in instrument frame; [3:] = S/C velocity
    vel_sc = sp.spkezr(obs, sp.utc2et(utc), ref, 'NONE', 'EARTH')[0][3:]

    # # # # # PART 3: VELOCITY COMPONENT WRT BORESIGHT DIRECTION # # # # #

    # Velocity vector dot boresight unit vector => speed along boresight
    vel_mag = sp.vdot(vel_sc, sp.vhat(bsight))

    #btc Invert sign so when S/C velocity is opposite boresight,
    #btc i.e. S/C receding from target to which boresight is pointing,
    #btc then negative dot product will result in positive return value
    return -vel_mag
