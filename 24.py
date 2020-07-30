# -*- coding: utf-8 -*-
from itertools import permutations
lista = ['0','1','2','3','4','5','6','7','8','9']
per = permutations(lista)
per = list(per)
print(''.join(list(per[1000000 - 1])))

