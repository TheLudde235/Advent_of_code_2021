inp = open('day01/input.txt').read()

inp_arr = inp.split('\n')

prev_line = int(inp_arr[0])
total = 0


for line in inp_arr:
    if int(line) > int(prev_line):
        total += 1
    prev_line = line

print(total)
