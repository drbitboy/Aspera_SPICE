#from altitude.AsperaAltitude import altitude
from beta.beta_Algorithm import beta
#from eclipse.AsperaEclipse import eclipse
from geometries.latlon.AsperaLatLon_Algorithm import latlon

import spiceypy as sp
import spiceypy.utils.support_types as stypes

import csv
import pytest
import os

# Read test.csv which has expected values from WebGeoCalc and Horizons Ephemeris data
testValsPath = './artifacts/test_values.csv'
testValsPath = os.path.abspath(os.path.join(os.path.dirname(__file__), testValsPath))
testfile = open(testValsPath,'r')
data = list(csv.reader(testfile, delimiter = ','))
test = data[1]
testfile.close()

# Furnish Kernel
# os.chdir(os.path.abspath(os.path.dirname(__file__)))
mkfile = './geometries/kernels/mk/asperaMetaKernel.tm'
#mkfile = os.path.abspath(os.path.join(os.path.dirname(__file__), mkfile))
sp.furnsh(mkfile)

# Load algorithm arguements
UTC = '2023-06-01T00:00:01'
Target = 'HST'

# Checking that AsperaLatLon outputs are approximately equal to expected values from WebGeoCalc and Horizons ephemeris data
def test_AsperaLatLon_vs_geowebcalc_Horizons():
    # Loading AsperaLatLon outputs
    lon, lat, ra, dec = latlon(UTC,Target)

    # Loading expected values from GeoWebCalc and Horizons ephemeris data
    GeoWebCalc = []
    for i in range(9,13):
        GeoWebCalc.append(float(test[i]))

    # Create list with ra/dec outputs of AsperaLatLon
    # ra and dec added twice to test against GeoWebCalc and Horizons ephemeris data
    LatLonOutputs = [ra, ra, dec, dec]

    # Comparing LatLon outputs to values from 'test.csv'
    for index in range(len(LatLonOutputs)):
        assert LatLonOutputs[index] == pytest.approx(GeoWebCalc[index],abs = .01)

# Checking that BetaAngle outputs are approximately equal to expected values from WebGeoCalc and Horizons ephemeris data
def test_AsperaBetaAngle_vs_geowebcalc():
    # Loading AsperaBetaAngle outputs
    ptarg1, ptarg2, betadeg = beta(UTC,Target)

    # Loading expected values from GeoWebCalc and Horizons ephemeris data
    GeoWebCalc = []
    for i in range(1,9):
        GeoWebCalc.append(float(test[i]))

    # Create list with outputs of AsperaBetaAngle
    # betadeg added twice to test against GeoWebCalc and Horizons ephemeris data
    BetaAngleOutputs = [ptarg1[0],ptarg1[1],ptarg1[2],ptarg2[0],ptarg2[1],ptarg2[2],betadeg,betadeg]

    # Comparing BetaAngle outputs to values from 'test.csv'
    for index in range(len(BetaAngleOutputs)):
        assert BetaAngleOutputs[index] == pytest.approx(GeoWebCalc[index], abs = .01)

