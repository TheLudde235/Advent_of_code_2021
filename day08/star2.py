inp_list: list = open('day08/input.txt').read().split('\n')

easy_values: dict = {
    2: 1,
    3: 7,
    4: 4,
    5: {2, 3, 5},
    6: {0, 6, 9},
    7: 8
}

wire_map: list = ['', '', '', '', '', '', '']

def get_key(my_dict, val):
    for key, value in my_dict.items():
        if val == value:
            return key

def decrypt(inp: str):
    signal_pattern: list = inp.split('|')[0].split()

    segments: dict = {
        0: '',
        1: '',
        2: '',
        3: '',
        4: '',
        5: '',
        6: '',
        7: '',
        8: '',
        9: ''
    }

    # get the easy signal patterns

    for signal in signal_pattern:
        if type(easy_values[len(signal)]) == int:
            segments[easy_values[len(signal)]] = sorted(signal)
            continue

    # we can figure out wire_map[0] by comparing the segments for 1 and 7; ex. 1: 'ab' 7: 'cab' differance: 'c'

    for ch in segments[7]:
        if ch not in segments[1]:
            wire_map[0] = ch

    # we can figure out wire_map[3] by checking for the common segment for 2, 3, 4 and 5
    tmp_list: list = list()
    for sp in signal_pattern:
        if len(sp) == 5:
            tmp_list.append(sp)

    for ch in segments[4]:
        check: bool = True
        for tmp in tmp_list:
            if ch not in tmp:
                check = False
                break
        if check:
            wire_map[3] = ch

    # with wire_map[3] we can use it to figure out wire_map[1] using the same strategy as we did with wire_map[0]

    for ch in segments[4]:
        if ch not in segments[1] and ch != wire_map[3]:
            wire_map[1] = ch

    # now we can figure out the segments for 5 with wire_map[1] since only the 5 has it enabled
    # and with segments[1] we can figure out the 2 and 3 since 2 doesn't use both segments in segments[1] and 3 does

    for tmp in tmp_list:
        if wire_map[1] in tmp:
            segments[5] = sorted(tmp)
            continue

        if segments[1][0] in tmp and segments[1][1] in tmp:
            segments[3] = sorted(tmp)
        else:
            segments[2] = sorted(tmp)

    # we can compare segments[5] to segments[1] to figure out wire_map[5] and wire_map[2]

    if segments[1][0] in segments[5]:
        wire_map[5] = segments[1][0]
        wire_map[2] = segments[1][1]
    else:
        wire_map[5] = segments[1][1]
        wire_map[2] = segments[1][0]

    # we can figure out segments[0] with wire_map[3] and the length

    tmp_list.clear()
    for sp in signal_pattern:
        if len(sp) == 6:
            if wire_map[3] not in sp:
                segments[0] = sorted(sp)
            else:
                tmp_list.append(sp)

    # we can figure out segments[6] and segments[9] with wire_map[2] since it's only active in segments[9]

    for tmp in tmp_list:
        if wire_map[2] in tmp:
            segments[9] = sorted(tmp)
        else:
            segments[6] = sorted(tmp)

    return segments


def decode_output(segments, outputs):
    result: int = 0
    value: int = 0

    for output in outputs:
        result *= 10
        result += get_key(segments, sorted(output))
    return result

counter: int = 0
for i in inp_list:
    output_values: list = i.split('|')[1].split()
    result: int = 0
    easy_output: bool = True
    # Check if output is "easy"
    for output in output_values:
        if type(easy_values[len(output)]) != int:
            easy_output = False
            break
    # Return output if "easy"
    if easy_output:
        for output in output_values:
            result *= 10
            result += easy_values[len(output)]
        counter += result
        continue

    counter += decode_output(decrypt(i), output_values)

print(counter)
