import os
from pathlib import Path
from offset_algorithm import offset
import spiceypy as sp
import csv

def main():
    """
    """

    names = ["NGC 625", "NGC 660", "NGC 891", "NGC 1353", "NGC 1406", "NGC 1448"]
    # Find location of kernel & furnish it
    mk_path = 'geometries/kernels/mk/aspera_mk.tm'
    mkfile = os.path.join(*mk_path.split('/'))
    sp.furnsh(mkfile)

    glxfiles = list()
    for name in names:
        tpc_path = f'geometries/kernels/generators/{name.replace(" ", "_")}.tpc'
        glxfile = os.path.join(*tpc_path.split('/'))
        sp.furnsh(glxfile)
        glxfiles.append(glxfile)



    utc = '2025 JUNE 01 00:00:01'
    instr1 = "ASP_SLIT_1"
    instr2 = "ASP_SLIT_2"

    for name in names:
        et = sp.str2et(utc)
        csv_path = f'geometries/offset/{name.replace(" ", "_")}.csv'
        with open(os.path.join(*csv_path.split('/')),'w', newline="") as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow('UTC,ASP_SLIT_1 offset,ASP_SLIT_2 offset'.split(','))
            for i in range(24):
                utc_cur = sp.et2utc(et, 'C', 3)
                angle1 = offset(utc_cur, instr1, name)
                angle2 = offset(utc_cur, instr2, name)
                csvwriter.writerow([utc_cur, angle1, angle2])
                et += 3600

    sp.unload(mkfile)
    for glxfile in glxfiles: sp.unload(glxfile)

if __name__ == "__main__":
    main()
def test_pytest_main(): main()
