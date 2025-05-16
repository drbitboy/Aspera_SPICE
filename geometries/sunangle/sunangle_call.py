import os
from pathlib import Path
from sunangle_algorithm import sunangle
import spiceypy as sp

def main():
    """Tests sunangle_algorithm.py using ephemeris data specified by the user.

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
    instrs = ['ASP_SLIT_1', 'ASP_SLIT_2', 'ASP_SOLAR']

    # Calculate sun boresight angle for each spacecraft instrument
    for i in range(len(instrs)):

        sb_angle = sunangle(utc, instrs[i])

        # Display sun boresight angle corresponding to each instrument
        print('\n' + instrs[i])
        print('SUN ANGLE (DEG): ' + str(sb_angle))

    sp.unload(mkfile)

if __name__ == "__main__":
    main()
