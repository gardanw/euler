# -*- coding: utf-8 -*-
def d(n):
    lista = []
    for i in range(1, int(n/2)+1):
        if n%i == 0:
            lista.append(i)
    return sum(lista)

lista_par = []
for i in range(10001):
    if i not in lista_par:
        pom = d(i)
        pom2 = d(pom)
        if i == pom2 and i != pom and pom not in lista_par:
            lista_par.append(pom)
            lista_par.append(pom2)
print(sum(lista_par))
