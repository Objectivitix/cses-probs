MAX = 10 ** 9

n = int(input())

s = 0
exp = 1

while (factor := 5 ** exp) <= MAX:
    s += n // factor
    exp += 1

print(s)
