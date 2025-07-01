import os
from pathlib import Path
from vel_sc_los_algorithm import vel_sc_los
import spiceypy as sp
from pytest import approx

def main():
    """Tests vel_sc_los_algorithm.py using ephemeris data specified by the user.

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

    slits = [['ASP_SLIT_1', -1999301], ['ASP_SLIT_2', -1999302]]

    vel_list = list()
    for instr_name,instr_id in slits:

        # Find velocity vector for given slit
        vel = vel_sc_los(utc, instr_name)

        # Display vectors corresponding to each slit
        print('\n' + instr_name)
        print('SPACECRAFT LOS VELOCITY:')
        print(vel)
        vel_list.append(vel)

    print()
    sp.unload(mkfile)

    tvel_list = [-2.1100916504219764, -2.1900125489503894]

    assert len(tvel_list) == len(vel_list)

    while vel_list:
        assert approx(tvel_list.pop(),rel=1e-14) == vel_list.pop()

if __name__ == "__main__":
    main()
def test_pytest_main(): main()
