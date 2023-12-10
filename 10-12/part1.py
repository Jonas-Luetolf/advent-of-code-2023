from helper import read_inp
from enum import Enum
import cmath


class dirs(Enum):
    N = -1j
    S = 1j
    W = -1
    E = 1

PIPES = {
        "|": [dirs.N,dirs.S],
        "-": [dirs.W,dirs.E],
        "L": [dirs.N,dirs.E],
        "J": [dirs.N,dirs.W],
        "7": [dirs.W,dirs.S],
        "F": [dirs.S,dirs.E]
}

def cindex(arr,c):
    return arr[int(c.imag)][int(c.real)]


def get_start_pip(arr):
    pos = 0  
    for y,line in enumerate(arr):
        for x,i in enumerate(line):
            if i == "S":
                pos = complex(x,y)
    spipe_dirs = []
    for n,d in zip([pos -1, pos+1, pos-1j,pos+1j],[dirs.W,dirs.E,dirs.N,dirs.S]):
        if dirs(d.value*-1) in PIPES[cindex(inp,n)]:
            spipe_dirs.append(d)
    spipe = [key for key,value in PIPES.items() if set(value) == set(spipe_dirs)][0] 
    return spipe,pos





inp = list(map(list, read_inp("input.txt")))
startpipe,startpos = get_start_pip(inp)
inp[int(startpos.imag)][int(startpos.real)] = startpipe


steps = 0
lcurr = startpos 
rcurr = startpos
ldir = PIPES[startpipe][0]
rdir = PIPES[startpipe][1]

while (lcurr != rcurr or startpos == lcurr):
    lcurr = lcurr + ldir.value
    rcurr = rcurr + rdir.value
    ldir = [d for d in PIPES[cindex(inp,lcurr)] if d not in [dirs(ldir.value*-1)]][0]
    rdir = [d for d in PIPES[cindex(inp,rcurr)] if d not in [dirs(rdir.value*-1)]][0]
    steps +=1

print(steps)
