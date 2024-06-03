import csv
import os
from complex_base import *

L = 8 * 2 + 1
OUT = 'repr.csv'

def main():
    M = gen_map(L)
    rows = []
    rows.append(
        ['nb10', 'n_b'] + list(range(L - 1, -1, -1)) + ['real', 'imag', 'dist']
    )
    for n_b_10, pt in M.items():
        b = bin(n_b_10)[2:].rjust(L, '0')
        rows.append(
            [n_b_10, b] +
            list(b) +
            [pt.real, pt.imag] +
            [(pt.real**2 + pt.imag**2) ** 0.5]
        )
    with open(os.path.join(os.path.dirname(__file__), OUT), 'w') as f:
        cw = csv.writer(f)
        cw.writerows(rows)


if __name__ == '__main__':
    main()
