import os
from pathlib import Path
from slitradec_algorithm import slitradec
import spiceypy as sp
from pytest import approx

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

    rdaa_list = list()
    # Calculate right ascension and declination for each spacecraft instrument
    for i in range(len(instrs)):

        [ra, dec, asp_ra, asp_dec] = rdaa = slitradec(utc, instrs[i]) # originally just [ra, dec] = ...
        rdaa_list.append(rdaa)

        # Display right ascension and declination corresponding to each instrument
        print('\n' + instrs[i])
        print('RA (DEG): ' + str(ra))
        print('DEC (DEG): ' + str(dec))

        print(str(asp_ra) + '\n' + str(asp_dec))

    print()
    sp.unload(mkfile)

    trdaa_list = [(54.76335005323475, -44.41642688573398, 25.567286692163933, -30.892650679670027,)
                 ,(57.50525079113758, -44.85657130128589, 25.567286692163933, -30.892650679670027,)
                 ,(73.93155366469205, 43.94984722800049,  25.567286692163933, -30.892650679670027,)
                 ]

    assert len(rdaa_list) == len(rdaa_list)
    while rdaa_list:
        rdaa,trdaa = list(rdaa_list.pop()), list(trdaa_list.pop())
        assert len(rdaa) == len(trdaa)
        while rdaa: assert approx(rdaa.pop(), rel=1e-14) == trdaa.pop()

if __name__ == "__main__":
    main()
def test_pytest_main(): main()
