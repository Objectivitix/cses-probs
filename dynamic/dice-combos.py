MODULUS = 10 ** 9 + 7
 
n = int(input())
 
combos_n = [0] * 7
combos_n[0] = 1

for i in range(1, n + 1):
    # wrap for O(1) space
    curr = i % 7

    # clear previous stored value
    combos_n[curr] = 0

    combos_n[curr] = sum(combos_n)
 
    combos_n[curr] %= MODULUS

print(combos_n[n % 7])
