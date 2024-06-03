import matplotlib.pyplot as plt
import numpy as np
from complex_base import *

L = 8 * 2 + 1

def main():
    M = gen_map(L)
    pts_x = [x.real for x in M.values()]
    pts_y = [x.imag for x in M.values()]

    # t_x = range(int(min(pts_x) - 1), int(max(pts_x) + 2))
    # t_y = range(int(min(pts_y) - 1), int(max(pts_y) + 2))
    # plt.xticks(
    #     t_x, [str(x) for x in t_x],
    #     size='large'
    # )
    # plt.xlabel('Real', size='large')

    # plt.yticks(
    #     t_y, [str(x) for x in t_y],
    #     size='large'
    # )
    # plt.ylabel('Imag', size='large')

    plt.scatter(
        pts_x, pts_y
    )

    # for n_b_10, pt in M.items():
    #     plt.annotate(
    #         bin(n_b_10)[2:].rjust(L, '0'),
    #         (pt.real, pt.imag),
    #         rotation=45
    #     )

    plt.grid(True, 'major',
        linestyle='-.')
    # plt.grid(True, 'both',
    #     linestyle='-.')
    plt.show()


if __name__ == '__main__':
    main()
