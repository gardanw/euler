from math import factorial

lista = []
for i in range(3, 100000):
    pom = list(str(i))
    suma = 0
    for p in pom:
        suma += factorial(int(p))
    if suma == i:
        lista.append(i)
print(sum(lista))