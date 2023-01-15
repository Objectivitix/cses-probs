string = input()

char_counter = {}

for char in string:
    if char in char_counter:
        char_counter[char] += 1
    else:
        char_counter[char] = 1

odds = 0
odd_char = None

for char, count in char_counter.items():
    if count & 1:
        odd_char = (char, count)
        odds += 1

    if odds > 1:
        print("NO SOLUTION")
        raise SystemExit

part_list = []

for char, count in char_counter.items():
    if count & 1:
        continue

    part_list.append(char * (count // 2))

part_string = "".join(part_list)

print(
    f"{part_string}{odd_char[0] * odd_char[1]}{part_string[::-1]}"
    if odd_char
    else f"{part_string}{part_string[::-1]}"
)
