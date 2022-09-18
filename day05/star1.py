input_list = open('day05/input.txt').read().split('\n')

tuple_pair_list: list = list()

for inp in input_list:
    i_list = inp.split(' -> ')
    xy1 = (int(i_list[0].split(',')[0]), int(i_list[0].split(',')[1]))
    xy2 = (int(i_list[1].split(',')[0]), int(i_list[1].split(',')[1]))
    tuple_pair_list.append((xy1, xy2))


def filter_diagonals(tp_list):
    output_list: list = list()
    highest_x: int = 0
    highest_y: int = 0
    for tp in tp_list:
        if tp[0][0] != tp[1][0] and tp[0][1] != tp[1][1]:
            continue
        if tp[0][0] > highest_x:
            highest_x = tp[0][0]
        if tp[1][0] > highest_x:
            highest_x = tp[1][0]
        if tp[0][1] > highest_y:
            highest_y = tp[0][1]
        if tp[1][1] > highest_y:
            highest_y = tp[1][1]
        output_list.append(tp)
    return output_list, (highest_x, highest_y)


def get_horizontal(tuple_pair):
    output: list = list()
    xy1 = tuple_pair[0]
    xy2 = tuple_pair[1]

    differance = xy2[0] - xy1[0]

    if differance >= 0:
        for i in range (differance):
            output.append((xy1[0]+i, xy1[1]))

    if differance < 0:
        for i in range(abs(differance)):
            output.append((xy1[0]-i, xy1[1]))
    output.append(xy2)
    return output


def get_vertical(tuple_pair):
    output: list = list()
    xy1 = tuple_pair[0]
    xy2 = tuple_pair[1]

    differance = xy2[1] - xy1[1]

    if differance >= 0:
        for i in range(differance):
            output.append((xy1[0], xy1[1]+i))

    if differance < 0:
        for i in range(abs(differance)):
            output.append((xy1[0], xy1[1]-i))
    output.append(xy2)
    return output


tuple_pair_list, highest_xy = filter_diagonals(tuple_pair_list)

map_2d_list: list = list()
for x in range(highest_xy[1]+1):
    map_2d_list.append(list())
    for y in range(highest_xy[0]+1):
        map_2d_list[x].append(f'.')


total: int = 0
for tuple_pair in tuple_pair_list:
    line: list = list()
    if tuple_pair[0][0] != tuple_pair[1][0]:
        line = get_horizontal(tuple_pair)
    else :
        line = get_vertical(tuple_pair)

    for pos in line:
        l = map_2d_list[pos[1]][pos[0]]
        if map_2d_list[pos[1]][pos[0]] == '1':
            total += 1

        if map_2d_list[pos[1]][pos[0]] == '.':
            map_2d_list[pos[1]][pos[0]] = '1'
        else:
            map_2d_list[pos[1]][pos[0]] = str(int(map_2d_list[pos[1]][pos[0]]) + 1)

print(total)
