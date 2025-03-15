import os
from pathlib import Path
from vel_earth_los_algorithm import vel_earth_los
import spiceypy as sp

def main():
    """Tests vel_earth_los_algorithm.py using ephemeris data specified by the user.

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

    vel_los = vel_earth_los(utc, 'ASP_SLIT_0')
    print('\nEARTH LOS VELOCITY: (KM/S)')
    print(vel_los)
    print()

    sp.unload(mkfile)

if __name__ == "__main__":
    main()
