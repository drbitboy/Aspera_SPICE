import os
from pathlib import Path
from sun_radec_algorithm import sun_radec
import spiceypy as sp
from pytest import approx

def main():
    """Tests sun_radec_algorithm.py using ephemeris data specified by the user.

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
    [sun_ra, sun_dec] = sun_radec(utc, target)
    print('RA (DEG): ' + str(sun_ra))
    print('DEC (DEG): ' + str(sun_dec))

    sp.unload(mkfile)

    tsun_ra = 68.81335865587167
    tsun_dec = 22.00922025779235

    assert approx(sun_ra, rel=1e-14) == tsun_ra
    assert approx(sun_dec, rel=1e-14) == tsun_dec

if __name__ == "__main__":
    main()
def test_pytest_main(): main()
