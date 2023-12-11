from clist import *
from helper import *
from itertools import combinations


def find_galaxies(arr:list)->list[complex]:
    galaxies = []
    for c in crange(0, complex(len(arr[0]), len(arr))):
        if cindex(arr, c) == "#":
            galaxies.append(c)
    
    return galaxies


def find_empty(arr:list)->list[int]:
    empty = []
    for y, row in enumerate(arr):
        if set(row) == {"."}:
            empty.append(y)
    return empty


def find_passed(c0:complex, c1:complex, empty_cols:list, empty_rows:list)->int:
    passed = 0
    for row in empty_rows:
        if int(min(c0.imag, c1.imag)) < row < int(max(c0.imag, c1.imag)):
            passed += 1

    for col in empty_cols:
        if int(min(c0.real, c1.real)) < col < int(max(c0.real, c1.real)):
            passed += 1

    return passed


inp = list(map(list, read_inp("input.txt")))
empty_rows, empty_cols = find_empty(inp), find_empty(transpose(inp))
galaxies = find_galaxies(inp)


n = 1000000
res = 0

for comb in list(combinations(galaxies, 2)):
    c_dif = comb[1] - comb[0]
    dif = abs(int(c_dif.real)) + abs(int(c_dif.imag))

    res += dif + find_passed(*comb, empty_cols, empty_rows) * (n - 1)

print(res)
