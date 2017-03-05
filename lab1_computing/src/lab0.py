from math import *

def f(x, y):
    return e**(x**3) - e**y * (x**6 - 2 * x**3 * y - 2 * x**3 + y**2 + 2 * y + 2)

def getByMethodHalfDivision(x, func):
    eps = 1e-4
    a = -1
    b = 1

    while func(x, a) * func(x, b) >= 0:
        a *= 2
        b *= 2

    while True:
        mid = (a + b) / 2
        if fabs(b - a) < eps * (fabs(mid) + 1):
            break

        if func(x, a) * func(x, mid) < 0:
            b = mid
        else:
            a = mid

    return mid

def getByX(x):
    return getByMethodHalfDivision(x, f)

def methodTrapeze(a, b, n, func):
    h = (b - a) / n
    left = a

    sum = 0
    for i in range(n - 1):
        left += h
        sum += func(left)

    return h * ((func(a) + func(b)) / 2 + sum)

a = 0
b = 2

result = methodTrapeze(a, b, 1000, getByX)
print("Результат", result)