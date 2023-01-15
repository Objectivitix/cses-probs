# BRUH MOMENT: Overcomplicated solution. Calculates
# second knight positions from every possible first knight
# position with convoluted logic. Everything is condensed
# into one bloated formula. An improved solution can be
# found in the `better` directory.

from math import comb

SPECIAL_CASES = [0, 6, 28, 96]

n = int(input())

for k in range(1, n + 1):
    if k < 5:
        print(SPECIAL_CASES[k - 1])
        continue

    print(
        (k ** 4 - k ** 3 - 10 * k ** 2 + 28 * k - 24) // 2  # pairs of rows (y < k-1)
        + k ** 2 - 2 * k + 4  # y1 = k-1, y2 = k
        + comb(k, 2) * k  # same rows
    )
