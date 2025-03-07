import spiceypy as sp

def main():

    mk = '../kernels/asperaMetaKernel.tm'
    spk = 'NewM82.bsp'
    pck = 'NewM82.tpc'

    sp.furnsh(mk)
    sp.furnsh(spk)
    sp.furnsh(pck)

    targ = 9999000
    utc = '2025 Jan 01 00:00:00'
    et = sp.str2et(utc)
    ref = 'J2000'
    abcorr = 'NONE'
    obs = 399 # 'EARTH'

    [ptarg, lt] = sp.spkezp(targ, et, ref, abcorr, obs)
    # [ptarg, lt] = sp.spkpos(targ, et, ref, abcorr, obs)

    print(ptarg)
    print(lt)

    sp.unload(mk)
    sp.unload(spk)
    sp.unload(pck)

main()