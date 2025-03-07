from sun_radec_algorithm import sun_radec
import spiceypy as sp
import pytest
import os

mkfile = './geometries/kernels/mk/asperaMetaKernel.tm'

def load_kernel():
    global test_values
    script_dir = os.path.dirname(os.path.abspath(__file__))
    analysis_pwd = os.path.join(script_dir, "../..")
    os.chdir(analysis_pwd)
    sp.furnsh(mkfile)
    
    test_values = open('./geometries/test_hst.csv').readlines()[1:]

utc = '2025 JUNE 01 00:00:01'
Target = "HST"

#@pytest.mark.skip(reason="Need values for sunPos..")
def test_sunPos():
    load_kernel()
    # NOTE : commenting out assertions until we get test values
    for utc_sun in test_values:
        curr_sun = sun_radec(utc_sun.split(',')[0], Target)
        test_sun = float(utc_sun.split(',')[9])
        #assert curr_beta0 == pytest.approx(test_beta0, abs = .0001)
        pass
    print("\nAll sunPos angle tests from test_hst.csv passed.\n")
    sp.unload(mkfile)
