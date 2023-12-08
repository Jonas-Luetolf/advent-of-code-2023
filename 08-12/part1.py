from helper import read_inp

NETWORK = {}
inp = read_inp("input.txt", sep="\n\n")
inst, net = inp[0].replace("L", "0").replace("R", "1"), inp[1]

for node in net.split("\n"):
    splited = node.split()
    key = splited[0]
    next_nodes = (splited[2][1:-1], splited[3][:-1])
    NETWORK.update({key: next_nodes})

steps = 0
actual_node = "AAA"
i = 0

while actual_node != "ZZZ":
    actual_node = NETWORK[actual_node][int(inst[i])]
    steps += 1
    i = (i + 1) % len(inst)

print(steps)
