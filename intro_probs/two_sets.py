# Why recurse when you can iterate? See a `better` solution.

import sys

MAX = 1_000_000

n = int(input())
s = n * (n + 1) // 2

if s & 1:
    print("NO")
    raise SystemExit

sys.setrecursionlimit(MAX)

partition_a = []
partition_b = []

def choose_next_num(largest, remaining):
    if remaining <= largest:
        partition_a.append(remaining)

        partition_b.extend(range(1, remaining))
        partition_b.extend(range(remaining + 1, largest + 1))
        return

    partition_a.append(largest)
    choose_next_num(largest - 1, remaining - largest)

choose_next_num(n, s // 2)

print("YES")
print(len(partition_a))
print(" ".join(map(str, partition_a)))
print(len(partition_b))
print(" ".join(map(str, partition_b)))
