# Python's pow function makes this problem trivial.

MODULUS = 10 ** 9 + 7

n = int(input())

def powmod(base, exponent, modulus):
    if exponent == 0:
        return 1

    if exponent & 1:
        return (
            powmod(base, exponent - 1, modulus)
            * (base % modulus)
            % modulus
        )

    u = powmod(base, exponent // 2, modulus)
    return u * u % modulus

print(powmod(2, n, MODULUS))
