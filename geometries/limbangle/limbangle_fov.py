import spiceypy as sp

mkfile = './kernels/mk/asperaMetaKernel2.tm'
sp.furnsh(mkfile)

# using 2025 for ASPERA
UTC = '2025-06-01T00:00:01'

sp.getfov('ASP_SOLAR')