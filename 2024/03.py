import re


def get_input():
    f = open('input', 'r')
    return f.read()


def mul(a, b):
    return int(a) * int(b)


def get_mul_calls(_input):
    return re.findall("mul\\([0-9]+,[0-9]+\\)", _input)


def get_mul_call_with_does(_input):
    return re.findall("mul\\([0-9]+,[0-9]+\\)|don't\\(\\)|do\\(\\)", _input)


def part_1():
    total = 0
    mul_calls = get_mul_calls(get_input())
    for call in mul_calls:
        total += eval(call)

    print(f"total mul sum: {total}")


def part_2():
    total = 0
    skip = False
    mul_calls = get_mul_call_with_does(get_input())
    for call in mul_calls:
        if call == "do()":
            skip = False
        elif call == "don't()":
            skip = True
        elif not skip:
            total += eval(call)

    print(f"total mul sum with skips: {total}")


part_1()
part_2()
