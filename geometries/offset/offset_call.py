import os
from pathlib import Path
from offset_algorithm import offset
import spiceypy as sp
import csv
from pytest import approx

def offset_brian(utc, instr, galaxy_targ):
    """ Calculates angle offset between boresight vector and
    vector to galaxy target

    Should be near-duplicate functionality with offset_algorithm.offset

    Args:
        utc (str): date and time at which altitude will be found
        instr (str): instrument from which to extract frame & boresight
        galaxy_targ (str): name of the galaxy

    Returns:
        float: angle between galaxy vector and boresight vector in degrees
        int: spacecraft ID
    """

    # # # # # PART 1: RETRIEVE ASPERA BORESIGHT VECTOR AND GALAXY VECTOR # # # # #
    # # # # #         - N.B. BOTH VECTORS WILL BE IN INSTRUMENT FRAME    # # # # #

    et = sp.str2et(utc)

    # Instrument => Instrument ID => Reference Frame Name and boresight
    # => Reference frame ID => Spacecraft ID => Spacecraft name (bodc2s)
    # => Vector to galaxy from spacecraft
    ref,vbore = sp.getfov(sp.bods2c(instr),99,99,99)[1:3]
    refID  = sp.gipool(f"FRAME_{ref}",0,1)[0]
    scID = sp.gipool(f"FRAME_{refID}_CENTER",0,1)[0]
    glx_vec = sp.spkezr(galaxy_targ, et, ref, 'NONE', sp.bodc2s(scID))[0][:3]

    # # # # # PART 2: FIND ANGLE BETWEEN BORESIGHT VECTOR AND GALAXY VECTOR # # # # #

    return sp.convrt(sp.vsep(vbore, glx_vec), 'RADIANS', 'DEGREES'), scID

def offset_test(utc, instr, galaxy_targ):

    # # # # # PART 1: RETRIEVE OFFSET FROM TWO METHODS # # # # #
 
    angle = offset(utc, instr, galaxy_targ)
    angle_brian, scID = offset_brian(utc, instr, galaxy_targ)

    # # # # # PART 2: GET THE SOURCE GALAXY UNIT VECTOR VIA TWO METHODS # # # # #

    et = sp.str2et(utc)
    galaxy_id = sp.bodn2c(galaxy_targ)

    glx_vec = sp.gdpool(f"SITE{galaxy_id}_XYZ", 0, 3)
    glx_ref = sp.gcpool(f"SITE{galaxy_id}_FRAME", 0, 1, 99)[0]
    if glx_ref.upper() != 'J2000':
        glx_vec = sp.mxv(sp.pxform(glx_ref, 'J2000', et), glx_vec)

    glx_vec_brian = sp.spkezr(galaxy_targ, et, 'J2000', 'NONE', sp.bodc2s(scID))[0][:3]

    # # # # # PART 3: TEST ANGLES AND VECTORS # # # # #

    assert approx(angle_brian, rel=1e-14) == angle
    assert sp.vnorm(sp.vsub(glx_vec, glx_vec_brian)) < 1e-14

    # # # # # PART 3: RETURN ANGLE FROM offset_algorithm.offset # # # # #

    return angle

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
                angle1 = offset_test(utc_cur, instr1, name)
                angle2 = offset_test(utc_cur, instr2, name)
                csvwriter.writerow([utc_cur, angle1, angle2])
                et += 3600

    sp.unload(mkfile)
    for glxfile in glxfiles: sp.unload(glxfile)

if __name__ == "__main__":
    main()
def test_pytest_main(): main()
