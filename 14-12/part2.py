from helper import *

inp = read_inp("input.txt")
inp = list(map(list, inp))
inp = list(map(lambda x: "".join(x), inp))


def str_transpose(inp):
    return list(map(lambda x: "".join(x), transpose(inp)))


def sort_column(line, top):
    lines = line.split("#")
    lines = list(map(lambda x: "".join(sorted(x, reverse=top)), lines))
    return "#".join(lines)


def cycle(inp):
    for top in [True, True, False, False]:
        inp = list(map(lambda x: sort_column(x, top), str_transpose(inp)))

    return inp


start_inp = inp
n = 1000000000
res = 0

combs = []
p = 1
inp = cycle(inp)
while not (inp in combs) and p < 1000000000:
    combs.append(inp)
    inp = cycle(inp)
    p += 1

offset = combs.index(inp) + 1

for i in range((n - offset) % (p - offset)):
    inp = cycle(inp)

for i, line in enumerate(inp):
    res += (len(inp) - i) * line.count("O")

print(res)
