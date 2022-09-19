import statistics

inp_list = '16,1,2,0,4,2,7,1,2,14'.split(',')

inp_list = open('day07/input.txt').read().split(',')

int_list: list = list()

for inp in inp_list:
    int_list.append(int(inp))


def calculate_cost(mid):
    total = 0
    for pos in int_list:
        total += abs(pos - mid)
    return total


median = statistics.median(int_list)

print(round(calculate_cost(median)))
