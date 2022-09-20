import math

inp_list = '16,1,2,0,4,2,7,1,2,14'.split(',')

inp_list = open('day07/input.txt').read().split(',')

int_list: list = list()

for inp in inp_list:
    int_list.append(int(inp))


def average(ls):
    total = 0
    for item in ls:
        total += item
    return total/len(ls)


def calculate_cost(fr, to):
    distance = abs(fr - to)
    return (distance * (distance - 1))/2 + distance


def calculate_total_cost(avg):
    total = 0
    for pos in int_list:
        total += calculate_cost(pos, avg)
    return total


# Slow af
def get_lowest(ls):
    lowest = math.inf

    for i in range(max(int_list) - min(int_list)):
        total = 0
        for item in ls:
            total += calculate_cost(item, min(int_list)+i)
        if total < lowest:
            lowest = total
    return lowest


print(get_lowest(int_list))
