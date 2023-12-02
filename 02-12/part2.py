from helper import read_inp
from functools import reduce


MAX_CUBES = {"red": 12, "green": 13, "blue": 14}

res = 0
lines = read_inp("input.txt")


def power(subsets: list) -> int:
    min_cubes = {"red": 0, "blue": 0, "green": 0}

    # combine subsets
    cubes = reduce(lambda s, i: s + i, subsets, [])

    # find max per color
    for i in cubes:
        if int(i[0]) > min_cubes[i[1]]:
            min_cubes[i[1]] = int(i[0])

    return reduce(lambda p, i: p * i, list(min_cubes.values()))


for line in lines:
    num = int((line.split(":")[0]).split(" ")[1])

    # split subsets
    subsets = (line.split(":")[1]).split(";")

    # split cube numbers
    subsets = list(map(lambda subset: subset.split(","), subsets))
    subsets = [
        list(map(lambda cubes: tuple(cubes.strip().split(" ")), subset))
        for subset in subsets
    ]

    res += power(subsets)

print(res)
