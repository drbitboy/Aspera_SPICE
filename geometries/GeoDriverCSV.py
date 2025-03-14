from altitude.altitude_algorithm import altitude
from beta.beta_algorithm import beta
from beta0.beta0_algorithm import beta0
from eclipse.eclipse_algorithm import eclipse
from latlon.latlon_algorithm import latlon
from limbangle.limbangle_algorithm import limbangle_instr, boresight_for_difference, get_fov
from moonboresight.moonboresight_algorithm import moonboresight_instr
from sunboresight.sunboresight_algorithm import sunboresight_instr
from ramangle.ramangle_algorithm import ramangle
from obsgeo.obsgeo_algorithm import obsgeo
from vel_earth_los.vel_earth_los_algorithm import vel_earth_los
from vel_sc_los.vel_sc_los_algorithm import vel_sc_los
from slitpa.slitpa_algorithm import slitpa

import spiceypy as sp
import spiceypy.utils.support_types as stypes
import datetime
import csv
import sys
import getopt
import re


mkfile = './geometries/kernels/mk/asperaMetaKernelM82.tm'
sp.furnsh(mkfile)

eclipsedSun = 'SUN' # Can also be moon
eclipsedMoon = 'MOON'
planetEarth = "EARTH"
#Target = 'HST'
Target = 'ASPERA'
galaxy_targ = '9999000'
instr1 = "ASP_SLIT_0"
instr2 = "ASP_SLIT_1"

# initialize arguements
t_initial = None
t_final = None
step = None
file_name = None

opts, args = getopt.getopt(sys.argv[1:],'s:e:h:f:',['start_time=','end_time=','step_size=','file_name='])

# ensure that required arguements are present
if ('-s' not in sys.argv and '--start_time' not in sys.argv):
    print("Invalid usage: must specify start time (-s)")
    exit()

if ('-e' not in sys.argv and '--end_time' not in sys.argv):
    print("Invalid usage: must specify end time (-e)")
    exit()

if ('-h' not in sys.argv and '--step_size' not in sys.argv):
    print("Invalid usage: Must specify step size (-h)")
    exit()

for opt, arg in opts:
    if opt in ['-s','--start_time']:
        t_initial = arg
        print(t_initial)
    elif opt in ['-e','--end_time']:
        t_final = arg
        print(t_final)
    elif opt in ['-h','--step_size']:
        step = arg
        print(step)
    elif opt in ['-f','--file_name']:
        file_name = arg
        print(file_name)

#if file name not provided, GeoDriver + time (no colons or dashes)
if file_name == None:
    file_name = 'GeoDriver' + str(t_initial) + '.csv'

pattern_time = r'^([0-9]{4})-([0-9]{2})-([0-9]{2})T([0-9]{2}):([0-9]{2}):([0-9]{2})$'

if re.match(pattern_time,t_initial) == None:
    print("Incorrect start time format (YYYY-MM-DDThh:mm:ss)")
    exit()

if re.match(pattern_time,t_final) == None:
    print("Incorrect final time format (YYYY-MM-DDThh:mm:ss)")
    exit()

def GeoLoop(t_initial, t_final, step,file_name):
    #t_initial and t_final in form "YYYY-MM-DDThh:mm:ss"
    #step size is in units of seconds
    fmt = '%Y-%m-%dT%H:%M:%S'
    start = datetime.datetime.strptime(t_initial,fmt)
    end = datetime.datetime.strptime(t_final,fmt)
    res_date = start

    header = ['UTC','Altitude (km)','Cartesian Position wrt Earth (J200, km)','Cartesian Position wrt Sun (J200, km)','Beta Angle (deg)', 'Beta0 (deg)',
              'Eclipse Status (Sun)','Eclipse Status (Moon)','Longitude (ITRF93, deg)','Latitude (ITRF93, deg)','RA (J200, deg)','Dec (J200, deg)',
              'Limb Angle (slit_0) (deg)','Limb Angle (slit_2) (deg)', 'Moon Boresight (slit_0) (deg)','Moon Boresight (slit_2) (deg)',
              'Sun Boresight (slit_0) (deg)','Sun Boresight (slit_2) (deg)', 'Ram Angle (slit_0) (deg)','Ram Angle (slit_2) (deg)', 
              'BSC difference (ASP bod and ASP_SLIT_0)', 'BSC difference (ASP body and ASP_SLIT_1)','FOV (slit_0 visiblity, slit_2 visiblity)', 
              'OBSGEO', 'vel_earth_los', 'vel_sc_los (slit_0)', 'vel_sc_los (slit_2)', 'slitpa (slit_0)', 'slitpa (slit_2)']
    data = []
    while res_date <= end:
        UTC = res_date.strftime(fmt)
        ptarg1, ptarg2, betadeg = beta(UTC,Target)
        beta_0 = beta0(UTC, Target)
        lon, lat, ra, dec = latlon(UTC,Target)
        alt = altitude(UTC,Target)
        eclipsed_Sun = eclipse(UTC, eclipsedSun, Target)
        eclipsed_Moon = eclipse(UTC, eclipsedMoon, Target)
        limb_angle1 = limbangle_instr(UTC,Target, instr1)
        limb_angle2 = limbangle_instr(UTC,Target, instr2)
        moon_boresight1 = moonboresight_instr(UTC, Target, instr1)
        moon_boresight2 = moonboresight_instr(UTC, Target, instr2)
        sun_boresight1 = sunboresight_instr(UTC, instr1)
        sun_boresight2 = sunboresight_instr(UTC, instr2)
        ram_angle1 = ramangle(UTC, instr1)
        ram_angle2 = ramangle(UTC, instr2)
        asp_slit_0 = boresight_for_difference(UTC, Target, galaxy_targ, instr1)
        asp_slit_2 = boresight_for_difference(UTC, Target, galaxy_targ, instr2)
        visible = get_fov(UTC, galaxy_targ)
        obs= obsgeo(UTC, Target, planetEarth)
        vel_earth = vel_earth_los(UTC, instr1)
        vel_sc_los1 = vel_sc_los(UTC, instr1)
        vel_sc_los2 = vel_sc_los(UTC, instr2)
        slitpa1 = slitpa(UTC, instr1)
        slitpa2 = slitpa(UTC, instr2)


        csv_line = [UTC,alt,ptarg1,ptarg2,betadeg,beta_0,eclipsed_Sun, eclipsed_Moon,lon,lat,ra,dec,
                    limb_angle1,limb_angle2,moon_boresight1,moon_boresight2,sun_boresight1,sun_boresight2,
                    ram_angle1,ram_angle2, asp_slit_0, asp_slit_2, visible, obs, vel_earth, vel_sc_los1, 
                    vel_sc_los2, slitpa1, slitpa2]
        data.append(csv_line)

        res_date += datetime.timedelta(seconds=int(step))
    filename = 'Test1.csv'
    with open(filename,'w', newline="") as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(header)
        csvwriter.writerows(data)

GeoLoop(t_initial,t_final,step,file_name)
#GeoLoop('2023-05-01T00:00:01','2023-05-02T00:00:01',3600)

sp.unload(mkfile)

