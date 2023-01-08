# BETTER: let f(x) = x ^ (x >> 1). This function encodes
# the positions where the bits of x change. It generates
# a valid Gray code because
#
#   1. the function is injective, and
#   2. f(x) and f(x + 1) always differ by exactly one bit.

n = int(input())

for i in range(1 << n):
    print(format(i ^ (i >> 1), f"0{n}b"))
