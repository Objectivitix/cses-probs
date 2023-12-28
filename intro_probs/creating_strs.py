# We do not use collections.Counter due to ordering requirements.
# Alternatively, use set, sorted, and itertools.permutations.

def get_counter(iterable):
    counter = {}

    for item in iterable:
        if item not in counter:
            counter[item] = 1
        else:
            counter[item] += 1

    return counter

def generate_strings(letters):
    if len(letters) == 1:
        letter, = letters
        count = letters[letter]

        yield letter * count
        return

    for letter in letters:
        new_letters = letters.copy()

        new_letters[letter] -= 1
        if new_letters[letter] == 0:
            del new_letters[letter]

        yield from (
            letter + substring
            for substring in generate_strings(new_letters)
        )

inp = sorted(input())
result = list(generate_strings(get_counter(inp)))

print(len(result))
print("\n".join(result))
