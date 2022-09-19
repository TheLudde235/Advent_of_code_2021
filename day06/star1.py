lanternfish_timer = open('day06/input.txt').read().split(',')

research_days: int = 80

for i in range(research_days):
    new_fishes: list = list()
    for j in range(len(lanternfish_timer)):
        item = int(lanternfish_timer[j])
        if item == 0:
            new_fishes.append(8)
            lanternfish_timer[j] = 6
        else:
            lanternfish_timer[j] = item-1

    for new_fish in new_fishes:
        lanternfish_timer.append(new_fish)

    if i >= research_days-1:
        print(len(lanternfish_timer))
