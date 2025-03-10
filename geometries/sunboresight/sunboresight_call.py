import os
from pathlib import Path
from sunboresight_algorithm import sunboresight_instr
import spiceypy as sp

def main():
    """Tests sunboresight_algorithm.py using ephemeris data specified by the user.

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

    sunboresight_angle = sunboresight_instr(utc, instr)
    print('SUN BORESIGHT ANGLE (DEG): ' + str(sunboresight_angle))

    sp.unload(mkfile)

if __name__ == "__main__":
    main()
