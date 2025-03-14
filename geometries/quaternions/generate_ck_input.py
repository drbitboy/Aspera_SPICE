import os
from pathlib import Path
from rotation_algorithm import rotation_matrix_utc, make_quart
import spiceypy as sp

def main():
    """
    """

    # Find location of kernel & furnish it
    cwd = Path.cwd()
    rel_path = 'geometries/kernels/mk/asperaMetaKernel2.tm'

    mkfile = os.path.join(cwd, rel_path)
    sp.furnsh(mkfile)

    # Specify time of observation based on interval in kernel(s)
    utc = '2025-06-01T00:47:00'
    target = 'ASPERA'

    cmat = rotation_matrix_utc(utc, target)
    quat = make_quart(cmat[0])
    
    print(cmat)
    print(quat)

    sp.unload(mkfile)

if __name__ == "__main__":
    main()
