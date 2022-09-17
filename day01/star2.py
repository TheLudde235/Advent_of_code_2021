inp = open('day01/input.txt').read()

inp_arr = inp.split('\n')

sliding_window = 0
prev_sliding_window = int(inp_arr[0]) + int(inp_arr[1]) + int(inp_arr[2])
total = 0

for i in range(len(inp_arr)):
    if i == 0 or i == len(inp_arr) - 1:
        continue
    sliding_window = int(inp_arr[i-1]) + int(inp_arr[i]) + int(inp_arr[i+1])

    if sliding_window > prev_sliding_window:
        total += 1

    prev_sliding_window = sliding_window

print(total)
