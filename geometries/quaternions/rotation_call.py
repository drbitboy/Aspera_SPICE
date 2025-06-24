import os
from pathlib import Path
from rotation_algorithm import rotation_matrix_sclk, make_quart
import spiceypy as sp
from pytest import approx

def main():
    """
    """

    # Find location of kernel & furnish it
    cwd = Path.cwd()
    #rel_path = 'geometries/kernels/mk/aspera_mk.tm'
    rel_path = 'geometries/kernels/mk/aspera_mk.tm'

    mkfile = os.path.join(cwd, rel_path)
    #mkfile = os.path.join(cwd, rel_path_sval)
    sp.furnsh(mkfile)

    # Specify time of observation based on interval in kernel(s)
    sclk = 8020944700000.000000
    target = 'ASPERA'

    cmat,sclk = rotation_matrix_sclk(sclk, target)
    qtr = make_quart(cmat)
    #print('MOON BORESIGHT ANGLE (DEG): ', moonboresight_angle)
    
    print(cmat)
    print(sclk)
    print(qtr)

    sp.unload(mkfile)

    tsclk = 8020944700000.0
    tqtr = [0.28490427, -0.46964652, 0.79148418, -0.26798229]

    try   : assert (sp.vnormg(sp.vsubg(qtr, tqtr, 4), 4) / sp.vnormg(qtr, 4)) < 1e-7
    except: assert (sp.vnormg(sp.vsubg(qtr, tqtr)) / sp.vnormg(qtr)) < 1e-7
    assert approx(sclk, rel=1e-14) == tsclk

if __name__ == "__main__":
    main()
def test_pytest_main(): main()
