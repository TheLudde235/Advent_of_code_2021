inp_list: list = open('day08/test_input.txt').read().split('\n')

signal_patterns: list = list()

test_input: str = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'
easy_input: str = 'egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb'

easy_values: dict = {
    2: 1,
    3: 7,
    4: 4,
    5: {2, 3, 5},
    6: {0, 6, 9},
    7: 8
}

# def print_connections(connections: dict):


def decrypt(inp: str):
    signal_pattern: list = inp.split('|')[0].split()
    output_values: list = inp.split('|')[1].split()
    result: int = 0
    easy_output: bool = True

    unique_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

    segments: dict = {
        0: None,
        1: None,
        2: None,
        3: None,
        4: None,
        5: None,
        6: None,
        7: None,
        8: None,
        9: None
    }

    wire_map: list = list()

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
        return result

    for signal in signal_pattern:
        if type(easy_values[len(signal)]) == int:
            segments[easy_values[len(signal)]] = signal
            unique_numbers.remove(easy_values[len(signal)])
            print(f'{signal}: {easy_values[len(signal)]}')
            continue


    print(f'unique_numbers: {unique_numbers}')


print(decrypt(test_input))
