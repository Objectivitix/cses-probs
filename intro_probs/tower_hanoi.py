RODS = {1, 2, 3}

n = int(input())

def generate_moves(t, source, dest):
    if t == 1:
        yield (source, dest)
        return

    intermediate_dest, = RODS - {source, dest}

    yield from generate_moves(t - 1, source, intermediate_dest)
    yield from generate_moves(1, source, dest)
    yield from generate_moves(t - 1, intermediate_dest, dest)

print(2 ** n - 1)

for move in generate_moves(n, 1, 3):
    print(*move)
