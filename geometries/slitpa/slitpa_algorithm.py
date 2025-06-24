import os
from pathlib import Path
import spiceypy as sp

def slitpa(utc, instr):

    """Slit position angle East of North (deg)
        Args:
        utc (str): date and time at which Earth LOS velocity will be found
        instr (str): instrument name for Aspera

    Returns:
        float: Slit position angle
    """

    # # # # # PART 0: CONVERT GET REQUIRED INSTRUMENT ID AND FOV_REF_VECTOR # # # # #

    instid = sp.bodn2c(instr)

    # Get boresight and frame; ensure shape is rectangle
    [shape, frame, bsight, n, bounds] = sp.getfov(instid, 4, 32, 32)
    assert shape=="RECTANGLE"

    inst_fov_ref_vector = sp.gdpool(f"INS{instid}_FOV_REF_VECTOR", 0, 3)

    # # # # # PART 1: CONVERT CELESTIAL NORTH IN J2000 FRAME TO SLIT FRAME # # # # #

    # Direction of Celestial North in J2000 frame
    celestial_north = [0, 0, 1]

    et = sp.utc2et(utc)

    # Rotate celestial_north to slit frame
    rotation_matrix_1 = sp.pxform('J2000', frame, et)
    ASP_north = sp.mxv(rotation_matrix_1, celestial_north)

    # # # # # PART 2: BUILD NEW COORDINATE FRAME WITH BORESIGHT AS Z-AXIS AND NEW CELESTIAL NORTH IN XZ PLANE # # # # #

    # Create new coordinate frame & rotation matrix to express vectors in frame
    #btc Inverted boresight is along +Z (sp.vminus does inversion)
    #btc North vector is in XZ plane and in half-plane on +X side of +Z
    #btc East will be +Y
    rotation_matrix_2 = sp.twovec(sp.vminus(bsight), 3, ASP_north, 1)

    # # # # # PART 3: ROTATE FOV REF VECTOR FOR SLIT INTO NEW FRAME # # # # #

    new_inst_vector = sp.mxv(rotation_matrix_2, inst_fov_ref_vector)

    # # # # # PART 4: RETRIEVE RIGHT ASCENSION (RA) OF _FOV_REF_VECTOR IN NEW FRAME # # # # #
    #btc 0degrees would be in +X/Z half-plane, same half-plane as North
    #btc 90degrees would be in +Y/Z half-plane, so East
    #btc 180degrees would be in -X/Z half-plane, opposite half-plane as North
    #btc 270degrees would be in -Y/Z half-plane, so West

    RA = sp.recrad(new_inst_vector)[1]
    deg_RA = sp.convrt(RA, 'RADIANS', 'DEGREES')

    return deg_RA
    #btc alternative:  return sp.recrad(new_inst_vector)[1] * sp.dpr()

    # Why not transform inst_fov_ref_vector to J2000 and find angle between that and Celestial North?
    # Code oscillates between ~53.7 & ~347.3 deg, not sure why
    # Measured East of North, so angle should vary between 0 and 360 deg
