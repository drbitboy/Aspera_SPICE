KPL/FK
 
   FILE: ksat_punta_arenas_sg7s_1751.tf
 
   This file was created by PINPOINT.
 
   PINPOINT Version 3.3.0 --- December 13, 2021
   PINPOINT RUN DATE/TIME:    2025-06-24T16:06:11
   PINPOINT DEFINITIONS FILE: ksat_punta_arenas_sg7s_1751.pinpoint
   PINPOINT PCK FILE:         empty.tpc
   PINPOINT SPK FILE:         ksat_punta_arenas_sg7s_1751.bsp
 
   The input definitions file is appended to this
   file as a comment block.
 
 
   Body-name mapping follows:
 
\begindata
 
   NAIF_BODY_NAME                      += 'NDOSL_SG7S'
   NAIF_BODY_CODE                      += 399101751
 
\begintext
 
 
   Reference frame specifications follow:
 
 
   Topocentric frame NDOSL_SG7S_TOPO
 
      The Z axis of this frame points toward the zenith.
      The X axis of this frame points North.
 
      Topocentric frame NDOSL_SG7S_TOPO is centered at the
      site NDOSL_SG7S, which has Cartesian coordinates
 
         X (km):                  0.1134672919694E+04
         Y (km):                 -0.3681578903408E+04
         Z (km):                 -0.5066204512612E+04
 
      and planetodetic coordinates
 
         Longitude (deg):       -72.8705555556000
         Latitude  (deg):       -52.9350000000000
         Altitude   (km):         0.2200000000033E-01
 
      These planetodetic coordinates are expressed relative to
      a reference spheroid having the dimensions
 
         Equatorial radius (km):  6.3781370000000E+03
         Polar radius      (km):  6.3567523142452E+03
 
      All of the above coordinates are relative to the frame ITRF93.
 
 
\begindata
 
   FRAME_NDOSL_SG7S_TOPO               =  399101751
   FRAME_399101751_NAME                =  'NDOSL_SG7S_TOPO'
   FRAME_399101751_CLASS               =  4
   FRAME_399101751_CLASS_ID            =  399101751
   FRAME_399101751_CENTER              =  399101751
 
   OBJECT_399101751_FRAME              =  'NDOSL_SG7S_TOPO'
 
   TKFRAME_399101751_RELATIVE          =  'ITRF93'
   TKFRAME_399101751_SPEC              =  'ANGLES'
   TKFRAME_399101751_UNITS             =  'DEGREES'
   TKFRAME_399101751_AXES              =  ( 3, 2, 3 )
   TKFRAME_399101751_ANGLES            =  ( -287.1294444444000,
                                            -142.9350000000000,
                                             180.0000000000000 )
 
\begintext
 
 
Definitions file ksat_punta_arenas_sg7s_1751.pinpoint
--------------------------------------------------------------------------------
 
Notional PINPOINT Definitions file for KSAT Punta Arenas Ground Station.
========================================================================
 
Brian T. Carcich, Latchmoor Service, INC.
 
See file [ndosl_190716_v02.cmt] at URL:
  https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/stations/
 
 
Caveats
========================================================================
 
- Station Code (SG7S) and NASA Number (1751) are notional
- Lat/Lon values are low-resolution and may be off by dozens of metres
- Elevation value is also low-resolution
- Elevation value assumes WGS84 is coincident with sea level
- WGS84 model data (BODY399_RADII) used by PINPOINT are in this file
  - PCK passed to PINPOINT on command-line has no data
 
 
Table 1: WGS-84 Ellipsoid
========================================================================
 
   From "SECT. D1: SPHEROID CONSTANTS" in [1]:
 
      --  --------  ------------  -------------
      NO  SPHEROID  R (M)         1/F
      --  --------  ------------  -------------
      25  WGS84     6378137.0000  298.257223563
      --  --------  ------------  -------------
 
   Spheroid RADII corresponding to the values above are:
 
begindata
 
      BODY399_RADII     = ( 6378.137  6378.137  6356.75231424518 )
 
begintext
 
 
Table 2: GEODETIC POSITIONS ON WORLD GEODETIC SYSTEM 1984
========================================================================
 
   ----  ----  --------------  --------------  --------  ------------------------
   STDN  NASA     LATITUDE       E. LONGITUDE   HEIGHT   NOTE
   CODE  NMBR   DEG AMIN ASEC   DEG AMIN ASEC   METERS
   ----  ----  --------------  --------------  --------  ------------------------
   SG7S  1751  -52 56 06.0000  -70 52 14.0000    22.000  eoportal.org/satellite-missions/gnomes
 
 
 
 
Table 3: STATION LOCATION AND EQUIPMENT
========================================================================
 
   ----  ----  ----------------------------------------------------------------
   STDN  NASA  LOCATION;
   CODE  NMBR  EQUIPMENT
   ----  ----  ----------------------------------------------------------------
   SG7S  1751  KSAT Punta Arenas, Chile; S/X-band
 
 
PINPOINT Inputs
=======================================================
 
begindata
   SITES                   += 'NDOSL_SG7S'
   NDOSL_SG7S_CENTER     = 399
   NDOSL_SG7S_FRAME      = 'ITRF93'
   NDOSL_SG7S_IDCODE     = 399101751
   NDOSL_SG7S_LATLON     = ( -52.9350000000, -72.8705555556,  0.022000 )
   NDOSL_SG7S_TOPO_FRAME = 'NDOSL_SG7S_TOPO'
   NDOSL_SG7S_TOPO_ID    = 399101751
   NDOSL_SG7S_UP         = 'Z'
   NDOSL_SG7S_NORTH      = 'X'
begintext
 
 
End of PINPOINT inputs.
=======================================================
 
begintext
 
[End of definitions file]
 
