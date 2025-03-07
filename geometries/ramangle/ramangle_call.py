import os
from pathlib import Path
from ramangle_algorithm import ramangle, ramangle_instr
import spiceypy as sp

def main():
    """Tests ramangle_algorithm.py using ephemeris data specified by the user.

    Args:
        None

    Returns:
        None
    """

    # Find location of kernel & furnish it
    cwd = Path.cwd()
    rel_path = 'geometries/kernels/mk/asperaMetaKernelM82.tm'

    mkfile = os.path.join(cwd, rel_path)
    sp.furnsh(mkfile)

    # Specify time of observation based on interval in kernel(s)
    utc = '2025 JUNE 01 00:00:01'
    target = 'ASPERA'
    instr = 'ASP_SLIT1'

    galaxy_targ = '9999000'
    [ram_angle, vel_sc_los] = ramangle(utc, target, galaxy_targ)
    [ra, dec] = ramangle_instr(utc, target, instr)

    # print('RAM ANGLE (DEG): ' + str(ram_angle))
    # print('S/C VELOCITY WRT TARGET (KM/S): ' + str(vel_sc_los))
    print('RAM ANGLE (DEG): ' + str(ra))
    print('S/C VELOCITY WRT TARGET (KM/S): ' + str(dec))

    sp.unload(mkfile)

if __name__ == "__main__":
    main()
