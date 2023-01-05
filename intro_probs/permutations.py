n = int(input())

match n:
    case 1:
        print("1")
    case 2 | 3:
        print("NO SOLUTION")
    case _:
        odds = (str(num) for num in range(1, n + 1) if num & 1)
        evens = (str(num) for num in range(2, n + 1) if not num & 1)

        print(f"{' '.join(evens)} {' '.join(odds)}".strip())
