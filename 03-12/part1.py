from helper import read_inp

is_symbol = lambda c: (not c.isdigit()) and (c != ".")


def check_neighbors(array, x, y, check_fun):
    for y_i in range(y - 1, y + 2):
        for x_i in range(x - 1, x + 2):
            if x_i == x and y_i == y:
                pass
            elif (len(array[0]) > x_i >= 0) and (len(array) > y_i >= 0):
                if check_fun(array[y_i][x_i]):
                    return True
    return False


lines = read_inp("input.txt")
res = 0
valid = False
actnum = ""
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if not c.isdigit():
            if valid:
                res += int(actnum)
            actnum = ""
            valid = False
        else:
            actnum += c
            if check_neighbors(lines, x, y, is_symbol):
                valid = True

print(res)
