import copy

inp_list: list[str] = '''2524255331
1135625881
2838353863
1662312365
6847835825
2185684367
6874212831
5387247811
2255482875
8528557131'''.split('\n')

prev_set: set[tuple[int, int]] = set()
matrix: list[list[int]] = list()

for line in inp_list:
    tmp_line: list[int] = list()
    for ch in line:
        tmp_line.append(int(ch))
    matrix.append(tmp_line)


class Counter:
    count: int = 0


def check(rc: tuple[int, int]):
    if matrix[rc[0]][rc[1]] == 0 or rc in prev_set:
        return
    matrix[rc[0]][rc[1]] += 1
    if matrix[rc[0]][rc[1]] > 9:
        matrix[rc[0]][rc[1]] = 0
        prev_set.add((rc[0], rc[1]))
        update_surrounding(rc[0], rc[1])
        Counter.count += 1


def update_surrounding(r_index: int, c_index: int):
    possible_indexes: list[tuple[int, int]] = [
        (r_index - 1, c_index - 1),
        (r_index - 1, c_index),
        (r_index - 1, c_index + 1),
        (r_index, c_index + 1),
        (r_index, c_index - 1),
        (r_index + 1, c_index + 1),
        (r_index + 1, c_index),
        (r_index + 1, c_index - 1)
    ]

    tmp_indexes: list[tuple[int, int]] = copy.deepcopy(possible_indexes)

    # top
    if r_index <= 0:
        for index in possible_indexes:
            if index[0] == r_index - 1:
                tmp_indexes.remove(index)

    possible_indexes = tmp_indexes
    tmp_indexes: list[tuple[int, int]] = copy.deepcopy(possible_indexes)

    # left
    if c_index <= 0:
        for index in possible_indexes:
            if index[1] == c_index - 1:
                tmp_indexes.remove(index)

    possible_indexes = tmp_indexes
    tmp_indexes: list[tuple[int, int]] = copy.deepcopy(possible_indexes)

    # right
    if c_index >= len(matrix[r_index]) - 1:
        for index in possible_indexes:
            if index[1] == c_index + 1:
                tmp_indexes.remove(index)

    possible_indexes = tmp_indexes
    tmp_indexes: list[tuple[int, int]] = copy.deepcopy(possible_indexes)

    # bottom
    if r_index >= len(matrix) - 1:
        for index in possible_indexes:
            if index[0] == r_index + 1:
                tmp_indexes.remove(index)

    possible_indexes = tmp_indexes

    for index in possible_indexes:
        check(index)


def step():
    prev_set.clear()
    Counter.count = 0
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            matrix[y][x] += 1

    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x] > 9:
                matrix[y][x] = 0
                Counter.count += 1
                update_surrounding(y, x)
    if Counter.count >= 100:
        return False
    return True


count: int = 1
while step():
    count += 1
print(count)
