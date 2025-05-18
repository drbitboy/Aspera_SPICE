import os
from pathlib import Path
from altitude_algorithm import altitude
import spiceypy as sp
from pytest import approx

def main():
    """Tests altitude_algorithm.py using ephemeris data specified by the user.

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
    alt = altitude(utc,target)
    print('ALTITUDE (KM): ' + str(alt))

    sp.unload(mkfile)

    assert approx(alt,rel=1e-14) == 6965.796879326453

if __name__ == "__main__":
    main()
def test_pytest_main(): main()
