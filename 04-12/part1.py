from helper import read_inp

lines = read_inp("input.txt")
lines = list(map(lambda line: line.split(":"), lines))

res = 0

for line in lines:
    numbers = line[1]
    winning, my_nums = numbers.split("|")
    winning, my_nums = winning.strip().split(" "), list(
        filter(("").__ne__, my_nums.strip().split(" "))
    )

    my_winning = list(filter(lambda num: num in winning, my_nums))
    if len(my_winning) > 0:
        res += 2 ** (len(my_winning) - 1)

print(res)
