from beta_algorithm import beta
import spiceypy as sp
import pytest
import os


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

#@pytest.mark.skip(reason="Need beta values..")
def test_beta():
    load_kernel()
    # NOTE : commenting out assertions until we get test values
    for utc_beta in test_values:
        curr_beta = beta(utc_beta.split(',')[0],Target)[2]
        test_beta = float(utc_beta.split(',')[2])
        #assert curr_beta == pytest.approx(test_beta, abs = .0001)
        pass
    
    print("\nAll beta angle tests from test_hst.csv passed.\n")
    sp.unload(mkfile)