import csv
import os
from complex_base import *

def pcg(c: complex) -> str:
    return f'{int(c.real)} {"+" if c.imag >= 0 else "-"} {int(abs(c.imag))}j'

def main(L1, L2, OUT):
    m = gen_map(max(L1, L2))

    res = []

    for a10 in [x[1] for x in m.items() if (len(bin(x[0])) - 2) <= L1]:
        a = to_bin(a10)
        for b10 in [x[1] for x in m.items() if (len(bin(x[0])) - 2) <= L2]:
            b = to_bin(b10)
            o10 = complex(a10 + b10)
            o = to_bin(o10)
            res.append(
                [a,b,o,a10,b10,o10]
            )

    max_len = max([len(x[2]) for x in res])

    headers = \
        [f'a{x}' for x in range(0, L1)] + \
        [f'b{x}' for x in range(0, L2)] + \
        [f'o{x}' for x in range(0, max_len)] + \
        ['', 'a', 'b', 'o']

    with open(os.path.join(os.path.dirname(__file__), OUT), 'w') as f:
        c = csv.writer(f)
        c.writerow(headers)
        for x in res:
            c.writerow(
                list(x[0].rjust(L1, '0')[::-1]) +
                list(x[1].rjust(L2, '0')[::-1]) +
                list(x[2].rjust(max_len, '0')[::-1]) +
                ['', pcg(x[3]), pcg(x[4]), pcg(x[5])]
            )

if __name__ == '__main__':
    # for i in range(1, 6):
    #     L = i
    #     OUT = f'binmath.{L}.csv'
    #     main(L, OUT)
    main(3, 7, f'binmath.csv')
