# Of course there is a dark magic bit manipulation
# solution in `better`.

BASE_CASES = [["0", "1"], ["00", "01", "11", "10"]]

n = int(input())

def generate_gray_code(length):
    if length < 3:
        yield from BASE_CASES[length - 1]
        return

    for i in range(1, length):
        prefix = "0" if i == 1 else "1" + "0" * (i - 2) + "1"

        yield from (
            prefix + entry
            for entry in generate_gray_code(length - i)
        )

    yield "1" + "0" * (length - 2) + "1"
    yield "1" + "0" * (length - 1)

for entry in generate_gray_code(n):
    print(entry)
