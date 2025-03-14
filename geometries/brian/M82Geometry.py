import os
import spiceypy as sp

def main():

    mk = os.path.join(os.path.dirname(__file__),'../kernels/mk/asperaMetaKernel.tm')
    spk = os.path.join(os.path.dirname(__file__),'M82spk.bsp')

    sp.furnsh(mk)
    sp.furnsh(spk)

    targ = 9999000
    utc = '2025 Jun 01 00:00:01'
    et = sp.str2et(utc)
    ref = 'J2000'
    abcorr = 'NONE'
    obs = 399 # 'EARTH'

    [ptarg, lt] = sp.spkezp(targ, et, ref, abcorr, obs)

    print(ptarg)
    print(lt)

    sp.unload(mk)
    sp.unload(spk)

main()
