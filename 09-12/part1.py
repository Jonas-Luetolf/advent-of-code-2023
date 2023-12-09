from helper import read_inp

lines = read_inp("input.txt")
lines = list(map(lambda line: list(map(int, line.split())), lines))


def extrapolate_sequence(sequence: list[int]):
    difs = [sequence]
    while len(set(difs[-1])) != 1 or difs[-1][0] != 0:
        difs.append([difs[-1][i] - difs[-1][i - 1] for i in range(1, len(difs[-1]))])

    while True:
        for i in range(len(difs) - 2, -1, -1):
            difs[i].append(difs[i][-1] + difs[i + 1][-1])
        yield difs[0][-1]


res = 0
for line in lines:
    seq = extrapolate_sequence(line)
    res += next(seq)
print(res)
