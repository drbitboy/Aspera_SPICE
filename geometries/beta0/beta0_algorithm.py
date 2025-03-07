import math as m
import spiceypy as sp

def beta0(utc,target):
    """Calculates beta0 angle, under which the outer edge of the Sun would be seen under grazing
    incident from the spacecraft.

    Args:
        mkfile (str): metakernel containg data on Aspera, nearby bodies, and M82
        utc (str): date and time at which beta0 angle will be found

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

    # find mangitude of Aspera's position vector wrt Earth
    r_vec, lt = sp.spkpos(target, et, ref, abcorr, 'EARTH')
    r = sp.vnorm(r_vec)

    # # # # # PART 3: SUN RADIUS # # # # #

    # same process as part 1, Sun's body ID is 10
    [sun_dim, sun_vals] = sp.bodvrd('SUN', 'RADII', 3)
    rs = (1/3) * (sun_vals[0] + sun_vals[1] + sun_vals[2])

    # # # # # PART 4: DISTANCE BETWEEN EARTH AND THE SUN # # # # #

    # same process as part 2
    d_vec, lt = sp.spkpos('SUN', et, ref, abcorr, 'EARTH')
    d = sp.vnorm(d_vec)

    # # # # # PART 5: BETA_0 # # # # #

    # final beta0 angle from rad to deg
    beta0_rad = m.asin(re/r) + m.asin(rs/d)
    beta0_deg = sp.convrt(beta0_rad, 'RADIANS', 'DEGREES')

    return beta0_deg
