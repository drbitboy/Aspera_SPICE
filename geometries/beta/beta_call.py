import os
from pathlib import Path
from beta_algorithm import beta
import spiceypy as sp

def main():
    """Tests beta_algorithm.py using ephemeris data specified by the user.

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
    target = 'ASPERA'

    # Call algorithm
    ptarg1, ptarg2, beta_angle = beta(utc, target)

    print("At UTC " + utc + ": \n")
    print("Aspera's cartesian position wrt Earth in J2000 frame (km):\n" + str(ptarg1) + "\n")
    print("Aspera's cartesian position wrt Sun in J2000 frame (km): \n" + str(ptarg2) + "\n")
    print("Aspera's beta angle (degrees): \n" + str(beta_angle))

    sp.unload(mkfile)

if __name__ == "__main__":
    main()
