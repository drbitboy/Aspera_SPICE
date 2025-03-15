from sunboresight_algorithm import sunboresight_instr

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
Galaxy_Targ = '9999000'
test_sunAngle = 0.14514962569996467

def test_one_value():
    load_kernel()
    sunAngle = sunboresight_instr(UTC, Target, Galaxy_Targ)

    assert sunAngle == pytest.approx(test_sunAngle, abs = .0001)
    sp.unload(mkfile)
    
def test_values_csv():
    load_kernel()
    pass
    sp.unload(mkfile)
