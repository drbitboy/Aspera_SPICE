import os
from pathlib import Path
from beta0_algorithm import beta0
import spiceypy as sp
from pytest import approx

def main():
    """Tests beta0_algorithm.py using ephemeris data specified by the user.

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
    beta0_angle = beta0(utc,target)
    print( 'BETA_0 ANGLE (DEG): ' + str(beta0_angle))

    sp.unload(mkfile)

    assert approx(beta0_angle,rel=1e-14) == 66.15082727879638

if __name__ == "__main__":
    main()
def test_pytest_main(): main()
