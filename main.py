import time

directory = 'day08'
fileName = 'star2'
timer = True

if timer:
    start = time.time()

exec(open(f'{directory}/{fileName}.py').read())

if timer:
    end = time.time()
    print(f'{(end - start)*1000}ms')