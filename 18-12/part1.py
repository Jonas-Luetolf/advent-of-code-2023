from helper import *
from collections import deque


DIRS = {"U": -1j, "D": 1j, "L": -1, "R": 1}


def to_complex(d, l):
    return DIRS[d] * int(l)


inp = list(map(lambda x: x.split(), read_inp("input.txt")))
steps = [to_complex(x[0], x[1]) for x in inp]
border = []

curr = 1000 + 1000j
for step in steps:
    border += list(crange(curr, curr + step))
    curr += step

border = list(set(border))


LINES = [[]]
curr_y = 0


x = (
    int((min(border, key=lambda x: x.real) + max(border, key=lambda x: x.real)).real)
    // 2
)
y = (
    int((min(border, key=lambda x: x.imag) + max(border, key=lambda x: x.imag)).imag)
    // 2
)

res = len(border)
start = x + y * 1j
q = deque([start])
visited = set()
while q:
    curr = q.popleft()
    if curr in visited or curr in border:
        continue
    res += 1
    visited.add(curr)
    q.extend(c_neighbors(curr))

print(res)
