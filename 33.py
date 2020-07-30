lista = []
for licznik in range(11, 100):
    for mianownik in range(licznik + 1, 100):
        ulamek = licznik / mianownik
        ulamek_test = 0
        if str(licznik)[0] in str(mianownik) and str(licznik)[0] != '0':
            m = list(str(mianownik))
            m.remove(str(licznik)[0])
            if int(str(licznik)[1]) == 0 or int(''.join(m)) == 0:
                continue
            ulamek_test = int(str(licznik)[1]) / int(''.join(m))
        elif str(licznik)[1] in str(mianownik) and str(licznik)[1] != '0':
            m = list(str(mianownik))
            m.remove(str(licznik)[1])
            if int(str(licznik)[0]) == 0 or int(''.join(m)) == 0:
                continue
            ulamek_test = int(str(licznik)[0]) / int(''.join(m))
        if ulamek == ulamek_test:
            lista.append((licznik, mianownik))
print(lista)