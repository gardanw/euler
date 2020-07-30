import numpy as np
def prime(liczba):
    flaga = 0
    for i in range(2,int(np.sqrt(liczba))+1):
        if liczba%i == 0:
            flaga += 1
    if flaga == 0:
        return True
    else:
        return False
lista = []
for i in range(100, 1000000):
    if prime(i) and i not in lista:
        temp = list(str(i))
        temp1 = []
        for j in range(len(temp)):
            temp.append(temp.pop(0))
            if not prime(int(''.join(temp))):
                break
            temp1.append(int(''.join(temp)))
            if j == len(temp)-1:
                lista += temp1

print(len(lista)+13)