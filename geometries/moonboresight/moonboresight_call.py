import os
from pathlib import Path
from moonboresight_algorithm import moonboresight, moonboresight_instr
import spiceypy as sp

def main():
    """Tests moonboresight_algorithm.py using ephemeris data specified by the user.

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
    instr1 = 'ASP_SLIT1'
    instr2 = 'ASP_SLIT2'

    galaxy_targ = '9999000'
    # moonboresight_angle = moonboresight(utc, target, galaxy_targ)
    moonboresight1 = moonboresight_instr(utc, target, instr1)
    moonboresight2 = moonboresight_instr(utc, target, instr2)
    print('MOON BORESIGHT ANGLE (DEG) (slit1): ', moonboresight1)
    print('MOON BORESIGHT ANGLE (DEG) (slit2): ', moonboresight2)

    sp.unload(mkfile)

if __name__ == "__main__":
    main()
