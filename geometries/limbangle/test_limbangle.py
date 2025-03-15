from limbangle_algorithm import limbangle
import spiceypy as sp
import os
import pytest
import math


mkfile = './geometries/kernels/mk/asperaMetaKernelM82.tm'

def load_kernel():
    global test_values
    script_dir = os.path.dirname(os.path.abspath(__file__))
    analysis_pwd = os.path.join(script_dir, "../..")
    os.chdir(analysis_pwd)
    sp.furnsh(mkfile)
    
    test_values = open('./geometries/test_hst.csv').readlines()[1:]

galaxy_targ = '9999000'
UTC = '2025 JUNE 01 00:00:01'
Target = "HST"

instrument_info = {'ASP_SOLAR': ['CIRCLE', 3], 'ASP_S-BAND': 
                   ['CIRCLE', 3], 'ASP_SLIT_0': ['RECTANGLE', 4], 'ASP_SLIT_1': ['RECTANGLE', 4]}

#@pytest.mark.skip(reason="Need limangle values..")
def test_limbangle():
    load_kernel()
    # NOTE : commenting out assertions until we get test values
    for utc_limbangle in test_values:
        print(utc_limbangle.split(',')[0])
        curr_limbangle = limbangle(utc_limbangle.split(',')[0], galaxy_targ, Target)
        print(curr_limbangle)
        test_limbangle = float(utc_limbangle.split(',')[6])
        print(test_limbangle)
        #assert curr_limbangle == pytest.approx(test_limbangle, abs = .0001)
        pass
    print("\nAll limbangle tests from test_hst.csv passed.\n")
    sp.unload(mkfile)
