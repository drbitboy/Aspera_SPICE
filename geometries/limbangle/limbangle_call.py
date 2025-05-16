import os
from pathlib import Path
from limbangle_algorithm import limbangle, limbangle_instr
import spiceypy as sp

def main():
    """Tests limbangle_algorithm.py using ephemeris data specified by the user.

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
    utc = '2025-06-01T00:00:01' # sp.et2utc(et, 'C', 3) # '2025 JUNE 01 00:00:01'
    target = 'ASPERA'
    instr1 = 'ASP_SLIT_1'
    instr2 = 'ASP_SLIT_2'

    galaxy_targ = '9999000'
    # limb = limbangle(utc, target, galaxy_targ)
    limb_instr1 = limbangle_instr(utc, target, instr1)
    limb_instr2 = limbangle_instr(utc, target, instr2)
    # print('LIMB ANGLE (DEG) (GALAXY_TARG): ' + str(limb))
    print('LIMB ANGLE (DEG) (slit1): ' + str(limb_instr1))
    print('LIMB ANGLE (DEG) (slit2): ' + str(limb_instr2))

    sp.unload(mkfile)

if __name__ == "__main__":
    main()
