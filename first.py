import random
from itertools import combinations


def generate_point():
    return (random.randint(0, 100), random.randint(0, 100))


def is_line(p1, p2, p3):
    x_1 = p1[0]
    y_1 = p1[1]
    x_2 = p2[0]
    y_2 = p2[1]
    x_3 = p3[0]
    y_3 = p3[1]
    if (x_3 - x_1) / (x_2 - x_1) == (y_3 - y_1) / (y_2 - y_1):
        return True
    return False


def get_area_triangle(p1, p2, p3):
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    x3 = p3[0]
    y3 = p3[1]
    return abs((x2-x1)*(y3-y1) - (x3-x1)*(y2-y1)) / 2


N = int(input("Введите количество точек: "))
points = []
for i in range(N):
    points.append(generate_point())
print(f"all points {points}")
combination = list(combinations(points, 3))
cur = ()
min = 10000
for comb in combination:
    if not is_line(comb[0], comb[1], comb[2]):
        print(f"Triangle with coord: {comb}")
        area = get_area_triangle(comb[0], comb[1], comb[2])
        print(f"area: {area}")
        if area < min:
            cur = comb
            min = area
print(f"Triangle with min area={area}: {cur}")
