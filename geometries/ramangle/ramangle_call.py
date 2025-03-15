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
    rel_path = 'geometries/kernels/mk/asperaMetaKernelM82.tm'

    mkfile = os.path.join(cwd, rel_path)
    sp.furnsh(mkfile)

    # Specify time of observation based on interval in kernel(s)
    utc = '2025 JUNE 01 00:00:01'
    instr = 'ASP_SLIT_0'
    ram_angle = ramangle(utc, instr)

    print('RAM ANGLE (DEG): ' + str(ram_angle))

    sp.unload(mkfile)

if __name__ == "__main__":
    main()
