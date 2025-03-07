from ramangle_algorithm import ramangle

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
test_ram = 137.18021609938828
test_vel = -5.549088587457021

def test_one_value():
    load_kernel()
    ram, vel = ramangle(UTC, Target, Galaxy_Targ)

    assert ram == pytest.approx(test_ram, abs = .0001)
    assert vel == pytest.approx(test_vel, abs = .0001)
    sp.unload(mkfile)

def test_values_csv():
    load_kernel()
    pass
    sp.unload(mkfile)