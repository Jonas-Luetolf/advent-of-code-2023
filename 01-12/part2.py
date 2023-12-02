from helper import read_inp

word_nums = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

nums_nums = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}


def first_last(line, items):
    occurrences = []
    for key, val in items.items():
        if line.find(key) != -1:
            occurrences.append((line.find(key), val))
        if line.rfind(key) != -1:
            occurrences.append((line.rfind(key), val))

    occurrences = list(set(occurrences))
    occurrences = sorted(occurrences)
    if len(occurrences) == 0:
        return None
    return occurrences[0], occurrences[-1]


lines = read_inp("input.txt")


res = 0
for line in lines:
    nums = []

    if first_last(line, word_nums) != None:
        nums += [*first_last(line, word_nums)]
    if first_last(line, nums_nums) != None:
        nums += [*first_last(line, nums_nums)]

    nums = sorted(nums)
    res += int(str(nums[0][1]) + str(nums[-1][1]))


print(res)
