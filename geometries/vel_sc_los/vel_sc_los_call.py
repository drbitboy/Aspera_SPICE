import os
from pathlib import Path
from vel_sc_los_algorithm import vel_sc_los
import spiceypy as sp

def main():
    """Tests vel_sc_los_algorithm.py using ephemeris data specified by the user.

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

    slits = [['ASP_SLIT_0', -1999301], ['ASP_SLIT_1', -1999302]]

    for instr_name,instr_id in slits:

        # Find velocity vector for given slit
        vel = vel_sc_los(utc, instr_name)

        # Display vectors corresponding to each slit
        print('\n' + instr_name)
        print('SPACECRAFT LOS VELOCITY:')
        print(vel)

    print()
    sp.unload(mkfile)

if __name__ == "__main__":
    main()
