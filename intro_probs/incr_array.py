_ = input()
it = map(int, input().split())

prev = 0
curr = next(it)

moves_n = 0

for num in it:
    prev, curr = max(prev, curr), num

    if prev > curr:
        moves_n += prev - curr

print(moves_n)
