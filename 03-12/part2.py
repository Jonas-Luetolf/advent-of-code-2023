from helper import read_inp
from functools import reduce


def get_num_neighbors(array, x, y, check_fun):
    nums = []
    for y_i in range(y - 1, y + 2):
        for x_i in range(x - 1, x + 2):
            if x_i == x and y_i == y:
                pass
            elif (len(array[0]) > x_i >= 0) and (len(array) > y_i >= 0):
                if check_fun(array[y_i][x_i]):
                    nums.append(get_num(array[y_i], x_i))

    return list(set(nums))


def get_num(line, x):
    num = line[x]
    i = 1
    innum_r = True
    innum_l = True
    
    while innum_r or innum_l:
        if line[x - i].isdigit() and x - i >= 0 and innum_l:
            num = line[x - i] + num
        else:
            innum_l = False
        if x + i < len(line) and line[x + i].isdigit() and innum_r:
            num += line[x + i]
        else:
            innum_r = False

        i += 1
    return int(num)


lines = read_inp("input.txt")
res = 0
valid = False
actnum = ""

for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == "*":
            nums = get_num_neighbors(lines, x, y, lambda c: c.isdigit())
            if len(nums) == 2:
                res += reduce(lambda p, i: p * i, nums, 1)
print(res)
