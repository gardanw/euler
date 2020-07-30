import numpy as np

n = 1001
lista = [1]
krok = 2
while lista[-1] != n * n:
    control = 0
    for i in range(lista[-1], n * n + 1, krok):
        if i in lista:
            continue
        else:
            lista.append(i)
            control += 1
        if control == 4:
            break
    krok += 2

print(sum(lista))
