inp_list: list[str] = open('day09/input.txt').read().split('\n')

count: int = 0

for y in range(len(inp_list)):
    row: str = inp_list[y]

    for x in range(len(row)):
        ch: str = row[x]
        # top
        if y == 0:
            # left
            if x == 0:
                if ch < row[x + 1] and ch < inp_list[y + 1][x]:
                    count += int(ch) + 1
                continue

            # right
            if x >= len(row) - 1:
                if ch < row[x - 1] and ch < inp_list[y + 1][x]:
                    count += int(ch) + 1
                continue

            if ch < row[x + 1] and ch < row[x - 1] and ch < inp_list[y + 1][x]:
                count += int(ch) + 1
            continue

        # bottom
        if y >= len(inp_list) - 1:
            # left
            if x == 0:
                if ch < row[x + 1] and ch < inp_list[y - 1][x]:
                    count += int(ch) + 1
                continue
            # right
            if y >= len(inp_list) - 1 and x >= len(row) - 1:
                if ch < row[x - 1] and ch < inp_list[y - 1][x]:
                    count += int(ch) + 1
                continue

            if ch < row[x + 1] and ch < row[x - 1] and ch < inp_list[y - 1][x]:
                count += int(ch) + 1
            continue

        # left
        if x == 0:
            if ch < row[x + 1] and ch < inp_list[y + 1][x] and ch < inp_list[y - 1][x]:
                count += int(ch) + 1
            continue
        # right
        if x >= len(row) - 1:
            if ch < row[x - 1] and ch < inp_list[y + 1][x] and ch < inp_list[y - 1][x]:
                count += int(ch) + 1
            continue
        print(f'x: {x}, y: {y}')
        if ch < row[x + 1] and ch < row[x - 1] and ch < inp_list[y + 1][x] and ch < inp_list[y - 1][x]:
            count += int(ch) + 1

print(count)
