# Alternatively, solve using numpy and linear algebra.

t = int(input())
coin_pile_pairs = (
    tuple(map(int, input().split()))
    for _ in range(t)
)

for a, b in coin_pile_pairs:
    x = (2 * b - a) / 3
    y = (a - x) / 2

    valid_sols = (
        x.is_integer()
        and y.is_integer()
        and x >= 0
        and y >= 0
    )

    print("YES" if valid_sols else "NO")
