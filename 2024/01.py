def parse_input():
    left = []
    right = []

    with open('01/input', 'r') as f:
        lines = f.readlines()
        for line in lines:
            left.append(int(line.split('   ')[0]))
            right.append(int(line.split('   ')[1]))

    return left, right


def get_total_distance(left, right):
    total = 0

    for i in range(len(left)):
        total += abs(left[i] - right[i])

    return total


def main_part_1():
    left, right = parse_input()
    left.sort()
    right.sort()
    total = get_total_distance(left, right)
    print(f"part_1: {total}")


def main_part_2():
    total = 0
    left, right = parse_input()
    union = set(left).intersection(set(right))

    for n in union:
        total += n * left.count(n) * right.count(n)

    print(f"part_2: {total}")


if __name__ == '__main__':
    main_part_1()
    main_part_2()
