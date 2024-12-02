# turn on 489,959 through 759,964
# turn off 820,516 through 871,914
# toggle 756,965 through 812,992

def parse_input():
    with open('input', 'r') as f:
        return f.readlines()


def toggle_lights(lights, _from, _to):
    _from = [int(x) for x in _from.split(',')]
    _to = [int(x) for x in _to.split(',')]
    for x in range(_from[0], _to[0] + 1):
        for y in range(_from[1], _to[1] + 1):
            lights[x][y] = 1 if lights[x][y] == 0 else 0


def set_lights(lights, _from, _to, value):
    _from = [int(x) for x in _from.split(',')]
    _to = [int(x) for x in _to.split(',')]
    for x in range(_from[0], _to[0] + 1):
        for y in range(_from[1], _to[1] + 1):
            lights[x][y] = value


def manage_lights(lights, _from, _to, factor):
    _from = [int(x) for x in _from.split(',')]
    _to = [int(x) for x in _to.split(',')]
    for x in range(_from[0], _to[0] + 1):
        for y in range(_from[1], _to[1] + 1):
            lights[x][y] += factor
            lights[x][y] = max(0, lights[x][y])


def count_lights_on(lights) -> int:
    total = 0
    for x in lights:
        for y in x:
            total += y

    return total


def part_1():
    lights = [[0 for y in range(1000)] for x in range(1000)]
    for line in parse_input():
        splitted = line.strip().split(' ')
        if splitted[0] == 'toggle':
            toggle_lights(lights, splitted[1], splitted[-1])
        if splitted[0] == 'turn':
            if splitted[1] == 'off':
                set_lights(lights, splitted[2], splitted[-1], 0)
            else:
                set_lights(lights, splitted[2], splitted[-1], 1)

    total = count_lights_on(lights)
    print(f"total lights on: {total}")


def part_2():
    lights = [[0 for y in range(1000)] for x in range(1000)]
    for line in parse_input():
        splitted = line.strip().split(' ')
        if splitted[0] == 'toggle':
            manage_lights(lights, splitted[1], splitted[-1], 2)
        if splitted[0] == 'turn':
            if splitted[1] == 'off':
                manage_lights(lights, splitted[2], splitted[-1], -1)
            else:
                manage_lights(lights, splitted[2], splitted[-1], 1)

    total = count_lights_on(lights)
    print(f"total lights on part 2: {total}")


part_1()
part_2()
