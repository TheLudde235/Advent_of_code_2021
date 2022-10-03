inp_list: list[str] = open('day10/input.txt').read().split('\n')

brackets_dict: dict = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

points_dict: dict = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


def get_unclosed_brackets(line):
    brackets_stack: list[str] = list()
    for ch in line:
        if ch in brackets_dict:
            brackets_stack.append(ch)
        else:
            if ch == brackets_dict[brackets_stack[-1]]:
                brackets_stack.pop()
            else:
                return False
    return brackets_stack


def get_scores(inputs):
    output: list[int] = list()
    for inp in inputs:
        count: int = 0
        bracket_stack = get_unclosed_brackets(inp)

        if bracket_stack:
            while bracket_stack:
                count *= 5
                count += points_dict[brackets_dict[bracket_stack.pop()]]
            output.append(count)
    return output


scores: list[int] = get_scores(inp_list)
scores.sort()
print(scores[int(len(scores)/2 - 0.5)])
