
def to_b10(n_b: str) -> complex:
    '''translate number in base (i - 1) to complex base 10'''
    c_map = {
        0: lambda n:               0j  + 2**(n/2),
        1: lambda n:  2**((n-1)/2)*1j  - 2**((n-1)/2),
        2: lambda n: -2**(n/2)    *1j  + 0,
        3: lambda n:  2**((n-1)/2)*1j  + 2**((n-1)/2),
        4: lambda n:               0j  - 2**(n/2),
        5: lambda n: -2**((n-1)/2)*1j  + 2**((n-1)/2),
        6: lambda n:  2**(n/2)    *1j  + 0,
        7: lambda n: -2**((n-1)/2)*1j  - 2**((n-1)/2),
    }

    r = 0
    n_b_rev = n_b[::-1]
    for n in range(0, len(n_b)):
        i = int(n_b_rev[n])
        c = n % 8
        r += i * c_map[c](n)

    return r

def gen_map(l = 10, no_complex=False):
    m = {}
    a = 0
    while a < (2**l):
        b = to_b10(bin(a)[2:])
        if not b.imag or b.imag and not no_complex:
            m[a] = b
        a += 1
    return m

# def add_naive(a, b):
#     if len(a) != len(b):
#         l_max = 

