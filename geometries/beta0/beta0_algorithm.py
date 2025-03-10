import math as m
import spiceypy as sp

def beta0(utc,target):
    """Calculates beta0 angle, under which the center of the Sun would
    be seen from the spacecraft. grazing the Earth terminator

    Args: #btc removed obsolete regerence to mkfile argumen
        utc (str): date and time at which beta0 angle will be found
        target (str): SPICE name of spacecraft #btc added target argument

    Returns:
        float: beta0 angle
    """

    # # # # # PART 1: EARTH RADIUS # # # # #

    # find radius of Earth in 3 dims
    [earth_dim, earth_vals] = sp.bodvrd('EARTH', 'RADII', 3)

    # assume Earth is a perfect sphere - find average of radii vals
    re = (1/3) * (earth_vals[0] + earth_vals[1] + earth_vals[2])

    # # # # # PART 2: ASPERA ALTITUDE WRT EARTH CG # # # # #

    et = sp.str2et(utc)
    ref = 'J2000'
    abcorr = 'NONE'

    #btc could we use altitude_algorithm.py here?
    # find mangitude of Aspera's position vector wrt Earth
    r_vec, lt = sp.spkpos(target, et, ref, abcorr, 'EARTH')
    r = sp.vnorm(r_vec)

    # # # # # PART 2: BETA_0 # # # # #

    # final beta0 angle from rad to deg
    beta0_rad = m.asin(re/r)
    beta0_deg = sp.convrt(beta0_rad, 'RADIANS', 'DEGREES')

    return beta0_deg
