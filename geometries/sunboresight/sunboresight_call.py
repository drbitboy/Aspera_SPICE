import os
from pathlib import Path
from sunboresight_algorithm import sunboresight_instr
import spiceypy as sp
from pytest import approx

def main():
    """Tests sunboresight_algorithm.py using ephemeris data specified by the user.

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
    instr1 = 'ASP_SLIT_1'
    instr2 = 'ASP_SLIT_2'

    sunboresight_angle1 = sunboresight_instr(utc, instr1)
    sunboresight_angle2 = sunboresight_instr(utc, instr2)

    print('SUN BORESIGHT ANGLE (DEG) - slit 1: ' + str(sunboresight_angle1))
    print('SUN BORESIGHT ANGLE (DEG) - slit 2: ' + str(sunboresight_angle2))

    sp.unload(mkfile)

    tsunboresight_angle1 = 67.65839835309303
    tsunboresight_angle2 = 67.65839835165521

    assert approx(sunboresight_angle1,rel=1e-14) == tsunboresight_angle1
    assert approx(sunboresight_angle2,rel=1e-14) == tsunboresight_angle2

if __name__ == "__main__":
    main()
def test_pytest_main(): main()
