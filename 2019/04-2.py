#! /usr/bin/env python3

from collections import Counter


# puzzle inputs
min_range = 284639
max_range = 748759

counter = 0

for n in range(min_range, max_range + 1):
    a = str(n)
    b = str(n)[1:]

    if any(x > y for x, y in zip(a, b)):
        continue

    if not any(x == y for x, y in zip(a, b)):
        continue

    if 2 not in Counter(a).values():
        continue

    counter += 1

print(counter)
