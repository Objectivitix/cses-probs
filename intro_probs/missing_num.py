n = int(input())
numbers = set(int(number) for number in input().split())

all_numbers = (i + 1 for i in range(n))

for number in all_numbers:
    if number not in numbers:
        print(number)
        break
