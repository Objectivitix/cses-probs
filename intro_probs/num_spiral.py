t = int(input())
posset = (
    tuple(map(int, input().split()))
    for _ in range(t)
)

for y, x in posset:
    n = max(y, x)
    n_is_odd = n & 1

    if x == n:
        j = n ** 2 if n_is_odd else (n - 1) ** 2 + 1
        print(j - y + 1 if n_is_odd else j + y - 1)
    else:
        k = (n - 1) ** 2 + 1 if n_is_odd else n ** 2
        print(k + x - 1 if n_is_odd else k - x + 1)
