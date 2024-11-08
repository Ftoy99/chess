verticalPos = {
    'a': 7,
    'b': 6,
    'c': 5,
    'd': 4,
    'e': 3,
    'f': 2,
    'g': 1,
    'h': 0,
}

verticalPosReverse = {
    7: 'a',
    6: 'b',
    5: 'c',
    4: 'd',
    3: 'e',
    2: 'f',
    1: 'g',
    0: 'h',
}


def num_to_pos(i, j) -> str:
    return verticalPosReverse[i] + j


def pos_to_num(pos) -> tuple:
    return int(pos[1]) - 1, verticalPos[pos[0]]
    pass
