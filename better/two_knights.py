# BETTER: Much more readable and understandable formula
# subtracts invalid positions from the number of total
# possible positions. Duplicates are accounted for with
# a division by 2.

n = int(input())

for k in range(1, n + 1):
    print(
        k ** 2 * (k ** 2 - 1) // 2
        - 4 * (k - 1) * (k - 2)  # coefficient = 8 / 2
    )
