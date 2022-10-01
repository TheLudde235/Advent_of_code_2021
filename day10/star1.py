inp_list: list[str] = open('day10/input.txt').read().split('\n')

brackets_stack: list[str] = list()

brackets_dict: dict = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

points_dict: dict = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}


def validate_line(line):
    for ch in line:
        if ch in brackets_dict:
            brackets_stack.append(ch)
        else:
            if ch == brackets_dict[brackets_stack[-1]]:
                brackets_stack.pop()
            else:
                return ch
    return ''


count: int = 0

for inp in inp_list:
    faulty_char = validate_line(inp)
    if faulty_char:
        count += points_dict[faulty_char]

print(count)
