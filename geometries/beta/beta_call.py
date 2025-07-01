import os
from pathlib import Path
from beta_algorithm import beta
import spiceypy as sp
from pytest import approx

def main():
    """Tests beta_algorithm.py using ephemeris data specified by the user.

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
    ptarg1, ptarg2, beta_angle = beta(utc, target)

    print("At UTC " + utc + ": \n")
    print("Aspera's cartesian position wrt Earth in J2000 frame (km):\n" + str(ptarg1) + "\n")
    print("Aspera's cartesian position wrt Sun in J2000 frame (km): \n" + str(ptarg2) + "\n")
    print("Aspera's beta angle (degrees): \n" + str(beta_angle))

    sp.unload(mkfile)

    ttarg1 = sp.vpack(5555.06833931, 2735.06203789, -3191.07780516)
    ttarg2 = sp.vpack(-5.08247326e+07, -1.31124653e+08, -5.68445794e+07)
    tbeta_angle = 115.78237271627174
    assert (sp.vnorm(sp.vsub(ptarg1, ttarg1)) / sp.vnorm(ptarg1)) < 1e-12
    assert (sp.vnorm(sp.vsub(ptarg2, ttarg2)) / sp.vnorm(ptarg2)) < 1e-8
    assert approx(tbeta_angle,rel=1e-14) == beta_angle

if __name__ == "__main__":
    main()
def test_pytest_main(): main()
