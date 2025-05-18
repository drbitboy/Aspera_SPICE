import os
from pathlib import Path
from moonboresight_algorithm import moonboresight, moonboresight_instr, moonboresight_instr_btc
import spiceypy as sp
from pytest import approx

def main():
    """Tests moonboresight_algorithm.py using ephemeris data specified by the user.

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

    galaxy_targ = '9999000'
    # moonboresight_angle = moonboresight(utc, target, galaxy_targ)
    moonboresight1 = moonboresight_instr(utc, target, instr1)
    moonboresight2 = moonboresight_instr(utc, target, instr2)
    print('MOON BORESIGHT ANGLE (DEG) (slit1): ', moonboresight1)
    print('MOON BORESIGHT ANGLE (DEG) (slit2): ', moonboresight2)

    moonboresight1_btc = moonboresight_instr_btc(utc, instr1)
    moonboresight2_btc = moonboresight_instr_btc(utc, instr2)
    print('MOON BORESIGHT ANGLE (DEG) (slit1): ', moonboresight1_btc)
    print('MOON BORESIGHT ANGLE (DEG) (slit2): ', moonboresight2_btc)

    sp.unload(mkfile)

    t1     = 99.97031141321129
    t2     = 98.26247448505372
    t1_btc = 99.97031141321128
    t2_btc = 98.26247448505369

    assert approx(moonboresight1, rel=1e-14) == t1
    assert approx(moonboresight2, rel=1e-14) == t2
    assert approx(moonboresight1_btc, rel=1e-14) == t1_btc
    assert approx(moonboresight2_btc, rel=1e-14) == t2_btc

if __name__ == "__main__":
    main()
def test_pytest_main(): main()
