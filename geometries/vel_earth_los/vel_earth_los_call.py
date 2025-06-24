import os
from pathlib import Path
from vel_earth_los_algorithm import vel_earth_los
import spiceypy as sp
from pytest import approx

def main():
    """Tests vel_earth_los_algorithm.py using ephemeris data specified by the user.

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

    vel_los1 = vel_earth_los(utc, 'ASP_SLIT_1')
    vel_los2 = vel_earth_los(utc, 'ASP_SLIT_2')
    print('\nEARTH LOS VELOCITY - slit 1: (KM/S)')
    print(vel_los1)
    print()
    print('\nEARTH LOS VELOCITY - slit 2: (KM/S)')
    print(vel_los2)
    print()

    sp.unload(mkfile)

    tvel_los1 = -8.779013226625448
    tvel_los2 = -7.8037293763198505

    assert approx(tvel_los1,rel=1e-14) == vel_los1
    assert approx(tvel_los2,rel=1e-14) == vel_los2

if __name__ == "__main__":
    main()
def test_pytest_main(): main()
