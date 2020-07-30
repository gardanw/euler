# -*- coding: utf-8 -*-


#liczba = 999999
#for i in range(1,int(liczba)+1):
#    if liczba%i == 0:
#        print(i)
lista = []
for i in range(900):
    for j in range(900):
        pom = (999-j)*(999-i)
        pom = str(pom)
        if pom == pom[::-1]:
#            print(pom, 999-i, 999-j)
            lista.append(int(pom))
#    print(999*(999-i))
print(max(lista))