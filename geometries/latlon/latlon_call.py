import os
from pathlib import Path
from latlon_algorithm import latlon
import spiceypy as sp

def main():
    """Tests latlon_algorithm.py using ephemeris data specified by the user.

    Args:
        None

    Returns:
        None
    """

    # Find location of kernel & furnish it
    cwd = Path.cwd()
    rel_path = 'geometries/kernels/mk/aspera_mk.tm'

    mkfile = os.path.join(cwd, rel_path)
    sp.furnsh(mkfile)

    # Specify time of observation based on interval in kernel(s)
    utc = '2025 JUNE 01 00:00:01'
    target = 'ASPERA'

    # Call algorithm
    [lat, lon, ra, dec] = latlon(utc,target)
    print('LATITUDE (DEG): ' + str(lat))
    print('LONGITUDE (DEG): ' + str(lon))
    print('RA (DEG): ' + str(ra))
    print('DEC (DEG): ' + str(dec))

    sp.unload(mkfile)

if __name__ == "__main__":
    main()
