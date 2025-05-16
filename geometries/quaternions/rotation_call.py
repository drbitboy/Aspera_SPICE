import os
from pathlib import Path
from rotation_algorithm import rotation_matrix_sclk, make_quart
import spiceypy as sp

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

    cmat = rotation_matrix_sclk(sclk, target)
    qtr = make_quart(cmat[0])
    #print('MOON BORESIGHT ANGLE (DEG): ', moonboresight_angle)
    
    print(cmat[0])
    print(cmat[1])
    print(qtr)


    sp.unload(mkfile)

if __name__ == "__main__":
    main()
