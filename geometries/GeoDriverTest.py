from altitude.altitude_Algorithm import altitude
from beta.beta_Algorithm import beta
from geometries.eclipse.AsperaEclipse_Algorithm import eclipse
from geometries.latlon.AsperaLatLon_Algorithm import latlon

import spiceypy as sp
import spiceypy.utils.support_types as stypes

import csv
import os

#read file
testfile = open('./geometries/artifacts/test_values.csv','r')
data = list(csv.reader(testfile, delimiter = ','))
test = data[1]
testfile.close()

#os.chdir(os.path.abspath(os.path.dirname(__file__)))
mkfile = './geometries/kernels/mk/asperaMetaKernel.tm'
#mkfile = os.path.abspath(os.path.join(os.path.dirname(__file__), mkfile))
sp.furnsh(mkfile)

UTC = '2023-06-01T00:00:01'

eclipsedSun = 'SUN' # Can also be moon
eclipsedMoon = 'MOON'
Target = 'HST'

#assign variables to values returned
ptarg1, ptarg2, betadeg = beta(UTC,Target)
lon, lat, ra, dec = latlon(UTC,Target)

def tests(E_var,T_var):
    t = False
    if abs(E_var - T_var) <= .01:
       t = True
    return t

print("X-Earth =",tests(ptarg1[0],float(test[1])))
print("Y-Earth =",tests(ptarg1[1],float(test[2])))
print("Z-Earth =",tests(ptarg1[2],float(test[3])))

print("X-Sun =",tests(ptarg2[0],float(test[4])))
print("Y-Sun =",tests(ptarg2[1],float(test[5])))
print("Z-Sun =",tests(ptarg2[2],float(test[6])))


if tests(betadeg,float(test[7])) and tests(betadeg,float(test[8])):
    print("Beta Angle = True")
else:
    print("Beta Angle = False")

if tests(ra,float(test[9])) and tests(ra,float(test[10])):
    print("RA = True")
else:
    print("RA = False")

if tests(dec,float(test[11])) and tests(dec,float(test[12])):
    print("Dec = True")
else:
    print("Dec = False")




