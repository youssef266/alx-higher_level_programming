#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    for ayz in range(x):
        try:
            print(f'{my_list[ayz]}', end='')
        except (IndexError):
            continue
        counter += 1
    print()
    return (counter)
