inp_list = open('day08/input.txt').read().split('\n')

counter: int = 0
value_set: set = {2, 3, 4, 7}

for inp in inp_list:
    values = inp.split('|')[1].split()
    for value in values:
        if len(value) in value_set:
            counter += 1

print(counter)
