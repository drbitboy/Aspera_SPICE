import spiceypy as sp

def sun_radec(utc, target):
    """Calculates the Sun's right ascension and declination.

    Args:
        mkfile (str): metakernel containg data on Aspera, nearby bodies, and M82
        utc (str): date and time at which right ascension and declination will be found

    Returns:
        float: Sun's right ascension and declination
    """

    et = sp.str2et(utc)
    ref = 'J2000'
    abcorr = 'NONE'

    # Generate position vector of Sun wrt Aspera
    starg, lt = sp.spkezr('SUN', et, ref, abcorr, target)
    pos = starg[0:3]

    # Find right ascension and declination of Sun
    [range, ra_rad, dec_rad] = sp.recrad(pos)

    ra_deg = sp.convrt(ra_rad, 'RADIANS', 'DEGREES')
    dec_deg = sp.convrt(dec_rad, 'RADIANS', 'DEGREES')

    return ra_deg, dec_deg
