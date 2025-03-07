import spiceypy as sp

def main():

    kernel = 'M82spk.bsp' # 'nh_stars1.bsp'
    sp.furnsh(kernel)

    ids = sp.spkobj(kernel)

    print(ids)

    '''
    utcBeg = '2025 JUN 01 00:00:01'
    etBeg = sp.str2et(utcBeg)

    print(etBeg)
    '''

    sp.unload(kernel)

main()