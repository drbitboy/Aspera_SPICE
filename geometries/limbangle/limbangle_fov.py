import spiceypy as sp

mkfile = './geometries/kernels/mk/asperaMetaKernel2.tm'
sp.furnsh(mkfile)

# using 2025 for ASPERA
UTC = '2025-06-01T00:00:01'

print(sp.getfov(sp.bodn2c('ASP_SOLAR'),99,99,99))
