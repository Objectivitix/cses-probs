seq = iter(input())

prev = None
curr = next(seq)

longest = 1
new = 1

for char in seq:
    prev, curr = curr, char

    if prev == curr:
        new += 1
        longest = max(longest, new)
    else:
        new = 1

print(longest)
