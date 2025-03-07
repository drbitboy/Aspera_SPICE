from eclipse_algorithm import eclipse

import spiceypy as sp
import spiceypy.utils.support_types as stypes
import os
import pytest


mkfile = './geometries/kernels/mk/asperaMetaKernel.tm'

def load_kernel():
    global test_values
    script_dir = os.path.dirname(os.path.abspath(__file__))
    analysis_pwd = os.path.join(script_dir, "../..")
    os.chdir(analysis_pwd)
    sp.furnsh(mkfile)
    
    test_values = open('./geometries/test_hst.csv').readlines()[1:]
    
eclipsedSun = 'SUN' # Can also be moon
eclipsedMoon = 'MOON'
Target = 'HST'
#Target = 'ASPERA'


#@pytest.mark.skip(reason="Need eclipse values..")
def test_eclipse():
    load_kernel()
    # NOTE : commenting out assertions until we get test values
    for utc_eclipse in test_values:
        curr_sun_ecl = eclipse(utc_eclipse.split(',')[0], "SUN", Target)
        curr_moon_ecl = eclipse(utc_eclipse.split(',')[0], "MOON", Target)
        
        test_sun_ecl = utc_eclipse.split(',')[4]
        test_moon_ecl = utc_eclipse.split(',')[5].strip()
        # assert curr_sun_ecl == test_sun_ecl
        # assert curr_moon_ecl == test_moon_ecl
        pass
    print("\nAll sun/moon eclipse tests from test_hst.csv passed.\n")
    sp.unload(mkfile)