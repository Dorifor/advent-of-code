def get_letters_grid():
    f = open('input', 'r')
    return [list(line.strip()) for line in f.readlines()]


def is_horizontal_match(_grid, i, j, factor=1):
    if factor == 1 and i >= len(_grid[j]) - 3 or factor == -1 and i < 3:
        return False
    return _grid[j][i + 1 * factor] == 'M' and _grid[j][i + 2 * factor] == 'A' and _grid[j][i + 3 * factor] == 'S'


def is_vertical_match(_grid, i, j, factor=1):
    if factor == 1 and j >= len(_grid) - 3 or factor == -1 and j < 3:
        return False
    return _grid[j + 1 * factor][i] == 'M' and _grid[j + 2 * factor][i] == 'A' and _grid[j + 3 * factor][i] == 'S'


def is_diagonal_match(_grid, i, j, factor=1):
    if factor == 1 and (j >= len(_grid) - 3 or i >= len(_grid[j]) - 3) or factor == -1 and (j < 3 or i < 3):
        return False
    return _grid[j + 1 * factor][i + 1 * factor] == 'M' and _grid[j + 2 * factor][i + 2 * factor] == 'A' and _grid[j + 3 * factor][
        i + 3 * factor] == 'S'


def is_reverse_diagonal_match(_grid, i, j, factor=1):
    if factor == 1 and (j < 3 or i >= len(_grid[j]) - 3) or factor == -1 and (j >= len(_grid) - 3 or i < 3):
        return False
    return _grid[j - 1 * factor][i + 1 * factor] == 'M' and _grid[j - 2 * factor][i + 2 * factor] == 'A' and _grid[j - 3 * factor][
        i + 3 * factor] == 'S'


def get_match_count(_grid, i, j):
    count = 0
    if is_horizontal_match(_grid, i, j):
        count += 1
    if is_vertical_match(_grid, i, j):
        count += 1
    if is_diagonal_match(_grid, i, j):
        count += 1
    if is_reverse_diagonal_match(_grid, i, j):
        count += 1
    if is_horizontal_match(_grid, i, j, -1):
        count += 1
    if is_vertical_match(_grid, i, j, -1):
        count += 1
    if is_diagonal_match(_grid, i, j, -1):
        count += 1
    if is_reverse_diagonal_match(_grid, i, j, -1):
        count += 1
    return count


def check_diag(_grid, i, j, factor):
    return _grid[j - 1 * factor][i - 1 * factor] == 'M' and _grid[j + 1 * factor][i + 1 * factor] == 'S'


def check_inverse_diag(_grid, i, j, factor):
    return _grid[j + 1 * factor][i - 1 * factor] == 'M' and _grid[j - 1 * factor][i + 1 * factor] == 'S'


def is_x_mas(_grid, i, j):
    if i < 1 or i > len(_grid[j]) - 2 or j < 1 or j > len(_grid) - 2:
        return False

    return (check_diag(_grid, i, j, 1) or check_diag(_grid, i, j, -1)) and (check_inverse_diag(_grid, i, j, 1) or check_inverse_diag(_grid, i, j, -1))


def part_1():
    total = 0
    grid = get_letters_grid()
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            if grid[j][i] == 'X':
                total += get_match_count(grid, i, j)

    print(f"total 'XMAS' matches: {total}")


def part_2():
    total = 0
    grid = get_letters_grid()
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            if grid[j][i] == 'A' and is_x_mas(grid, i, j):
                total += 1

    print(f"total 'X-MAS' matches: {total}")


part_1()
part_2()
