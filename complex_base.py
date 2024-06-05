import math

# https://math.stackexchange.com/a/1210892/402507
def _cdiv(a: complex) -> tuple[complex, int]:
    n = a.real
    m = a.imag
    oddity = n % 2 + m % 2
    if oddity != 1:
        return (
            ((m - n) / 2) - ((n + m) / 2) * 1j,
            0
        )
    else:
        return (
            ((m - n + 1) / 2) - ((n + m - 1) / 2) * 1j,
            1
        )

def to_bin(n: int) -> str:
    r = ''
    while n != 0:
        quotient, remainder = _cdiv(n)
        r += str(remainder)
        n = quotient
    return r[::-1]

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

def gen_map(l = 10, no_complex=False, start=0):
    m = {}
    a = start
    while a < (2**l):
        b = to_b10(bin(a)[2:])
        if not b.imag or b.imag and not no_complex:
            m[a] = b
        a += 1
    return m

def calc_min_max_distance_for_digits(l):
    m = gen_map(l, start=2**(l-1))
    ds = [(x.real**2 + x.imag**2)**0.5 for x in m.values()]
    return min(ds), max(ds)

# Random thought:
# is there a correlation between adding more digits in binary and the max distance from origin?
#  1: 1
#  2: √2
#  3: √5
#  4: √13
#  5: √26
#  6: √65
#  7: √130
#  8: 2√65 = √260
#  9: √565
# 10: √1130
# 11: √2285
# 12: √4637
# 13: √9274
# 14: √18,785
# 15: √37,570
# 16: √75,140
# Upon investigation - probably not, but it was a fun exersize
# mm = {
#     k: calc_min_max_distance_for_digits(k)
#     for k in range(1, 17)
# }

def gen_add_list_through(len_a, len_b):
    m_a = gen_map(len_a).values()
    m_b = gen_map(len_b).values()
    ads = []
    for a10 in m_a:
        a = to_bin(a10)
        for b10 in m_b:
            b = to_bin(b10)
            o10 = a10 + b10
            o = to_bin(o10)
            ads.append((a, b, o))
    return ads

def max_gen_add_list(len_a, len_b):
    return max([len(x[2]) for x in gen_add_list_through(len_a, len_b)])
