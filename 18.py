# -*- coding: utf-8 -*-
lista = [[75], [95, 64], [17, 47, 82], [18, 35, 87, 10], [20, 4, 82, 47, 65], [19, 1, 23, 75, 3, 34], [88, 2, 77, 73, 7, 63, 67], [99, 65, 4, 28, 6, 16, 70, 92], [41, 41, 26, 56, 83, 40, 80, 70, 33], [41, 48, 72, 33, 47, 32, 37, 16, 94, 29], [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14], [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57], [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48], [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31], [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]
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
#for i in range(1,len(lista)):
    
for i in lista_wartosci:
    print(i)
print(max(lista_wartosci[-1]))
    
    