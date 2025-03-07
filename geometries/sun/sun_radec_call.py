import os
from pathlib import Path
from sun_radec_algorithm import sun_radec
import spiceypy as sp

def main():
    """Tests sun_radec_algorithm.py using ephemeris data specified by the user.

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

    # Call algorithm
    [sun_ra, sun_dec] = sun_radec(utc, target)
    print('RA (DEG): ' + str(sun_ra))
    print('DEC (DEG): ' + str(sun_dec))

    sp.unload(mkfile)

if __name__ == "__main__":
    main()
