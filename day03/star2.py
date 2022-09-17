import copy

inp = open('day03/input.txt').read()

inp_list = inp.split('\n')


def binary_to_decimal(binary_num):
    reversed_binary_num = binary_num[::-1]
    result = 0
    current_value = 1

    for ch in reversed_binary_num:
        if ch == '1':
            result += current_value
        current_value *= 2

    return result


def oxygen_rating(value_list):
    for i in range(len(value_list[0])):

        amount_of_zeros = 0
        amount_of_ones = 0

        temp_arr = copy.deepcopy(value_list)

        for line in value_list:
            if line[i] == '0':
                amount_of_zeros += 1
            else:
                amount_of_ones += 1

        if amount_of_zeros > amount_of_ones:
            prev_most_common = '0'
        else:
            prev_most_common = '1'

        for line in value_list:
            if line[i] != prev_most_common:
                temp_arr.remove(line)

        value_list = temp_arr

        if len(value_list) == 1:
            return binary_to_decimal(value_list[0])

    print('Error when returning oxygen rating')
    return value_list


def co2_rating(value_list):
    prev_least_common = ''

    for i in range(len(value_list[0])):

        amount_of_zeros = 0
        amount_of_ones = 0

        temp_arr = copy.deepcopy(value_list)

        if i != 0:
            for line in value_list:
                if line[i-1] != prev_least_common:
                    temp_arr.remove(line)

        value_list = temp_arr

        for line in value_list:
            if line[i] == '0':
                amount_of_zeros += 1
            else:
                amount_of_ones += 1

        if 0 < amount_of_ones < amount_of_zeros:
            prev_least_common = '1'
        if 0 < amount_of_zeros <= amount_of_ones:
            prev_least_common = '0'

        if len(value_list) == 1:
            return binary_to_decimal(value_list[0])

    print('Error when returning co2 rating')
    return value_list


total = int(oxygen_rating(inp_list)) * int(co2_rating(inp_list))

print(total)
