from helper import read_inp
from math import lcm

NETWORK = {}

inp = read_inp("input.txt", sep="\n\n")
inst, net = inp[0].replace("L", "0").replace("R", "1"), inp[1]

for node in net.split("\n"):
    splited = node.split()
    key = splited[0]
    next_nodes = (splited[2][1:-1], splited[3][:-1])
    NETWORK.update({key: next_nodes})

steps = 0


actual_nodes = [i for i in NETWORK.keys() if i[-1] == "A"]
cycles = []

for j, node in enumerate(actual_nodes):
    fz = None
    fi = 0

    actnode = node
    i = 0

    while True:
        while True:
            actnode = NETWORK[actnode][int(inst[i % len(inst)])]
            i += 1
            if actnode[-1] == "Z":
                break

        if fz == None:
            fz = actnode
            fi = i

        elif fz == actnode:
            break

    cycles.append(i - fi)

print(lcm(*cycles))
