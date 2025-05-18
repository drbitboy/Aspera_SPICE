import os
import spiceypy as sp
from pytest import approx

def main():

    mk = os.path.join(os.path.dirname(__file__),'../kernels/mk/aspera_mk.tm')
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

    tptarg = sp.vpack(-9.76810086e+16, 5.87699666e+16, 3.07840739e+17)
    tlt = 1094991953051.3345

    assert (sp.vnorm(sp.vsub(ptarg, tptarg)) / sp.vnorm(ptarg)) < 1e-8
    assert approx(lt, rel=1e-14) == tlt

if "__main__" == __name__:
  main()
def test_pytest_main(): main()
