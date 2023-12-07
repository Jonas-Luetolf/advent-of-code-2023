from collections import Counter
from helper import *

CARDS = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"][::-1]


def get_type(cards):
    card_type = 7

    if cards == "JJJJJ":
        cards = "AAAAA"
    most_card = Counter("".join(cards).replace("J", "")).most_common()[0][0]

    cards = list(("".join(cards)).replace("J", most_card))
    n = len(set(cards))
    c = Counter(cards).most_common()[0][1]

    if n == 5:
        card_type = 1

    if n == 4:
        card_type = 2

    elif n == 3:
        card_type = 3 + (c - 2)

    elif n == 2:
        card_type = 5 + (c - 3)

    return card_type


def ordernum(cards):
    n = []
    for c in cards:
        n.append(CARDS.index(c))
    return n


inp = read_inp("input.txt")
inp = list(map(lambda x: tuple(x.split()), inp))
inp = list(sorted(inp, key=lambda x: (get_type(x[0]), ordernum(x[0]))))


res = 0
for i, c in enumerate(inp):
    res += (i + 1) * int(c[1])

print(res)
