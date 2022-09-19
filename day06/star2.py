lanternfish_timer = open('day06/input.txt').read().split(',')

research_days: int = 256

days = [0, 0, 0, 0, 0, 0, 0, 0, 0]

# populate the day list
for fish in lanternfish_timer:
    if fish == '0':
        days[0] += 1
    if fish == '1':
        days[1] += 1
    if fish == '2':
        days[2] += 1
    if fish == '3':
        days[3] += 1
    if fish == '4':
        days[4] += 1
    if fish == '5':
        days[5] += 1
    if fish == '6':
        days[6] += 1
    if fish == '7':
        days[7] += 1
    if fish == '8':
        days[8] += 1


for i in range(research_days):
    tmp_day0 = days[0]

    days[0] = days[1]
    days[1] = days[2]
    days[2] = days[3]
    days[3] = days[4]
    days[4] = days[5]
    days[5] = days[6]

    days[6] = tmp_day0 + days[7]
    days[7] = days[8]
    days[8] = tmp_day0

    if i >= research_days-1:
        total = 0

        for day in days:
            total += day
        print(total)
