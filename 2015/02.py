import math

dimensions = []


def parse_input():
    with open('input', 'r') as f:
        for d in f.readlines():
            dimensions.append(d.strip().split('x'))


def get_data(box_dimensions):
    l = int(box_dimensions[0])
    w = int(box_dimensions[1])
    h = int(box_dimensions[2])
    volume = l * w * h
    around = sum(sorted([l, w, h])[:2]) * 2
    ribbon_area = volume + around

    area1 = l * w
    area2 = w * h
    area3 = h * l
    margin = min(area1, area2, area3)
    area = 2 * area1 + 2 * area2 + 2 * area3 + margin
    return area, ribbon_area


def part_1_and_2():
    area_total = 0
    ribbon_total = 0
    for d in dimensions:
        area, ribbon_area = get_data(d)
        area_total += area
        ribbon_total += ribbon_area

    print(f"total square feet of wrapping paper: {area_total}")
    print(f"total square feet of ribbon: {ribbon_total}")


parse_input()
part_1_and_2()
