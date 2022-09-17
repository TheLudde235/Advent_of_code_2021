inp = open('day03/input.txt').read()

inp_arr = inp.split('\n')

def binary_to_decimal(binary_num):
    reversed_binary_num = binary_num[::-1]
    total = 0
    current_value = 1

    for ch in reversed_binary_num:
        if ch == '1':
            total += current_value
        current_value *= 2

    return total


gamma_rate = ''
epsilon_rate = ''

for i in range(len(inp_arr[0])):
    amount_of_zeros = 0
    amount_of_ones = 0

    for line in inp_arr:
        if line[i] == '0':
            amount_of_zeros += 1
        else:
            amount_of_ones += 1

    if amount_of_zeros > amount_of_ones:
        gamma_rate += '0'
        epsilon_rate += '1'
    else:
        gamma_rate += '1'
        epsilon_rate += '0'


result = int(binary_to_decimal(gamma_rate)) * int(binary_to_decimal(epsilon_rate))

print(result)
