inp = open('day02/input.txt').read()

inp_arr = inp.split('\n')

horizontal_pos = 0
vertical_pos = 0

for action in inp_arr:
    if action[0] == 'f':
        horizontal_pos += int(action[-1])
        continue
    if action[0] == 'd':
        vertical_pos += int(action[-1])
        continue
    if action[0] == 'u':
        vertical_pos -= int(action[-1])
        continue

print(f'Horizontal: {horizontal_pos}, Vertical: {vertical_pos}, Total: {horizontal_pos * vertical_pos}')
