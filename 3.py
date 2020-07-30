# -*- coding: utf-8 -*-


number = 600851475143

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
            print(dzielnik, lista_pierwszych)
            
    dzielnik += 1
    
print(spr, dzielnik, lista_pierwszych)

number = 297058020
prim = 2

while number > 1:
    if number % prim == 0:
        number /= prim
    else:
        prim += 1

print(prim)

