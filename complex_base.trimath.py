import csv
import os
from complex_base import *

def pcg(c: complex) -> str:
    return f'{int(c.real)} {"+" if c.imag >= 0 else "-"} {int(abs(c.imag))}j'

def main(L1, L2, L3, OUT):
    m = gen_map(max(L1, L2, L3))

    res = []

    for a10 in [x[1] for x in m.items() if (len(bin(x[0])) - 2) <= L1]:
        a = to_bin(a10)
        for b10 in [x[1] for x in m.items() if (len(bin(x[0])) - 2) <= L2]:
            b = to_bin(b10)
            for c10 in [x[1] for x in m.items() if (len(bin(x[0])) - 2) <= L3]:
                c = to_bin(c10)
                o10 = complex(a10 + b10 + c10)
                o = to_bin(o10)
                res.append(
                    [a,b,c,o,a10,b10,c10,o10]
                )

    max_len = max([len(x[3]) for x in res])

    headers = \
        [f'a{x}' for x in range(0, L1)] + \
        [f'b{x}' for x in range(0, L2)] + \
        [f'c{x}' for x in range(0, L3)] + \
        [f'o{x}' for x in range(0, max_len)] + \
        ['', 'a', 'b', 'c', 'o']

    with open(os.path.join(os.path.dirname(__file__), OUT), 'w') as f:
        c = csv.writer(f)
        c.writerow(headers)
        for x in res:
            c.writerow(
                list(x[0].rjust(L1, '0')[::-1]) + # a
                list(x[1].rjust(L2, '0')[::-1]) + # b
                list(x[2].rjust(L3, '0')[::-1]) + # c
                list(x[3].rjust(max_len, '0')[::-1]) + # o
                ['', pcg(x[4]), pcg(x[5]), pcg(x[6]), pcg(x[7])]
            )

if __name__ == '__main__':
    # for i in range(1, 6):
    #     L = i
    #     OUT = f'binmath.{L}.csv'
    #     main(L, OUT)
    main(3, 3, 3, f'binmath.tri.csv')
