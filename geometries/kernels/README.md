# Kernels for Aspera_SPICE repository
# Kernels folder is modeled off of NAIF website directories
# Files with extensions ending in 't' are text kernels,
# otherwise they are binary kernels
# Folder contents:


## CK
- orientation (attitude) of a spacecraft or other structure
- file extension(s): .bc, .tc 

## EK (currently empty)
- mission events

## FK
- reference frame specification
- file extension(s): .tf

## IK (currently empty)
- instrument geometry

## LSK
- leapseconds
- file extension(s): .tls

## MK
- metakernels
- file extension(s): .mk

## PCK
- binary and text form of planetary constants containing only orientation
- file extension(s): .tpc, .bpc

## SCLK
- spacecraft clock coefficients
- file extension(s): .tsc

## SPK
- ephemeris for vehicles, planets, satellites, comets, asteroids
- file extension(s): .bsp

## unused
- "dump" for kernels that are outdated or unused in the metakernels

# Provenance

The files under this directory comprise kernels used to (py)test the
algorithms of the Aspera_SPICE repository.

### Location within the Aspera_SPICE repository:
* /geometries/kernels/

### Original source
* Github repo:   https://github.com/drbitboy/Aspera_SPICE_kernels.git
* Commit:  0e24bc30f459aca92ba7c9b4ca2fd356e494b206
* Author: Brian Carcich <briantcarcich@gmail.com>
* Date:   Wed May 21 10:29:26 2025 -0400
* Branch (as of that date):  kernel_updates_202514

These kernels and scripts may be modified after that data,
but that was the original source for the added files.
