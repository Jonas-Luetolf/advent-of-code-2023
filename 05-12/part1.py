from helper import *


class rangemap:
    def __init__(self, dest, src, l) -> None:
        self.dest = dest
        self.src = src
        self.l = l

    def map(self, num):
        if num >= self.src and num < self.src + self.l:
            num = self.dest + (num - self.src)

        return num


def map_num(num: int, nummaps: list[list[rangemap]]):
    for nummap in nummaps:
        for maprange in nummap:
            if num != maprange.map(num):
                num = maprange.map(num)
                break

    return num


inp = read_inp("input.txt", sep="\n\n")
seeds = list(map(int, inp[0].split()[1:]))
maps = inp[1:]

nummaps = []

for nummap in maps:
    map_lines = nummap.split("\n")[1:]
    map_lines = list(map(lambda r: r.split(), map_lines))
    rangemaps = []

    for map_line in map_lines:
        map_line = list(map(int, map_line))
        rangemaps.append(rangemap(*map_line))
    nummaps.append(rangemaps)


print(min(list(map(lambda n: map_num(n, nummaps), seeds))))
