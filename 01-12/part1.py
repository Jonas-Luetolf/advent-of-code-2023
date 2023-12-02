from helper import read_inp


def get_num(line: str) -> int:
    nums = [c for c in line if c.isdigit()]
    return int(nums[0] + nums[-1])


lines = read_inp("input.txt")

nums = [get_num(line) for line in lines]

print(nums)
print(sum(nums))
