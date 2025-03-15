from altitude.altitude_algorithm import altitude  #btc fix typo
from beta.beta_algorithm import beta  #btc fix typo
from eclipse.eclipse_algorithm import eclipse
from latlon.latlon_algorithm import latlon  #btc fix typo

from limbangle.limbangle_algorithm import limbangle  #btc fix typo

import spiceypy as sp

#had to make different kernel path for GeoDriver, DON'T DO THIS
#set current working directory to geometries for other test files
#update: setting current working directory to analysis for testing

mkfile = './geometries/kernels/mk/asperaMetaKernelM82.tm'
sp.furnsh(mkfile)

Target = 'ASPERA'
if Target == 'ASPERA':
    UTC = '2025 JUNE 01 00:00:01'
else:
    UTC = '2023 JUNE 01 00:00:01'

eclipsedSun = 'SUN' # Can also be moon
eclipsedMoon = 'MOON'
galaxy_targ = '9999000'

#assign variables to values returned
limb = limbangle(UTC, galaxy_targ, Target)
ptarg1, ptarg2, betadeg = beta(UTC,Target)
lon, lat, ra, dec = latlon(UTC, Target)
latlong = (lon, lat)
radec = (ra, dec)

print("At UTC " + UTC + ": \n")

print(Target + "'s altitude (km): \n" + str(altitude(UTC, Target)) + "\n")
print(Target + "'s cartesian position with respect to Earth's center in J2000 frame (km): \n" + str(ptarg1) + "\n")
print(Target + "'s cartesian position with respect to the Sun's center in J2000 frame (km): \n" + str(ptarg2) + "\n")
print(Target + "'s beta angle (degrees): \n" + str(betadeg) + "\n") 
print(Target + " eclipse status (Sun): \n" + eclipse(UTC, eclipsedSun, Target) + "\n")
print(Target + " eclipse status (Moon): \n" + eclipse(UTC, eclipsedMoon, Target) + "\n")
print(Target + "'s longitude and latitude in ITRF93 frame (deg): \n" + str(latlong) + "\n")
print(Target + "'s RA and Dec in J2000 frame (deg): \n" + str(radec) + "\n")
print(Target + "'s limbangle wrt Earth and " + galaxy_targ + " is: " + str(limb))


sp.unload(mkfile)

# have driver select what data they want to output
