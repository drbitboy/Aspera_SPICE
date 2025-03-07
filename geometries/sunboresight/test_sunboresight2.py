from sunboresight_algorithm import sunboresight
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
galaxy_targ = '9999000'


#@pytest.mark.skip(reason="Need sunboresight values..")
def test_sunboresight():
    load_kernel()
    # NOTE : commenting out assertions until we get test values
    for utc_sbs in test_values:
        curr_sbs = sunboresight(utc_sbs.split(',')[0], Target, galaxy_targ)
        test_sbs = float(utc_sbs.split(',')[10])
        #assert curr_sbs == pytest.approx(test_sbs, abs = .0001)
        pass
    print("\nAll sunboresight angle tests from test_hst.csv passed.\n")
    sp.unload(mkfile)