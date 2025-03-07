import os
from pathlib import Path
import spiceypy as sp

def obsgeo(utc, sc, targ):
    """X, Y, and Z coordinates of the S/C wrt Earth center.

    Args:
        utc (str): date and time at which S/C position will be found
        sc (str): S/C name
        targ (str): planet name

    Returns:
        tuple: S/C position
    """
    
    et = sp.utc2et(utc)
    ref = 'J2000'
    abcorr = 'NONE'
    sc_id = sp.bodn2c(sc)
    planet_id = sp.bodn2c(targ)

    # Generate state vectors from Earth to S/C; extract position vector
    [starg, lt] = sp.spkez(sc_id, et, ref, abcorr, planet_id)
    pos_sc = starg[0:3]

    return pos_sc