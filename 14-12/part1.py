from helper import *

inp = read_inp("input.txt")
inp = list(map(list,inp))
inp=list(map(lambda x: "".join(x),transpose(inp)))


res = 0
def sort_column(line,top):
    lines = line.split("#")
    lines = list(map(lambda x: "".join(sorted(x,reverse=top)),lines))
    return "#".join(lines)

inp = list(map(lambda x: sort_column(x,True),inp))
inp=transpose(inp)

res = 0
for i,line in enumerate(inp):
    res += (len(inp)-i)*line.count("O")

print(res)
