import spiceypy as sp

def latlon(utc,target):
    """Calculates the latitude, longitude, right ascension, and declination of Aspera wrt Earth.

    Args:
        mkfile (str): metakernel containg data on Aspera, nearby bodies, and M82
        utc (str): date and time at which beta0 angle will be found

    Returns:
        float: latitude, Earth frame (IAU_EARTH)
        float: longitude, Earth frame
        float: right ascension, Inertial J2000 frame (J2000)
        float: declination, Inertial J2000 frame
    """

    # # # # # PART 1: FIND POSITION VECTOR FROM EARTH -> ASPERA # # # # #

    et = sp.str2et(utc)
    ref_J2000 = 'J2000'
    ref_EARTH = 'IAU_EARTH'
    abcorr = 'NONE'

    [pos_J2000, lt] = sp.spkpos(target, et, ref_J2000, abcorr, 'EARTH')
    [pos_EARTH, lt] = sp.spkpos(target, et, ref_EARTH, abcorr, 'EARTH')

    # # # # # PART 2: FIND LAT/LON OF ASPERA WRT EARTH # # # # #

    [radius, lon_rad, lat_rad] = sp.reclat(pos_EARTH)
    lon_deg = sp.convrt(lon_rad, 'RADIANS', 'DEGREES')
    lat_deg = sp.convrt(lat_rad, 'RADIANS', 'DEGREES')

    # # # # # PART 3: FIND RA/DEC OF ASPERA WRT J2000 # # # # #

    [radius, ra_rad, dec_rad] = sp.recrad(pos_J2000) #btc keep range()
    ra_deg = sp.convrt(ra_rad, 'RADIANS', 'DEGREES')
    dec_deg = sp.convrt(dec_rad, 'RADIANS', 'DEGREES')

    return lat_deg, lon_deg, ra_deg, dec_deg
