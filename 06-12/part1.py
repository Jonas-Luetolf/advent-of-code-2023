from helper import *
from math import sqrt, ceil, floor
from functools import reduce
inp = read_inp("input.txt")

inp = list(map(lambda l:list(map(int,l.split()[1:])),inp))

res=[]

for t, d in zip(inp[0],inp[1]):
    
    # solutions for x (t - x) -d = 0
    x1 = floor((-t + sqrt(t**2 + 4 * (-d))) / -2)
    x2 = ceil((-t - sqrt(t**2 + 4 * (-d))) / -2)

    # number of ints between x1 and x2
    res.append(abs(x1 - x2) - 1)

print(reduce(lambda p,i:p*i,res,1))
