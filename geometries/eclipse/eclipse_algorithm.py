import spiceypy as sp

def eclipse(utc, eclipsed_body, target):
    """Determines whether or not a specified body (back) has been eclipsed by Earth (front) as seen
    by an observer (Aspera).

    Args:
        utc (str): date and time at which state of eclipse, or occultation, will be determined
        eclipsed_body (str): body that may be eclisped
        target (str): observer (Aspera)

    Returns:
        str: state of eclipse
    """
    
    et = sp.str2et(utc)
    abcorr = 'NONE'

    # Front body
    front = 'EARTH'
    fshape = 'ELLIPSOID'
    fframe = 'ITRF93'

    # Back body
    back = eclipsed_body
    bshape = 'ELLIPSOID'
    bframe = f'IAU_{eclipsed_body}'

    # Determine whether or not the back body is eclipsed
    ocltid = sp.occult(back, bshape, bframe, front, fshape, fframe, abcorr, target, et)

    # Translate occult ID from numerical to English
    if (ocltid < 0) or (ocltid > 0):

        # First by second, or second by first
        ocltid = 'PARTIAL'

    else:
        ocltid = 'NONE'

    return ocltid
