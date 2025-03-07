from sun_radec_algorithm import sun_radec

import spiceypy as sp
import os
import csv
import pytest


mkfile = './geometries/kernels/mk/asperaMetaKernelM82.tm'

def load_kernel():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    analysis_pwd = os.path.join(script_dir, "../..")
    os.chdir(analysis_pwd)
    sp.furnsh(mkfile)


UTC = '2025 JUNE 01 00:00:01'
Target = 'ASPERA'
test_raDeg = 68.81335865587167
test_decDeg = 22.00922025779235

def test_one_value():
    load_kernel()
    raDeg, decDeg = sun_radec(UTC, Target)

    assert raDeg == pytest.approx(test_raDeg, abs = .0001)
    assert decDeg == pytest.approx(test_decDeg, abs = .0001)
    sp.unload(mkfile)

def test_values_csv():
    load_kernel()
    pass
    sp.unload(mkfile)