import time

<<<<<<< HEAD
directory = 'day09'
=======
directory = 'day11'
>>>>>>> ff46610af10891e01bd312e6626b7f1a3e90ba8e
fileName = 'star2'
timer = True

if timer:
    start = time.time()

exec(open(f'{directory}/{fileName}.py').read())

if timer:
    end = time.time()
    print(f'{round((end - start)*1000, 3)}ms')