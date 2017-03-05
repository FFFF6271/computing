from math import sin, pi, fabs, floor, ceil, e

def func(x):
    return e**x # sin((pi / 6) * x)

def generate_table(x):
    counter = 0

    left, right, step = -10, 10, 1
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

def select_values(table, n, max_index):
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

### Compute value 1 ###

def y(position, values):
    length = len(position)

    xn, x0 = position[length - 1], position[0]
    if(len(position) == 2):
        return (values[0] - values[1]) / (x0 - xn)

    return (y(position[0:length - 1], values[0:length - 1]) - y(position[1:length], values[1:length])) / (x0 - xn)

def newton_recursive(x, need_array):
    sum = need_array[0][1]
    multi = 1

    x_values = [need_array[0][0]]
    y_values = [need_array[0][1]]

    for i in range(1, len(need_array)):
        multi *= (x - need_array[i - 1][0])

        x_values.append(need_array[i][0])
        y_values.append(need_array[i][1])

        sum += multi * y(x_values, y_values)

    return sum

######

### Compute value 2 ###

def newton(t, need_array):
    n = len(need_array)

    res = need_array[0][1]

    for i in range(1, n):
        F = 0
        for j in range(0, i + 1):
            den = 1
            for k in range(0, i + 1):
                if k != j:
                    den *= (need_array[j][0] - need_array[k][0])
            F += need_array[j][1] / den
        for k in range(0, i):
            F *= (t - need_array[k][0])
        res += F
    return res

######

if __name__ == "__main__":
    x = float(input())
    n = int(input())

    count_points = n + 1

    if n <= 0:
        print("[Error] n < 0")
        exit()

    table, max_index = generate_table(x)

    if (len(table) < count_points):
        print("[Error] Нет достаточно точек")
        exit()

    need_array = select_values(table, max_index, count_points)

    print("После построения полинома (рекурсивно)", newton_recursive(x, need_array))
    print("После построения полинома", newton(x, need_array))

    print("Точное значение функции", func(x))