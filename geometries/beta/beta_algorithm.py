import math as m
import spiceypy as sp

def beta(utc, Target):
    """Calculates beta angle, which is measured between Aspera position vector wrt Earth & Aspera
    position vector wrt Sun.

    Args:
        mkfile (str): metakernel containing data on Aspera, nearby bodies, and M82 #btc fix typo
        utc (str): date and time at which beta angle will be found

    Returns:
        numpy.ndarray: Aspera's cartesian position wrt Earth
        numpy.ndarray: Aspera's cartesian position wrt Sun
        float64:       Value of beta angle  #btc add description of third returned element
    """

    et = sp.str2et(utc)
    ref = 'J2000'
    abcorr = 'NONE'

    # Generate position vector of Aspera wrt Earth
    ptarg1, lt1 = sp.spkpos(Target, et, ref, abcorr, 'EARTH')

    # Generate position vector of Aspera wrt Sun
    ptarg2, lt2 = sp.spkpos(Target, et, ref, abcorr, 'SUN')

    # Use Aspera's position vectors to find beta angle, convert rad -> deg
    beta_rad = sp.vsep(ptarg1, ptarg2)  #btc remove intermediate var
    beta_deg = beta_rad*(180/m.pi)      #btc = sp.vsep(...) * sp.dpr()

    return ptarg1, ptarg2, beta_deg
