n = int(input())

while n != 1:
    print(n, end=" ")
    if n & 1:
        n = n * 3 + 1
    else:
        n = int(n / 2)

print(n)
