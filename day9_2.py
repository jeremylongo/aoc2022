from enum import IntEnum

data = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""


data = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""



data = """D 1
L 2
D 2
L 1
R 1
D 1
R 2
U 1
R 1
D 2
R 1
L 2
U 1
D 2
R 1
L 2
R 1
U 2
D 2
L 1
U 2
R 2
D 1
R 2
D 1
U 2
D 2
L 1
U 1
R 1
D 1
U 1
D 1
U 2
L 2
R 1
U 1
R 2
L 2
U 2
R 1
L 1
U 1
L 2
R 1
D 1
L 1
D 2
U 1
D 1
R 1
L 2
D 1
R 2
L 2
U 1
D 2
R 2
D 1
U 1
R 2
D 1
L 1
U 2
R 2
D 1
U 2
R 1
D 2
R 1
D 1
U 2
R 2
U 1
R 1
U 1
L 1
U 2
D 1
R 2
D 2
R 2
D 1
L 2
D 2
L 1
R 1
U 1
D 2
L 2
D 2
L 1
D 2
R 1
D 1
R 2
L 2
R 2
D 2
R 1
D 2
R 2
U 2
L 2
R 1
U 1
R 1
U 1
D 1
U 1
R 2
L 1
R 1
D 2
U 3
R 1
L 2
D 1
R 3
U 1
D 2
R 1
D 1
R 2
L 1
R 2
L 2
D 3
R 3
D 1
U 2
D 2
R 1
D 2
R 1
L 3
D 1
L 1
R 2
D 3
R 2
D 3
R 3
L 2
U 3
D 3
L 2
R 3
L 1
U 1
L 2
D 2
U 1
D 2
U 1
D 2
R 1
U 1
D 2
U 1
L 1
R 2
L 2
D 3
U 2
L 3
D 2
U 1
D 3
L 1
U 1
D 2
R 2
U 1
L 2
D 3
L 3
D 3
U 1
R 1
U 2
D 1
R 3
L 1
D 1
U 3
D 1
L 2
U 1
L 3
D 2
L 2
R 1
L 3
U 3
R 3
U 1
R 2
D 1
L 3
U 3
D 3
L 2
D 1
U 2
D 2
U 2
R 3
U 2
L 1
U 1
R 2
L 3
D 3
U 3
R 1
L 1
U 1
D 1
U 2
R 1
D 3
L 1
R 3
L 4
D 3
R 2
U 3
R 1
L 4
R 1
L 3
R 3
U 2
D 1
L 3
D 4
U 4
L 3
U 4
R 4
L 1
R 4
D 1
R 1
L 3
R 3
L 1
R 4
D 2
L 3
D 2
U 1
R 3
D 2
L 3
R 4
L 3
U 3
D 3
R 1
D 2
U 4
L 1
R 1
L 4
R 3
U 1
L 4
R 1
U 3
R 1
L 1
U 3
R 3
U 2
R 2
L 4
U 1
R 1
D 3
L 2
D 1
L 3
R 3
D 3
L 4
U 2
L 3
U 4
L 2
U 2
D 4
L 3
D 1
U 2
L 3
R 4
U 1
L 4
R 4
L 3
U 2
D 4
L 1
R 3
D 2
L 3
U 1
L 3
U 4
R 2
U 2
R 1
D 2
L 4
R 3
D 2
L 3
U 3
D 3
L 1
D 4
R 3
U 1
R 3
L 1
U 3
R 2
D 3
L 3
U 3
L 3
D 5
U 4
L 5
D 2
R 1
D 2
U 5
R 1
U 2
D 2
R 4
U 2
L 3
U 2
R 5
D 4
L 3
U 3
D 1
R 2
L 3
U 1
R 5
D 1
U 2
R 1
U 3
L 2
U 5
R 4
D 5
L 4
D 4
L 2
U 4
R 5
L 1
D 1
R 2
U 2
D 5
R 2
U 4
L 3
D 2
R 4
L 1
R 1
L 2
U 4
D 4
R 5
D 3
R 1
D 4
L 4
U 5
L 2
U 2
L 3
R 4
U 5
L 4
U 2
D 1
R 2
U 4
L 1
U 3
R 1
U 5
D 5
U 4
D 3
L 3
U 3
D 2
U 4
R 3
D 1
U 5
D 3
R 1
U 2
R 1
D 4
R 4
L 4
U 1
L 5
R 3
D 2
U 2
L 5
R 1
L 1
U 3
D 4
R 5
L 4
D 5
L 2
U 1
D 1
U 3
R 4
D 4
L 4
U 3
L 2
D 2
L 5
U 1
R 6
U 4
R 3
D 2
R 6
D 2
R 6
L 3
R 4
L 3
D 5
U 2
R 5
L 5
R 4
U 6
R 6
D 1
U 4
D 4
L 3
D 2
U 5
R 2
U 5
D 2
U 3
R 2
D 5
R 2
D 6
R 1
U 5
D 2
L 6
U 2
L 4
R 6
L 6
D 6
L 3
D 5
L 1
R 5
D 4
L 4
U 1
R 3
D 6
R 6
U 2
R 4
D 1
R 4
U 4
L 6
U 6
D 6
R 2
D 2
L 4
R 6
L 1
U 5
D 4
U 4
R 3
U 1
D 3
R 6
D 4
U 5
R 3
D 5
R 5
D 4
U 4
D 3
U 6
L 1
D 4
U 6
L 3
R 3
D 6
U 4
R 3
L 3
R 1
D 6
R 4
U 2
R 6
L 3
D 3
L 4
R 3
L 4
R 3
U 4
R 3
D 4
R 6
D 2
U 1
D 2
L 3
D 4
L 1
D 5
L 6
U 4
L 7
R 6
U 7
R 7
L 5
D 1
U 3
R 6
U 6
R 2
U 5
R 4
U 7
R 1
L 3
D 7
L 4
D 6
U 1
L 1
R 3
D 2
L 5
R 1
U 1
L 1
R 6
L 6
D 2
U 3
L 6
R 6
L 3
D 3
R 2
L 1
U 5
R 6
D 2
L 5
U 1
D 4
R 3
L 6
R 2
L 4
D 4
R 5
D 3
R 2
L 5
U 7
D 5
L 3
R 2
D 5
U 5
D 2
U 2
L 2
R 5
L 2
D 5
R 3
U 4
R 4
D 1
L 6
U 2
R 7
L 3
U 4
D 2
R 5
L 6
R 7
L 1
U 5
L 3
U 7
D 6
R 3
D 3
U 7
L 4
R 2
U 1
L 1
R 6
D 5
R 7
U 4
D 2
R 2
D 4
L 1
U 4
D 2
R 2
D 5
U 7
D 1
U 7
R 3
U 5
L 1
R 7
L 2
R 5
U 5
R 5
D 4
U 5
L 7
D 3
R 5
L 3
R 1
U 8
L 4
U 3
D 4
U 1
L 2
D 5
L 5
D 4
U 3
L 2
R 3
D 6
L 4
U 3
R 1
U 1
D 3
R 5
D 4
L 7
U 7
R 7
L 6
D 7
U 5
L 2
U 4
R 8
L 4
U 4
R 5
U 1
R 1
D 7
R 6
L 8
R 1
D 4
U 5
R 6
L 3
R 7
L 4
D 7
U 8
R 5
D 5
U 4
L 3
D 4
U 1
L 8
R 8
U 2
L 5
R 7
D 5
L 5
D 3
L 5
U 4
D 1
U 6
R 7
D 5
R 4
D 6
U 4
L 5
D 8
U 5
L 7
D 1
U 8
R 3
U 4
R 5
U 7
R 6
L 3
U 4
L 7
R 5
U 6
L 2
R 2
U 7
R 4
D 2
L 2
D 6
L 5
D 5
L 1
R 5
D 1
U 5
L 8
R 3
D 4
R 2
U 2
L 5
D 4
U 7
D 9
R 9
U 9
R 3
L 2
D 8
U 6
L 1
R 1
D 4
L 9
R 9
L 3
U 4
D 7
U 9
D 5
R 8
D 6
R 9
U 2
R 2
U 8
R 5
U 6
L 8
D 7
L 2
U 3
R 3
U 6
L 5
R 4
D 6
U 6
R 6
D 5
U 5
D 6
L 4
D 2
U 6
L 8
U 3
D 6
U 1
L 7
D 6
R 3
D 7
U 6
D 4
U 5
R 3
D 7
L 5
U 6
L 6
R 2
D 7
L 7
U 5
D 9
R 6
L 9
R 1
L 6
U 5
R 4
U 7
L 2
U 5
L 9
U 3
R 2
L 5
R 2
U 6
L 3
D 7
R 9
D 3
L 4
R 2
D 8
L 6
D 9
L 5
D 1
R 8
D 4
U 5
L 7
D 2
R 2
L 7
D 6
L 7
R 1
D 4
U 3
D 3
U 8
R 8
L 3
D 8
U 7
R 4
D 9
L 3
U 10
L 4
D 4
R 7
U 1
L 10
U 10
R 9
U 3
L 3
R 1
D 10
L 4
U 9
L 4
U 7
L 8
R 7
D 1
U 3
L 3
U 2
R 4
U 5
D 9
L 5
U 10
L 2
U 1
L 7
D 9
L 8
R 10
D 7
U 9
L 4
U 10
L 3
U 1
D 1
L 1
D 6
U 8
R 8
L 6
U 9
L 3
U 6
R 6
U 3
R 7
U 2
D 4
L 4
R 8
D 3
R 8
U 2
R 3
D 6
U 4
R 9
L 4
D 4
L 6
R 2
D 10
L 7
R 9
L 7
D 8
R 2
D 2
U 9
R 2
U 1
R 10
U 1
D 2
U 10
D 10
U 5
R 3
U 5
R 10
L 3
R 5
U 5
L 4
D 3
L 7
D 3
U 10
R 7
L 3
D 2
L 1
D 1
L 7
R 2
L 10
D 6
R 4
L 8
R 9
D 5
L 2
D 4
R 1
L 4
R 8
D 5
R 10
D 1
L 10
D 11
L 10
R 4
L 3
D 1
U 4
L 9
D 6
U 2
R 4
L 2
U 5
D 1
R 6
L 5
U 7
D 2
R 5
D 9
R 11
U 9
D 9
R 2
L 9
D 4
U 7
L 10
D 7
U 4
D 1
U 4
D 10
L 8
D 3
L 8
D 8
R 7
D 10
R 5
U 1
L 11
D 2
L 11
U 4
L 8
D 10
U 3
D 11
R 10
L 1
D 2
U 11
L 4
U 2
L 6
D 7
R 10
L 2
D 7
R 9
U 6
D 5
R 9
U 1
D 3
R 8
D 7
L 3
D 8
U 4
D 4
R 8
L 7
R 1
D 3
U 7
D 4
L 10
R 1
D 6
R 1
L 5
D 2
L 9
R 1
U 5
D 4
U 11
L 6
R 11
D 11
R 6
U 9
R 1
L 5
U 3
R 10
L 8
R 6
L 2
R 8
D 11
L 5
R 3
L 1
R 3
L 8
R 10
U 2
R 2
D 7
L 9
U 2
L 8
D 3
U 1
L 11
D 1
U 6
L 2
R 7
D 5
R 1
D 11
U 12
D 10
L 11
U 3
D 10
L 6
U 3
D 12
R 4
D 9
R 2
U 12
R 11
L 2
R 7
L 11
U 12
R 12
U 1
R 2
D 8
R 10
U 2
D 8
U 8
D 5
U 10
R 4
U 8
D 4
R 8
D 8
R 2
U 4
L 10
D 2
L 10
R 2
D 9
U 6
L 2
D 10
L 2
D 11
R 11
U 2
L 6
D 3
U 3
R 4
U 9
L 9
R 8
D 5
L 9
U 8
L 11
D 8
R 12
U 1
D 1
U 7
L 11
U 2
L 12
R 11
U 8
R 12
U 11
L 7
U 5
L 4
R 4
D 1
U 6
D 7
U 5
R 5
U 10
D 2
R 9
L 12
D 9
U 6
L 11
D 7
L 6
D 10
L 9
D 11
R 7
D 10
L 1
R 9
D 10
L 1
U 1
L 13
R 10
D 9
L 9
U 7
L 10
R 1
U 12
R 13
U 8
L 9
U 5
L 11
D 11
U 8
R 2
D 2
R 7
D 3
L 3
R 2
L 6
U 11
L 6
U 8
L 11
U 12
L 13
D 4
L 8
U 11
D 9
U 11
D 10
U 4
D 9
L 12
D 6
L 11
U 11
L 1
D 6
R 12
U 9
D 1
L 4
R 9
L 13
R 10
D 9
L 2
R 3
D 10
L 13
R 3
L 8
R 8
L 1
R 5
L 12
D 10
R 6
U 7
R 11
U 11
R 10
D 9
R 12
D 8
U 6
L 8
D 6
L 10
R 2
L 2
D 12
U 12
R 11
L 8
U 2
R 2
L 11
U 11
L 7
D 2
U 2
L 9
D 4
R 2
U 7
D 3
R 1
D 6
U 13
R 11
D 1
U 4
R 9
D 7
L 12
U 12
L 10
U 9
L 1
D 1
U 6
L 1
D 13
U 14
L 2
D 6
U 8
D 8
L 9
D 1
R 11
D 6
L 8
R 11
U 4
L 5
R 5
D 10
U 10
R 7
D 7
L 8
U 9
R 1
L 5
D 4
L 13
D 4
R 14
D 13
R 9
L 13
R 7
L 14
R 12
D 1
U 8
L 10
U 7
D 9
U 7
D 13
L 1
R 1
D 14
L 9
U 5
R 7
U 2
L 11
D 5
U 7
D 1
L 13
U 14
L 1
D 3
R 3
D 1
L 3
U 4
R 14
U 11
R 4
L 13
U 3
R 8
D 5
U 8
L 6
R 14
L 3
D 2
L 5
U 11
R 8
L 11
U 8
D 11
U 14
R 14
L 4
D 10
R 11
U 1
D 4
U 11
D 5
L 5
R 14
U 12
L 1
D 4
R 11
L 5
R 9
U 9
D 2
U 12
D 2
R 8
U 6
L 11
U 8
L 6
U 9
L 5
U 3
D 10
R 10
D 6
U 1
R 13
U 5
R 8
U 11
L 11
D 10
R 11
U 2
D 3
R 10
D 2
L 9
R 7
L 8
U 1
R 6
L 3
D 10
U 14
D 4
U 7
L 6
R 8
U 15
D 14
U 5
D 15
U 2
D 4
L 11
U 8
L 10
U 15
R 8
U 14
D 6
R 9
L 15
R 9
L 11
R 3
D 2
U 10
L 12
D 2
L 5
D 1
R 8
U 7
L 7
D 7
L 15
D 11
U 3
L 4
U 10
L 14
U 10
D 10
U 11
D 1
L 3
R 11
L 3
U 10
L 2
D 8
R 8
L 12
D 15
U 10
L 14
R 4
L 9
R 11
U 10
R 7
D 13
U 11
D 10
R 3
U 6
R 9
L 15
R 11
D 6
R 14
L 7
D 7
L 3
D 13
U 10
R 14
U 2
D 4
U 1
R 1
D 8
R 12
L 15
R 4
L 15
U 13
D 12
L 8
D 1
R 3
U 11
R 3
U 2
R 4
D 15
U 4
L 6
D 6
L 9
D 2
L 15
R 5
U 2
R 7
D 7
U 15
L 4
D 7
R 9
D 11
R 8
L 4
R 6
L 11
U 16
L 10
U 10
L 11
U 9
R 8
U 13
R 13
L 5
R 8
L 12
U 11
L 4
D 10
R 2
U 13
R 4
L 15
D 15
L 15
R 16
L 7
R 14
D 5
L 16
U 6
D 3
L 13
D 8
L 11
U 13
L 9
U 6
L 4
U 11
R 1
L 13
R 11
L 13
R 13
L 9
D 15
R 1
L 15
R 14
L 14
U 7
L 1
R 6
D 16
L 2
R 12
L 4
D 12
R 8
U 9
D 10
R 1
L 2
D 5
L 3
R 15
L 8
D 1
L 1
D 8
U 13
R 1
L 2
D 1
R 3
L 6
U 12
L 4
D 13
U 2
L 4
D 10
R 16
D 1
U 1
L 11
D 8
L 12
R 8
L 5
R 1
D 12
R 2
D 7
U 16
D 11
L 15
R 4
U 4
D 4
U 4
L 17
U 3
D 8
U 1
L 1
U 4
L 7
U 9
L 13
D 10
L 2
U 7
L 13
D 16
U 6
L 10
D 16
L 8
U 10
L 6
U 16
L 5
U 4
R 9
D 12
R 1
U 14
L 14
R 16
D 5
L 16
R 14
U 10
R 4
U 9
L 15
D 4
U 15
L 11
R 14
L 10
D 14
L 10
D 12
R 2
D 3
R 1
U 1
L 17
U 9
D 13
R 7
D 7
U 13
D 1
R 14
U 10
R 16
L 17
R 7
D 17
U 11
L 2
U 16
L 8
U 13
R 17
U 5
L 7
R 3
D 17
L 10
U 9
D 16
R 3
U 5
L 15
R 16
D 11
U 9
L 3
R 14
D 4
L 4
U 12
D 9
U 10
D 15
L 12
R 6
D 4
L 14
D 5
L 4
U 7
R 15
D 6
L 15
U 14
D 10
L 3
D 9
L 15
R 9
U 1
L 4
D 15
U 12
D 9
R 8
D 14
R 15
D 7
U 18
L 5
U 6
L 6
D 10
L 18
R 3
L 11
D 10
L 13
U 13
L 13
R 3
L 1
U 3
D 7
L 9
R 6
U 18
R 18
U 15
R 9
U 4
R 12
L 12
D 6
U 10
D 13
L 6
R 13
L 13
D 12
U 4
D 15
L 12
D 10
U 12
R 8
L 13
D 11
L 13
U 12
D 5
U 12
R 10
L 9
U 13
R 7
D 2
L 6
U 13
D 15
R 3
U 4
D 5
L 2
D 10
U 7
L 2
D 5
L 5
D 11
R 5
U 18
L 9
D 8
U 12
R 3
U 8
R 14
D 1
R 4
L 5
D 10
R 18
D 2
R 9
L 14
U 4
R 15
D 4
R 2
L 4
U 13
R 6
U 18
D 4
U 7
L 15
D 1
L 6
D 3
U 15
L 17
U 15
R 14
L 9
U 5
L 4
U 13
R 5
D 17
U 17
L 15
U 14
R 5
L 1
R 9
U 8
R 15
U 18
L 12
R 13
D 15
R 5
L 11
R 5
U 12
R 8
L 6
R 1
L 10
U 17
L 16
U 12
L 14
D 16
U 13
D 18
L 5
U 16
L 11
D 15
U 2
L 9
D 5
L 17
D 17
L 4
D 4
L 19
R 6
D 6
U 18
R 16
U 12
D 2
L 4
U 19
R 6
U 1
D 15
R 13
U 18
D 12
L 9
U 1
R 13
D 18
L 4
D 17
L 9
D 8
U 3
D 5
R 7
L 16
U 3
L 1
D 13
R 17
D 8
R 9
U 17
L 2
U 17
D 16
L 8
R 9
D 7
L 16
R 10
L 16
D 10
L 15
U 17
L 2
U 10
D 16
R 1
L 2
D 4
R 13
L 12
D 8
U 10
L 6
D 14
L 6
D 11
R 1
D 10
L 18
D 12
R 14
L 3
D 7
L 12
R 19
U 5
R 19
D 3
L 15
U 13
"""

class Direction(IntEnum):
    UP = 1
    DOWN = 2
    LEFT = 4
    RIGHT = 8


def print_grid(col, lines, s, nodes):
    for y in range(lines):
        l = "." * col
        if s[1] == y:
            l = l[:s[0]] + 's' + l[s[0] + 1:]
        for n in range(len(nodes)-1, -1, -1):
            if nodes[n][1] == y:
                x = nodes[n][0]
                l = l[:x] + str(n) + l[x+1:]
        print(l)

    print()

def vector_dist(h, t):
    x = abs(h[0] - t[0])
    y = abs(h[1] - t[1])
    return x*x+y*y

def walk(moves, nodecount):
    s = [11, 15]
    nodes = []
    for n in range(nodecount):
        nodes.append([11, 15])

    covered = {'11_15': True}

    move_count = 0

    for move in moves:
        vector = [0, 0]
        match move[0]:
            case Direction.UP:
                vector = [0, -1]
            case Direction.DOWN:
                vector = [0, 1]
            case Direction.LEFT:
                vector = [-1, 0]
            case Direction.RIGHT:
                vector = [1, 0]

        for i in range(move[1]):
            # update head node position
            nodes[0][0] += vector[0]
            nodes[0][1] += vector[1]

            correction_vector = None
            fix_nexts = False
            v = [vector[0], vector[1]]

            # update following nodes
            for n in range(1, nodecount):
                dist = vector_dist(nodes[n - 1], nodes[n])
                if (dist > 2):
                    oldx = nodes[n][0]
                    oldy = nodes[n][1]
                    if dist > 4 and correction_vector is not None:
                        nodes[n][0] = nodes[n][0] + correction_vector[0]
                        nodes[n][1] = nodes[n][1] + correction_vector[1]
                    else:
                        if dist == 4:
                            # straight line, coords = average between current and parent
                            nodes[n][0] = (nodes[n][0] + nodes[n - 1][0]) // 2
                            nodes[n][1] = (nodes[n][1] + nodes[n - 1][1]) // 2
                        else:
                            nodes[n][0] = nodes[n - 1][0] - v[0]
                            nodes[n][1] = nodes[n - 1][1] - v[1]
                        v[0] = nodes[n][0] - oldx
                        v[1] = nodes[n][1] - oldy
                        if (dist > 4):
                            correction_vector=[v[0], v[1]]
                        else:
                            correction_vector = None
#                print(move_count, " ", i, " ", n)
#                print_grid(26, 21, s, nodes)

            key = str(nodes[nodecount-1][0]) + "_" + str(nodes[nodecount-1][1])
            covered[key] = 1

#        print_grid(26, 21, s, nodes)

        move_count += 1

    return covered




moves = []
data = data.splitlines()
for datum in data:
    direction = datum[0]
    count = int(datum[2:])
    match direction:
        case 'U':
            move = [Direction.UP, count]
        case 'D':
            move = [Direction.DOWN, count]
        case 'L':
            move = [Direction.LEFT, count]
        case _:
            move = [Direction.RIGHT, count]

    moves.append(move)

covered = walk(moves, 10)

print(len(covered))
