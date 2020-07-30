import scipy.special


def factor(number):
    k = 0
    while True:
        if number % 2 == 0:
            k += 1
            number = number // 2
        else:
            break
    return k


def g(n, m):
    return factor(scipy.special.comb(n, m, exact=True))


def f(n):
    out = 0
    for m in range(n // 2 + 1):
        temp = g(n, m)
        if temp > out:
            out = temp
    return out


def s(n):
    out = 0
    for i in range(1, n + 1):
        out += f(i)
        if i % 1000 == 0:
            print(i)
    return out


plik = open('wynik.txt', 'w')
plik.write(str(s(10 ** 16)))
plik.close()

