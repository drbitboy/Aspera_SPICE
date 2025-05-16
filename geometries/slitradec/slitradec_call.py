import os
from pathlib import Path
from slitradec_algorithm import slitradec
import spiceypy as sp

def main():
    """Tests slitradec_algorithm.py using ephemeris data specified by the user.

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
    utc = '2025 JUNE 01 00:01:00'
    instrs = ['ASP_SLIT_1', 'ASP_SLIT_2', 'ASP_SOLAR']

    # Calculate right ascension and declination for each spacecraft instrument
    for i in range(len(instrs)):

        [ra, dec, asp_ra, asp_dec] = slitradec(utc, instrs[i]) # originally just [ra, dec] = ...

        # Display right ascension and declination corresponding to each instrument
        print('\n' + instrs[i])
        print('RA (DEG): ' + str(ra))
        print('DEC (DEG): ' + str(dec))

        print(str(asp_ra) + '\n' + str(asp_dec))

    print()
    sp.unload(mkfile)

if __name__ == "__main__":
    main()
