# Calculates Aspera's altitude wrt center of gravity of Earth

import spiceypy as sp

def altitude(utc,target):

    """Calculates Aspera's altitude wrt Earth's center of gravity.
        
        Args:
            mkfile (str): metakernel containg data on Aspera, nearby bodies, and M82
            utc (str): date and time at which altitude will be found
        Returns:
            float: Aspera's altitude
        """
        
    et = sp.str2et(utc)
    ref = 'J2000'
    abcorr = 'NONE'

    # Generate position vector of Aspera
    ptarg, lt = sp.spkpos(target, et, ref, abcorr, 'EARTH')

    # Find mangitude of position vector (altitude)
    alt = sp.vnorm(ptarg)
    
    return alt