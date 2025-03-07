import os
from pathlib import Path
from rotation_algorithm import make_quart, rotation_matrix_sclk
import spiceypy as sp
cwd = Path.cwd()
rel_path = 'geometries/kernels/mk/asperaMetaKernel_cktest.tm'


mkfile = os.path.join(cwd, rel_path)
sp.furnsh(mkfile)

target = 'ASPERA'
sclk1 = 8020944700000.000000
sclk2 = 8021808700000.000000

def main():

    with open("geometries/quaternions/quats_test.txt", "w") as f:
        cur = sclk1
        while (cur <= sclk2):
            # Write the data to the file
            cmat = rotation_matrix_sclk(cur, target)
            qtr = make_quart(cmat[0])
            result = str(cmat[1]) +" "+ str(qtr[0]) + " " + str(qtr[1]) + " " +  str(qtr[2]) + " " + str(qtr[3]) + "\n"
            f.write(result)
            cur += 600000

    sp.unload(mkfile)
if __name__ == "__main__":
    main()