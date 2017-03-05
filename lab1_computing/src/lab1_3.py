"""
многомерная интерполяции на примере нахождения значений функции 2-х переменных
"""

from math import *

eps_const = 0.00001
eps_otn = 0.0001
def f_0(x, y):
    return x * x + y * y

# Table: (x, (y, ...), (z, ...)), ...

def generate_table(f, part_x, part_y):
    startx, endx, stepx = part_x
    if(part_y == ()):
        starty = startx; endy = endx; stepy = stepx
    else:
        starty, endy, stepy = part_y

    table = []
    x = startx
    j = 0
    while(x < endx + stepx):
        y = starty
        table.append([x, [], []])
        while(y < endy + stepy):
            table[j][1].append(y)
            table[j][2].append(f(x, y))
            y += stepy
        x += stepx
        j += 1
    return table

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
# поиск конфигурации по х
def find_list_x(table, x, n):
    a = 0
    b = len(table)
    while(b - a > 1):
        m = int((a + b) / 2)
        #print(a, b, m, table[0][m])
        if table[m][0] > x:
            b = m
        elif table[m][0] == x:
            return m
        else:
            a = m
    mid = a

    res = []
    left = max(0, mid - int((n + 1)/2))
    right = min(len(table) - 1, left + n)
    left = max(0, right - n)
    for i in range(left, right + 1):
        res.append(i)
    return res

def getCoefPolynomByConfiguration(conf, n):
    newconf = []
    for i in range(0, len(conf[0]) - n):
        #print(conf[1][i+1], conf[1][i])
        tmp = (conf[1][i+1] - conf[1][i]) / (conf[0][i+n] - conf[0][i] )
        newconf.append(tmp)
    return newconf

def newton(t, need_array):
    print(need_array)
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


n = int(input("Введите степень полинома для интерполяции x: "))
x = float(input("x = "))
m = int(input("Введите степень полинома для интерполяции y: "))
y = float(input("y = "))

table = generate_table(f_0, (0, 5, 1), ())

max_index = find_max_index(table, x)
x_l = select_values(table, n, max_index)

tablex = []

def gen_normal_array(arr):
    need_array = []
    for index in range(len(arr[0])):
        need_array.append([arr[0][index], arr[1][index]])
    return need_array

for i in x_l:
    tmp = newton(y, gen_normal_array(i[1:3]))
    tablex.append([i[0], tmp])

z = newton(x, tablex)
print("Результат ", z)
print("Правильный ответ ", f_0(x, y))
