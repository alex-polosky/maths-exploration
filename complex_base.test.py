import sys
from complex_base import *

_stderr = sys.__stderr__
ERRORED = False
# def _newerr(*a, **kw):
#     _stderr(*a, **kw)
#     ERRORED = True
# sys.stderr = _newerr

def test_to_b10():
    global ERRORED
    exp = {
        1: '000000001',
        2: '000001100',
        3: '000001101',
        4: '111010000',
        5: '111010001',
        6: '111011100',
        7: '111011101',
        8: '111000000',
        9: '111000001',
        10: '111001100',
        11: '111001101',
        12: '100010000',
        13: '100010001',
        14: '100011100',
        15: '100011101',
        16: '100000000',
    }

    results = []
    for b10, cb in exp.items():
        res = to_b10(cb)
        results.append([cb, '\t', b10, '\t', res])
        if b10 != res:
            _stderr.write(f'err: {b10}\n')
            ERRORED = True

    for r in results:
        print(*r)

def test_to_bin():
    global ERRORED
    exp = {
                '1': 1,
             '1100': 2,
             '1101': 3,
        '111010000': 4,
        '111010001': 5,
        '111011100': 6,
        '111011101': 7,
        '111000000': 8,
        '111000001': 9,
        '111001100': 10,
        '111001101': 11,
        '100010000': 12,
        '100010001': 13,
        '100011100': 14,
        '100011101': 15,
        '100000000': 16,
    }

    results = []
    for cb, b10 in exp.items():
        res = to_bin(b10)
        results.append([b10, '\t', cb, '\t', res])
        if cb != res:
            _stderr.write(f'err: {cb}\n')
            ERRORED = True

    for r in results:
        print(*r)


if __name__ == '__main__':
    test_to_b10()
    test_to_bin()
    print('')
    if ERRORED:
        print('Errors found!')
    else:
        print('All clean!')
