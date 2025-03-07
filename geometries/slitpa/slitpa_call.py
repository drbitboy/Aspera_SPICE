import os
from pathlib import Path
from slitpa_algorithm import slitpa
import spiceypy as sp

def main():
    """Tests slitpa_algorithm.py using ephemeris data specified by the user.

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
    utc = '2025 JUNE 01 00:01:00'
    instr1 = 'ASP_SLIT1'
    instr2 = 'ASP_SLIT2'

        # Find angle for given slit
    slitpa_deg1 = slitpa(utc, instr1)
    slitpa_deg2 = slitpa(utc, instr2)

    # Display angles corresponding to each slit
    print('SLIT1 POSITION ANGLE EAST OF NORTH (DEG): ' + str(slitpa_deg1))
    print('SLIT2 POSITION ANGLE EAST OF NORTH (DEG): ' + str(slitpa_deg2))

    sp.unload(mkfile)

if __name__ == "__main__":
    main()
