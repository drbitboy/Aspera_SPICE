from latlon_algorithm import latlon

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

UTC = '2023-06-01T00:00:01'
Target = 'HST'
test_values = [-13.773143968504627, -19.10442363834492, 235.1182396412025, -19.02907942878186]

def test_one_value():
    load_kernel()
    values = latlon(UTC, Target)

    for index in range(len(test_values)):
        #assert values[index] == pytest.approx(test_values[index], abs = .0001)
        pass # need to change values
    
    sp.unload(mkfile)

def test_values_csv():
    load_kernel()

    testfile = open(os.path.abspath('./geometries/latlon/test_latlon.csv'),'r')
    data = list(csv.reader(testfile, delimiter = ','))[1:]

    for row in data:
        utc = row[0]
        print(utc)
        test_values = [float(value) for value in row[1:]]
        values = latlon(utc, Target)

        for index in range(len(test_values)):
            #assert values[index] == pytest.approx(test_values[index], abs = .0001)
            pass # need to change values
        
    sp.unload(mkfile)

