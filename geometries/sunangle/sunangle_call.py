import os
from pathlib import Path
from sunangle_algorithm import sunangle
import spiceypy as sp
from pytest import approx

def main():
    """Tests sunangle_algorithm.py using ephemeris data specified by the user.

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
    instrs = ['ASP_SLIT_1', 'ASP_SLIT_2', 'ASP_SOLAR']

    # Calculate sun boresight angle for each spacecraft instrument
    sb_list = list()
    for i in range(len(instrs)):

        sb_angle = sunangle(utc, instrs[i])
        sb_list.append(sb_angle)

        # Display sun boresight angle corresponding to each instrument
        print('\n' + instrs[i])
        print('SUN ANGLE (DEG): ' + str(sb_angle))

    sp.unload(mkfile)

    tsb_list = [67.658398353093, 67.6583983516552, 22.34518861180846]

    assert len(sb_list) == len(tsb_list)
    while sb_list:
        assert approx(sb_list.pop(), rel=1e-14) == tsb_list.pop()

def test_pytest_main(): main()


if __name__ == "__main__":
    main()
def test_pytest_main(): main()
