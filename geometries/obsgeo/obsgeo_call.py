import os
from pathlib import Path
from obsgeo_algorithm import obsgeo
import spiceypy as sp

def main():
    """Tests obsgeo_algorithm.py using ephemeris data specified by the user.

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
    sc = "ASPERA" #-1999
    targ = "EARTH" #399

    pos_sc = obsgeo(utc, sc, targ)

    print('\nOBSGEO-X: ', pos_sc[0])
    print('OBSGEO-Y: ', pos_sc[1])
    print('OBSGEO-Z: ', pos_sc[2])

    sp.unload(mkfile)

if __name__ == "__main__":
    main()