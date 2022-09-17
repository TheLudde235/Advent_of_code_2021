inp = open('day04/input.txt').read()

inp_arr = inp.split('\n\n')

order = inp_arr[0].split(',')
inp_arr.remove(inp_arr[0])

boards = []

for board in inp_arr:
    rows = board.split('\n')
    r = []
    for row in rows:
        r.append(row.split())
    boards.append(r)


def return_best_board() -> int:
    prev_numbers: set = set()
    for number in order:
        prev_numbers.add(number)
        for board in boards:
            for row in board:
                for item in row:
                    if item == number:
                        c = row.index(item)
                        b: bool = True

                        for tmpRow in board:
                            if tmpRow[c] not in prev_numbers:
                                b = False
                                break
                            else:
                                b = True

                        if b:
                            return boards.index(board)

                        for tmpCol in row:
                            if tmpCol not in prev_numbers:
                                b = False
                                break
                            else:
                                b = True

                        if b:
                            return boards.index(board)


def get_result(board) -> int:
    prev_numbers: set = set()
    last_number: int
    for number in order:
        prev_numbers.add(number)
        last_number = number
        for row in board:
            for item in row:
                if item == number:
                    c: int = row.index(item)
                    b: bool = True

                    for tmpRow in board:
                        if tmpRow[c] not in prev_numbers:
                            b = False
                            break
                        else:
                            b = True

                    if b:
                        total_sum = 0
                        for r in board:
                            for i in r:
                                if i not in prev_numbers:
                                    total_sum += int(i)

                        return total_sum * int(last_number)

                    for tmpCol in row:
                        if tmpCol not in prev_numbers:
                            b = False
                            break
                        else:
                            b = True

                    if b:
                        total_sum = 0
                        for r in board:
                            for i in r:
                                if i not in prev_numbers:
                                    total_sum += int(i)

                        return total_sum * int(last_number)


while len(boards) > 1:
    boards.remove(boards[return_best_board()])

print(get_result(boards[0]))
