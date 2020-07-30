# -*- coding: utf-8 -*-

def dzielniki(liczba):
    lista = []
    for i in range(1, int(liczba/2)+1):
        if liczba%i == 0:
            lista.append(i)
    if len(lista) == 0:
        lista.append(1)
    return lista

slownik = {}
liczna = []
niedobor = []
doskonala = []
liczby = []
for i in range(1, 28124):
    slownik[i] = dzielniki(i)
    if sum(slownik[i]) > i:
        liczna.append(i)
#    if len(liczna) != 0 and liczna[-1] + liczna[-1] > 28124:
#        break
print('done 1')
sumy = []
for i in range(len(liczna)):
    for j in range(i, len(liczna)):
        if liczna[i] + liczna[j] in slownik:
            del slownik[liczna[i]+liczna[j]] 
for i in range(28124):
    if i in slownik:
        sumy.append(i)
print(sum(sumy))