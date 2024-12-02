def parse_input():
    with open('input', 'r') as f:
        return f.readlines()


def is_report_safe(report, skipped_index=-1):
    levels = [int(x) for x in report.strip().split(' ')]
    if skipped_index != -1:
        if skipped_index >= len(levels):
            return False
        levels.pop(skipped_index)
    adjacent = 0
    consecutive = 0
    for i in range(1, len(levels)):
        if levels[i - 1] < levels[i]:
            consecutive += 1
        else:
            consecutive -= 1

        difference = abs(levels[i - 1] - levels[i])
        if 1 <= difference <= 3:
            adjacent += 1

    is_safe = len(levels) - 1 == adjacent == abs(consecutive)

    if not is_safe and skipped_index != -1:
        return is_report_safe(report, skipped_index + 1)

    return is_safe


def part_1():
    total = 0
    for report in parse_input():
        if is_report_safe(report):
            total += 1

    print(f"total safe reports: {total}")


def part_2():
    total = 0
    for report in parse_input():
        if is_report_safe(report, 0):
            total += 1

    print(f"total damped safe reports: {total}")


part_1()
part_2()
