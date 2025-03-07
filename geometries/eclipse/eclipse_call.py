import os
from pathlib import Path
from eclipse_algorithm import eclipse
import spiceypy as sp
# import spiceypy.utils.support_types as stypes

def main():
    """Tests eclipse_algorithm.py using ephemeris data specified by the user.

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
    eclipsed_sun = eclipse(utc, 'SUN', target)
    eclipsed_moon = eclipse(utc, 'MOON', target)
    
    print("At UTC " + utc + ": \n")
    print("Aspera eclipse status (Sun): \n" + eclipsed_sun + "\n")
    print("Aspera eclipse status (Moon): \n" + eclipsed_moon)

    sp.unload(mkfile)

if __name__ == "__main__":
    main()
