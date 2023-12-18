def read_inp(filename, dtype=str, sep="\n"):
    with open(filename, "r") as f:
        inp = f.read().rstrip().split(sep)
    return list(map(dtype, inp))


def binary_search(item, sorted_list):
    lower = 0
    upper = len(sorted_list)
    middel = int(lower + upper // 2)

    if sorted_list[middel] == item:
        return middel
    elif item < sorted_list[middel] and item >= sorted_list[lower]:
        return binary_search(item, sorted_list[lower:middel])
    elif item > sorted_list[middel] and item <= sorted_list[upper - 1]:
        return binary_search(item, sorted_list[middel + 1 : upper]) + middel + 1
    else:
        raise ValueError(f"{item} not in list")


def seperate_by_k(l, k=0):
    if k not in l:
        l.append(k)
    l.sort()
    l_lower = l[: binary_search(k, l)]
    l_upper = l[binary_search(k, l) + 1 :]
    return l_lower, l_upper


def crange(c1, c2):
    y_step = int(
        abs(c2.imag - c1.imag) // (c2.imag - c1.imag) if (c2.imag - c1.imag) != 0 else 1
    )
    x_step = int(
        abs(c2.real - c1.real) // (c2.real - c1.real) if (c2.real - c1.real) != 0 else 1
    )

    for y in range(int(c1.imag), int(c2.imag) + y_step, y_step):
        for x in range(int(c1.real), int(c2.real) + x_step, x_step):
            yield complex(x, y)


def cindex(arr, c):
    return arr[int(c.imag)][int(c.real)]


def c_neighbors(c):
    n = (
        list(crange(c - 1 - 1j, c + 1 - 1j))
        + list(crange(c - 1, c + 1))
        + list(crange(c - 1 + 1j, c + 1 + 1j))
    )
    n.remove(c)
    return n
