# verify that vega.tpc works by calculating

import math
import spiceypy as sp

def main():

    mkfile = '../kernels/asperaMetaKernelWithStar.tm'
    sp.furnsh(mkfile)

# # # NEEDS SPK # # #

#    targ = 8888001 # 'Vega'
#    et = 693204549.1835771 # 12/19/21 16:48:00
#    ref = 'J2000'
#    abcorr = 'NONE'
#    obs = 399 # 'EARTH'

#    position, velocity = sp.spiceypy.spkez(targ, et, ref, abcorr, obs)
#    print('\nposition: ', position)
#    print('\nvelocity: ', velocity)
#    print()

# # # READS DIRECTLY FROM PCK # # #

    bodyID = 8888001 # 'Vega'
    item = 'RADII' # we want to know radii of star
    maxn = 3 # there are 3 dimensions to star radius - we want to see all of them (tested w/ 1, received error)

    # calculate output
    [dim, values] = sp.bodvcd(bodyID, item, maxn)

    # print output
    print('\nNO. VALS RETURNED: ', dim)
    print('RADII: ', values)

    # check XYZ coordinates match ra/dec
    rectan = [0.125096, -0.769413, 0.626382] # given coordinates, can't read them out of file
    [range, ra, dec] = sp.recrad(rectan)
    print('\nRANGE: ', range)
    print('RA: ', ra)
    print('DEC: ', dec)
    print()

    # M82 / Vega
    newRA = 148.9667 # 279.23473479
    newDEC = 69.6797 # 38.7836889

    x = math.cos(newRA * math.pi/180) * math.cos(newDEC * math.pi/180)
    y = math.sin(newRA * math.pi/180) * math.cos(newDEC * math.pi/180)
    z = math.sin(newDEC * math.pi/180)
    print(x, y, z)

    sp.unload(mkfile)

main()