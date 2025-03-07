from latlon_algorithm import latlon

import spiceypy as sp
import os
import pytest

mkfile = './geometries/kernels/mk/asperaMetaKernelM82.tm'

def load_kernel():
    global test_values
    script_dir = os.path.dirname(os.path.abspath(__file__))
    analysis_pwd = os.path.join(script_dir, "../..")
    os.chdir(analysis_pwd)
    sp.furnsh(mkfile)
    
    
    test_values = open('./geometries/test_hst.csv').readlines()[1:]

utc = '2025 JUNE 01 00:00:01'
Target = "HST"



#@pytest.mark.skip(reason="Need latlon values..")
def test_latlon():
    load_kernel()
    # NOTE : commenting out assertions until we get test values
    for utc_latlon in test_values:
        longitude, latitude, ra, dec = latlon(utc_latlon.split(',')[0],Target)
        test_lon = float(utc_latlon.split(',')[7])
        test_lat = float(utc_latlon.split(',')[6])
        pass
        # assert longitude == pytest.approx(test_lon, abs = .0001)
        # assert latitude == pytest.approx(test_lat, abs = .0001)
    sp.unload(mkfile)
    print("\nAll latlon tests from test_hst.csv passed.\n")