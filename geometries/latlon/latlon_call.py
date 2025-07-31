import os
from pathlib import Path
from latlon_algorithm import latlon
import spiceypy as sp
from pytest import approx

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

    tlat = -27.13690775124862
    tlon = 136.77099728886716
    tra  =  26.213529553706564
    tdec = -27.264999787177263

    assert approx(lat, rel=1e-14) == tlat
    assert approx(lon, rel=1e-14) == tlon
    assert approx(ra, rel=1e-14) == tra
    assert approx(dec, rel=1e-14) == tdec

if __name__ == "__main__":
    main()
def test_pytest_main(): main()
