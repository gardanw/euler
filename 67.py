# -*- coding: utf-8 -*-
plik = open("p067_triangle.txt")
lista = []
for linia in plik:
    pom = []
    pom2 = []
    for i in range(len(linia)-1):
        if linia[i] != " ":
            pom2.append(linia[i])
        if len(pom2) == 2:
            pom.append(int(''.join(pom2)))
            pom2 = []
    lista.append(pom)
#for i in lista:
#    print(i)
lista_wartosci = []
for i in lista:
    pom = []
    for j in range(len(i)):
        pom.append(0)
    lista_wartosci.append(pom)
lista_wartosci[0][0] = lista[0][0]
for i in range(1, len(lista)):
    lista_wartosci[i][0] = lista_wartosci[i-1][0] + lista[i][0]
    lista_wartosci[i][-1] = lista_wartosci[i-1][-1] + lista[i][-1]
    for j in range(1,len(lista[i])-1):
        if lista_wartosci[i-1][j-1] > lista_wartosci[i-1][j]:
            lista_wartosci[i][j] = lista_wartosci[i-1][j-1] + lista[i][j]
        else:
            lista_wartosci[i][j] = lista_wartosci[i-1][j] + lista[i][j]
    
#for i in lista_wartosci:
#    print(i)
print(max(lista_wartosci[-1]))
    
    