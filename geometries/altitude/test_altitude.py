from altitude_algorithm import altitude
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

UTC = '2023 JUNE 01 00:00:01'
Target = 'HST'



#@pytest.mark.skip(reason="Need altitude values..")
def test_altitude():
    load_kernel()
    for utc_altitude in test_values:
        curr_altitude = altitude(utc_altitude.split(',')[0],Target)
        test_altitude = float(utc_altitude.split(',')[1])
        assert curr_altitude == pytest.approx(test_altitude, abs = .0001)

    print("\nAll altitude tests from test_hst.csv passed.\n")
    sp.unload(mkfile)