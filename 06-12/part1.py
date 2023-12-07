from helper import *
from math import sqrt, ceil, floor

inp = read_inp("input.txt")
t = int("".join(inp[0].split()[1:]))
d = int("".join(inp[1].split()[1:]))

# solutions for x (t - x) -d = 0
upper = floor((-t + sqrt(t**2 + 4 * (-d))) / -2)
lower = ceil((-t - sqrt(t**2 + 4 * (-d))) / -2)

# number of ints between x1 and x2
print(abs(upper - lower) - 1)
