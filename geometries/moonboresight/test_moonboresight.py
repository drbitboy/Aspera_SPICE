from moonboresight_algorithm import moonboresight

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
Galaxy_Targ = '9999000'
Target = 'ASPERA'
test_value = 65.6264029680922

def test_one_value():
    load_kernel()
    value = moonboresight(UTC, Target, Galaxy_Targ)

    assert value == pytest.approx(test_value, abs = .0001)
    sp.unload(mkfile)

def test_values_csv():
    load_kernel()
    pass
    sp.unload(mkfile)
