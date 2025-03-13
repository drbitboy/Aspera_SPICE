"""Usage:

  python rotation_compare.py [--verbose] [--bits=51]

Expected output with not command-line arguments:

  Kernels compared:
    ../kernels/ck/aspera_test1.bc
    ../kernels/ck/cdr_3_ck.bc
  absolute tolerance:  4.440892098500626e-16 (~ 51.0000 bits)
  Value count:  5764 values; 1441 quaternions
  Mismatches:  0

"""
import os
import sys
import math
import spiceypy as sp
from pytest import approx

def main():
  sclk1 = 8020944700000.000000      ### from ckbrief -t -dpsclk blah.bc
  sclk2 = 8021808700000.000000      ### - same
  cktol = 10090.0                   ### 1009ms
  scref = -1999000                  ### ASPERA_SPACECRAFT ref frame
  ref = 'J2000'                     ### Base ref frame
  quatslists = list()               ### List of lists
  pydir = os.path.dirname(__file__) ### Directory of this script
  cks ='../kernels/ck/aspera_test1.bc ../kernels/ck/cdr_3_ck.bc'.split()
  for ckrelpath in cks:
    ckpath = os.path.join(pydir, ckrelpath)  ### build path to ck
    sp.furnsh(ckpath)                        ### Load CK
    quats = list()                           ### Create list of values
    sclkdp = sclk1                           ### Initial SCLKDP
    while sclkdp <= sclk2:                   ### Loop over SCLK range
      c = sp.ckgp(scref,sclkdp,cktol,ref)[0]   ### C-matrix from CK
      quats.extend(list(sp.m2q(c)))            ### Extend list with quat
      sclkdp += 600000.0                       ### Add a minute to SCLK
    quatslists.append(quats)                 ### Append to list of lists
    sp.unload(ckpath)                        ### Unoad CK

  ### default tolerance is 2**-51
  ### - optional override with command-line option --bits=N
  ### - convert bits to absolute tolerance for pytest.approx
  argbits = ([51] + [arg[7:] for arg in sys.argv[1:]
                     if arg.startswith("--bits=")]
            ).pop()
  abstol = 2.0 ** (-float(argbits))
  bits = math.log(abstol) / math.log(0.5)

  ### Compare values of first list in list of lists to subsequent values
  arrA = [approx(v,abs=abstol) for v in quatslists[0]]
  L = len(arrA)
  assert not (L%4),'List does not comprise quaternion elements'
  ckA = cks[0]

  ### Loop over subsequent lists from subsequent CKs
  for arrB,ckB in zip(quatslists[1:],cks[1:]):

    print(f"Kernels compared:\n  {ckA}\n  {ckB}")
    print(f"absolute tolerance:  {abstol} (~ {bits:.4f} bits)")
    assert len(arrB) == L,'Value lists have different lengths'
    print(f"Value count:  {L} values; {L>>2} quaternions")

    ### Store values and offset to any mismatches
    mismatches = [tup for tup in zip(arrA,arrB,range(L))
                  if not (tup[0]==tup[1])
                 ]

    if "--verbose" in sys.argv[1:]:
      for abo in mismatches: print(abo)
    print(f"Mismatches:  {len(mismatches)}")

if __name__ == "__main__":
    main()
