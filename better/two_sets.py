# BETTER: Iterative solution avoids manually setting
# a high recursion limit and is more efficient.

n = int(input())
s = n * (n + 1) // 2

if s & 1:
    print("NO")
    raise SystemExit

partition_a = []
partition_b = []

largest = n
remaining = s // 2

while remaining > largest:
    partition_a.append(largest)
    largest, remaining = largest - 1, remaining - largest

partition_a.append(remaining)

partition_b.extend(range(1, remaining))
partition_b.extend(range(remaining + 1, largest + 1))

print("YES")
print(len(partition_a))
print(" ".join(map(str, partition_a)))
print(len(partition_b))
print(" ".join(map(str, partition_b)))
