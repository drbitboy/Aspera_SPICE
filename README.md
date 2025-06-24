# ASPERA mission SPICE library

### Language:  Python

### Prerequisite:  spiceypy (Python module)

### Quick start:
```
  git clone -b btc_review_202503 --depth=1 https://github.com/drbitboy/Aspera_SPICE.git
  cd Aspera_SPICE

  make  ### load test kernels, then run all tests
```

### Manifest - Primary files

* geometries/ - top directory of SPICE scripts
  * geometries/xyz/xyz_algorithm.py - library routines
  * geometries/xyz/xyz_call.py - test drivers for xyz_algorithm routines
  * geometries/GeoDriver*.py - large global or near-global tests
  * geometries/artifacts/ - source data for geometries/GeoDriverTest.py script
  * geometries/kernels/ - Test kernels
    * N.B. this will come from another repo, and is not part of this repo
* Makefile - Make script to optinall load kernels, then run all available tests

### Manifest - Other files

* README.md - this file
* geometries/xyz/test_*.py - more test drivers for xyz_algorithm routines
   * Most are tied to obsolete HST SPICE data and are functionally disabled
* geometries/latlon/test_latlon.csv - possibly obsolete
* geometries/test_hst.csv - obsolete
* Test1.csv - test output from geometries/GeoDriverCSV.py test
  * N.B. not part of this repository
* testall.log - test overall output
  * N.B. not part of this repository
* geometries/CSV_Test.csv - unknnown purpose
