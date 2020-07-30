# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 13:29:00 2019

@author: Damian
"""


number = 297058020
def roz(number):
    prim = 2
    
    while number > 1:
        if number % prim == 0:
            number /= prim
        else:
            prim += 1
    
    return prim



#number = 600851475143
def rozklad(number):
    dzielnik = 2
    
    lista_pierwszych = []
    
    while dzielnik < number/2:
        lista_pom = []
        for i in range(1,int(dzielnik**(0.5))+1):
            if dzielnik%i == 0:
                lista_pom.append(i)
        if len(lista_pom) == 1:
            if number%dzielnik == 0:
                lista_pierwszych.append(dzielnik)
                spr = 1
                for j in lista_pierwszych:
                    spr *= j
                if spr == number:
                    break
        dzielnik += 1
    return lista_pierwszych
# ind = 1
# lista1 =[]
# for i in range(100):
#     lista = rozklad(i)
#     if len(lista) != 0 and max(lista) > i**0.5:
#         ind += 1
#         lista1.append(i)
# #    if i%1000 == 0:
# #        print(i, ind)
# print(ind)
# print(lista1)
lista1 = []
ind = 1
for i in range(1000000):
    if roz(i) < i**0.5:
        ind += 1
        # lista1.append(i)
    if i % 100000 == 0:
        print(i, ind)
print(ind)
print(len(lista1))