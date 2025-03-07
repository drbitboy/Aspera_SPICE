import os
from pathlib import Path
import spiceypy as sp

def vel_earth_los(utc, galaxy_targ):
    """Earth LOS velocity wrt target due to Earth's orbit around Sun. Should be positive when Earth and
    target are receding from each other, and negative otherwise.

    Args:
        utc (str): date and time at which Earth LOS velocity will be found
        galaxy_targ (str): body ID for galaxy contained in mkfile

    Returns:
        tuple: EARTH LOS velocity
    """
    
    et = sp.utc2et(utc)
    ref = 'J2000'
    abcorr = 'NONE'
    galaxy_targ_id = int(galaxy_targ)

    # Generate state vectors from Sun to Earth; extract velocity vector
    [state_earth_sun, lt] = sp.spkez(399, et, ref, abcorr, 10)
    v_earth = state_earth_sun[3:6]

    # Generate state vectors from galaxy to Earth; extract position vector
    [state_earth_galaxy, lt] = sp.spkez(399, et, ref, abcorr, galaxy_targ_id)
    t = state_earth_galaxy[0:3]
    
    v_los = -(sp.vdot(v_earth, t) / sp.vnorm(t))

    return v_los