from helper import read_inp

MAX_CUBES = {"red": 12, "green": 13, "blue": 14}

res = 0
lines = read_inp("input.txt")


def validate(subsets: list) -> bool:
    for subset in subsets:
        for cubes in subset:
            if int(cubes[0]) > MAX_CUBES[cubes[1]]:
                return False

    return True


for line in lines:
    num = int((line.split(":")[0]).split(" ")[1])

    # split subsets
    subsets = (line.split(":")[1]).split(";")

    # split cube numbers
    subsets = list(map(lambda subset: subset.split(","), subsets))
    subsets = [
        list(map(lambda cubes: tuple(cubes.strip().split(" ")), subset))
        for subset in subsets
    ]

    if validate(subsets):
        res += num

print(res)
