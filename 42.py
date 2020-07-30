
def liczby_trojkata(n):
    lista = []
    for i in range(1, n+1):
        lista.append(0.5*i*(i+1))
    return lista

def odczytywanie_z_pliku(plik):
    z_pliku = open(plik)
    lista_slow = []
    for linia in z_pliku:
        pomocnicza = []
        for i in range(len(linia)):
            if linia[i] != '"' and linia[i] != ',':
                pomocnicza.append(linia[i])
            elif linia[i] == ',':
                lista_slow.append(''.join(pomocnicza))
                pomocnicza = []
    return lista_slow

def sumowanie(lista_ze_slowami, alfabet):
    lista_sum = []
    for slowo in lista_ze_slowami:
        suma = 0
        for i in range(len(slowo)):
            suma += alfabet[slowo[i]]
        lista_sum.append(suma)
    return lista_sum

def sprawdz_czy_trojkat(sumy, lista_slow, lista_liczb):
    slowa_trojkaty = []
    for i in range(len(sumy)):
        if sumy[i] in lista_liczb:
            slowa_trojkaty.append(lista_slow[i])
    return slowa_trojkaty


alfabet = {}
for i in range(26):
    alfabet[chr(65+i)] = i + 1

print(len(sprawdz_czy_trojkat(sumowanie(odczytywanie_z_pliku('p042_words.txt'),alfabet),odczytywanie_z_pliku('p042_words.txt'),liczby_trojkata(30))))
print(alfabet)
print(odczytywanie_z_pliku('p042_words.txt'))
