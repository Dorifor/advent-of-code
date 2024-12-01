# It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
# It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
# It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

def is_nice(line: str) -> bool:
    line = line.strip()
    if line.__contains__('ab') or line.__contains__('cd') or line.__contains__('pq') or line.__contains__('xy'):
        return False

    vowel_count = 0
    for v in 'aeiou':
        vowel_count += line.count(v)

    twice = False
    for i in range(1, len(line)):
        if line[i] == line[i - 1]:
            twice = True
            break

    return vowel_count >= 3 and twice


def parse_input():
    with open('input', 'r') as f:
        return f.readlines()


def part_1():
    words = parse_input()
    nice_lines = [w for w in words if is_nice(w)]
    print(f"nice words with algo 1: {len(nice_lines)}")


def is_nice_2(line: str) -> bool:
    repeat_with_letter_between = False
    for i in range(2, len(line)):
        if line[i] == line[i - 2]:
            repeat_with_letter_between = True
            break

    repeated_pair = False
    for i in range(1, len(line)):
        if line.count(line[i - 1] + line[i]) > 1:
            repeated_pair = True
            break

    return repeated_pair and repeat_with_letter_between


def part_2():
    words = parse_input()
    nice_lines = [w for w in words if is_nice_2(w)]
    print(f"nice words with algo 2: {len(nice_lines)}")


part_1()
part_2()
