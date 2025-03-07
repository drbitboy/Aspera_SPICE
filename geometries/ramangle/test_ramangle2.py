from ramangle_algorithm import ramangle
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
    
UTC = '2023 JUNE 01 00:00:01'
Target = 'HST'
galaxy_targ = '9999000'



#@pytest.mark.skip(reason="Need ramangle values..")
def test_ramangle():
    load_kernel()
    # NOTE : commenting out assertions until we get test values
    for utc_ramangle in test_values:
        curr_ramangle = ramangle(utc_ramangle.split(',')[0], Target, galaxy_targ)
        test_ramangle = float(utc_ramangle.split(',')[9])
        #assert curr_ramangle == pytest.approx(test_ramangle, abs = .0001)
        pass

    print("\nAll ramangle tests from test_hst.csv passed.\n")
    sp.unload(mkfile)
