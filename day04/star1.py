inp = '''7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7'''

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

prev_numbers: set = set({})
last_number = {}
bingo = False

board = None

for number in order:
    prev_numbers.add(number)
    last_number = number

    for board in boards:
        c: int
        r: int
        for row in board:
            for item in row:
                if item == number:
                    c = row.index(item)
                    r = row.index(item)
                    b: bool = True
                    for tmpRow in board:
                        if tmpRow[c] not in prev_numbers:
                            b = False
                            break
                        else:
                            b = True

                    if b:
                        bingo = True
                        board = boards.index(board)
                        break

                    for tmpCol in row:
                        if tmpCol not in prev_numbers:
                            b = False
                            break
                        else:
                            b = True

                    if b:
                        bingo = True
                        board = boards.index(board)
                        break
            if bingo:
                break
        if bingo:
            break
    if bingo:
        break

unmarked_sum = 0

for row in boards[board]:
    for item in row:
        if item not in prev_numbers:
            unmarked_sum += int(item)


print(unmarked_sum * int(last_number))
