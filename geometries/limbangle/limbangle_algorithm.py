import math as m
import spiceypy as sp

def limbangle(utc,target, galaxy_targ):
    """Calculates limb angle, which is measured between boresight vector and unit vector of Earth
    limb (solved for indirectly).

    Assume boresight is pointed at galaxy_targ

    Args:
        utc (str): date and time at which beta0 angle will be found
        target (str): observer with boresight
        galaxy_targ (str): body ID for galaxy contained in mkfile
    """

    # # # # # PART 1: ANGLE A # # # # #

    et = sp.str2et(utc)
    ref = 'J2000'
    abcorr = 'NONE'

    #btc use beta0 instead?
    # Find radius of Earth in 3 dims
    [dim, vals] = sp.bodvrd('EARTH', 'RADII',3)

    # Calculate average radius assuming Earth is a perfect sphere
    r = (1/3) * (vals[0] + vals[1] + vals[2])

    # Find magnitude of Aspera's position vector wrt Earth
    x_sc, lt = sp.spkpos(target, et, ref, abcorr, 'EARTH')
    x_sc_mag = sp.vnorm(x_sc)

    # Use Earth's radius and the magnitude of Aspera's position vector to find angle A, rad -> deg
    a_rad = m.asin(r/x_sc_mag)
    a_deg = sp.convrt(a_rad, 'RADIANS', 'DEGREES')

    # # # # # PART 2: ANGLE B # # # # #

    # Find Aspera's position vector wrt galaxy
    bsc, lt = sp.spkpos(galaxy_targ, et, ref, abcorr, target)

    #btc use vsep instead?
    # Use Aspera's position vectors to find angle B, convert rad -> deg
    b_rad = m.acos( sp.vdot(x_sc, bsc) / (x_sc_mag * sp.vnorm(bsc)) )
    b_deg = sp.convrt(b_rad, 'RADIANS', 'DEGREES')

    # Calculate limb angle
    limb = 180 - a_deg - b_deg

    return limb

def limbangle_instr(utc,target, instr):
    """Calculates limb angle, which is measured between boresight vector and unit vector of Earth
    limb (solved for indirectly).


    Args:
        utc (str): date and time at which limb angle will be found
        target (str): observer with boresight
        instr (str): instrument name for Aspera
    """

    # # # # # PART 1: ANGLE A # # # # #

    et = sp.str2et(utc)
    ref = 'J2000'
    abcorr = 'NONE'

    # Find radius of Earth in 3 dims
    [dim, vals] = sp.bodvrd('EARTH', 'RADII',3)

    #btc use beta0 instead?
    # Calculate average radius assuming Earth is a perfect sphere
    r = (1/3) * (vals[0] + vals[1] + vals[2])

    # Find magnitude of Aspera's position vector wrt Earth
    x_sc, lt = sp.spkpos(target, et, ref, abcorr, 'EARTH')
    x_sc_mag = sp.vnorm(x_sc)

    # Use Earth's radius and the magnitude of Aspera's position vector to find angle A, rad -> deg
    a_rad = m.asin(r/x_sc_mag)
    a_deg = sp.convrt(a_rad, 'RADIANS', 'DEGREES')

    # # # # # PART 2: ANGLE B # # # # #

    # Find Aspera's boresight vector in J2000
    instid = sp.bodn2c(instr)
    shape, frame, bsight, n, bounds = sp.getfov(instid,99,99,99)
    rotation_matrix = sp.pxform(frame, ref, et)  #btc must be in same frame as x_sc
    vboreJ2k = sp.mxv(rotation_matrix,bsight)

    # bsc, lt = sp.spkpos(galaxy_targ, et, ref, abcorr, target)

    #btc use vsep instead?
    # Use Aspera's position vectors to find angle B, convert rad -> deg
    b_rad = m.acos( sp.vdot(x_sc, vboreJ2k) / (x_sc_mag * sp.vnorm(vboreJ2k)) )
    b_deg = sp.convrt(b_rad, 'RADIANS', 'DEGREES')

    # Calculate limb angle
    limb = 180 - a_deg - b_deg

    return limb


def boresight_for_difference(utc, target, galaxy_targ, reference_frame):
    """Calculates boresight vector between Aspera and galaxy_targ, and calculates
    boresight vector between galaxy_targ and a reference frame of an instrument
    on Aspera (check out ik kernel for instrument names).

    NOTE: For testing only. If the difference between both vectors is 0, Aspera is
    pointing in the direction of the reference frame. If this is true, function get_fov
    defined in test_limbangle should return true for a given set of UTC times.


    Args:
        utc (str): date and time at which beta0 angle will be found
        galaxy_targ (str): body ID for galaxy contained in mkfile
        reference_grame (str): a instrument name that has been defined in an ik file

    Returns:
        #btc fix somment
        vector: the difference between Asperas boresight vector and the instruments boresight vector, in J2000 frame.
    """

    et = sp.str2et(utc)
    ref = 'J2000'
    abcorr = 'NONE'

    #btc use beta0 instead?
    # Find radius of Earth in 3 dims
    [dim, vals] = sp.bodvrd('EARTH', 'RADII',3)

    # Calculate average radius assuming Earth is a perfect sphere
    r = (1/3) * (vals[0] + vals[1] + vals[2])

    # Find magnitude of Aspera's position vector wrt Earth
    x_sc, lt = sp.spkpos(target, et, ref, abcorr, 'EARTH')
    x_sc_mag = sp.vnorm(x_sc)

    # Use Earth's radius and the magnitude of Aspera's position vector to find angle A, rad -> deg
    a_rad = m.asin(r/x_sc_mag)
    a_deg = sp.convrt(a_rad, 'RADIANS', 'DEGREES')

    # # # # # PART 2: ANGLE B # # # # #

    # Find Aspera's boresight vector wrt galaxy
    bsc_aspera, lt = sp.spkpos(galaxy_targ, et, ref, abcorr, target)

    # Find boresight vector between reference_frame and galaxy
    frame, bsc_rf = sp.getfov(sp.namfrm(reference_frame), 4)[1:3]

    #btc convert bsc_rf to same frame (J2000) as bsc_aspera before subtraction
    return bsc_aspera - sp.mxv(sp.pxform(reference_frame,ref,et),bsc_rf)

def get_fov(UTC, galaxy_targ):
    '''
    Determines whether or not a galaxy target is in the fov (field of view) of an
    instrument (using -1999301 = ASP_SLIT1 and -1999302 = ASP_SLIT2 for this test)
    at a specific UTC time

    Args:
        UTC (str): desired time to calculate whether or not galaxy_targ is the
        specified instruments FOV

    Returns:
        (boolean1, boolean2): boolean1 is true if galaxy_targ is in the fov of
        ASP_SLIT1 at the given UTC time. boolean2 is true if galaxy_targ is in the fov of
        ASP_SLIT2 at the given UTC time
    '''
    et = sp.str2et(UTC)

    # fovTrg = returns whether or not a target is visible
    # the fov of an instrument at a given time
    # inst = instrument name
    # target = target observed
    # tshape = name of shape model for target (assumed point)
    # tframe = blank because tshape is a point
    # abcorr = aberration correction (assumed none)
    # observr = name of observer
    # et = time of observation
    # returns true of galaxy_targ is in the fov of the instrument
    slit1_visibl = sp.fovtrg('-1999301', galaxy_targ, 'POINT', '', 'NONE', 'ASPERA', et)
    slit2_visibl = sp.fovtrg('-1999302', galaxy_targ, 'POINT', '', 'NONE', 'ASPERA', et)

    return (slit1_visibl, slit2_visibl)
    #print(slit2_visibl)
