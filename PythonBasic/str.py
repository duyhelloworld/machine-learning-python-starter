# print("num" in "Helloworld, Im num")

# Slicing
a = "abcdefghijklmno"
# print(a[2:5])
# print(a[2:], a[0:1], sep="___")

import time

def count_items(items):
    print('Counting ', end='', flush=True)
    num = 0
    for item in items:
        num += 1
        time.sleep(1)
        print('.', end='', flush=True)

    print(f'\nThere were {num} items')

# count_items(a)
# print("     Hello    _".strip("_"))
