s = "+ - - - - +"
m1 = "|  o   o  |"
m2 = "|  o      |"
m3 = "|    o    |"
m4 = "|      o  |"
m5 = "|         |"

dice = [
    [m5, m3, m5],
    [m2, m5, m4],
    [m2, m3, m4],
    [m1, m5, m1],
    [m1, m3, m1],
    [m1, m1, m1]
]


def dice_line(i):
    return [s, *dice[i - 1], s]


def join_row(*rows):
    return ['   '.join(r) for r in zip(*rows)]


def ndice(*ns):
    for line in join_row(*map(dice_line, ns)):

        print("░", line, "░")


def ndice_aside(*ns):
    print("======================  SET ASIDE  ======================")
    for line in join_row(*map(dice_line, ns)):

        print("▓", line, "▓")
