import os
from pathlib import Path
from ramangle_algorithm import ramangle
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
    rel_path = 'geometries/kernels/mk/aspera_mk.tm'

    mkfile = os.path.join(cwd, rel_path)
    sp.furnsh(mkfile)

    # Specify time of observation based on interval in kernel(s)
    utc = '2025 JUNE 01 00:00:01'
    instr1 = 'ASP_SLIT_1'
    instr2 = 'ASP_SLIT_2'
    ram_angle1 = ramangle(utc, instr1)
    ram_angle2 = ramangle(utc, instr2)

    print('RAM ANGLE (DEG) - slit 1: ' + str(ram_angle1))
    print('RAM ANGLE (DEG) - slit 2: ' + str(ram_angle2))

    sp.unload(mkfile)

if __name__ == "__main__":
    main()
