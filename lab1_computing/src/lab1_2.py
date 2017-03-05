from math import *
from lab1 import newton

def generate_table(left, right, step, func, x = 0):
    counter = 0
    table = []

    max_len = fabs(left - x)
    max_index = -1

    while left < (right + step / 2):
        tmp = fabs(left - x)
        if(tmp < max_len):
            max_index = counter
            max_len = tmp

        table.append([left, func(left)])
        left += step
        counter += 1

    return table, max_index

def find_max_index(table, x):
    max_index = -1

    counter = 0
    max_len = fabs(table[0][0] - x)

    for point in table:
        tmp = fabs(point[0] - x)
        if(tmp < max_len):
            max_index = counter
            max_len = tmp
        counter += 1

    return max_index

def select_values(table, max_index, n):
    delta = (n - 1) / 2
    l, r = max_index - floor(delta), max_index + ceil(delta)

    if(l < 0):
        r += abs(l)
        l = 0

    if(r + 1 > len(table)):
        l -= r + 1 - len(table)
        r = len(table) - 1

    need_array = []
    for i in range(l, r + 1):
        need_array.append(table[i])

    return need_array


eps_const = 1e-5
eps_otn = 1e-4

def half_div_method(a, b, eps, x, f):
    x1 = a
    x2 = b
    eps = (b - a) * eps
    while True:
        mid = (x1 + x2) / 2
        if abs(x2 - x1) < eps * abs(mid) + eps_const:
            break
        fm = f(x, mid)
        if(fm == 0):
            return mid
        if(fm * f(x, x1) < 0):
            x2 = mid
        else:
            x1 = mid
    if abs(f(x, x1)) > abs(f(x, x2)):
        return x2
    return x1

def f1y(x, y):
    x3 = x ** 3
    return exp(x3 - y) - x3 * (x3 - 2 * y - 2) - y * y - 2 * y - 2

def f2y(x, y):
    return x * x * exp(-y) + y * exp(-y) - exp(x * x) * log(x * x + y)

def f1(x):
   return half_div_method(-1, 2, eps_otn, x, f1y)

def f2(x):
    return half_div_method(0.1, 2, eps_otn, x, f2y)

def generate_need_array(tab_x, tab_y):
    need_array = []
    for i in range(len(tab_x)):
        need_array.append([tab_x[i], tab_y[i]])

    return need_array


def easy_sort(table):
    for i in range(0, len(table)):
        for j in range(1, len(table)):
            if table[j][0] < table[j - 1][0]:
                table[j], table[j - 1] = table[j - 1], table[j]

    return table

if __name__ == "__main__":
    table1, j = generate_table(0, 1, 0.1, f1)
    table2, j = generate_table(0, 1, 0.1, f2)

    table3 = []

    for i in range(0, len(table1)):
        # reverse
        table3.append([table2[i][1] - table1[i][1], table1[i][0]])

    table3 = easy_sort(table3)

    x = 0
    n = 4
    count_points = n + 1

    need_array = select_values(table3, find_max_index(table3, x), count_points)

    new_x = newton(x, need_array)

    print("Результат x = ", new_x)
    y1 = f1(new_x)
    y2 = f2(new_x)
    print("y = ", y1 + (y2 - y1) / 2)