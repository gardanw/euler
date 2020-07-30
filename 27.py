def pierwsza(liczba):
    l = int((liczba**2)**0.5)
    for i in range(2, int(l**0.5 + 1)):
        if liczba % i == 0:
            return False
    return True


odp = {'a': 0, 'b': 0, 'pierwsze': []}
lista = []
for a in range(-999, 1000):
    for b in range(-999, 1000):
        for n in range(int((b**2)**0.5)):
            if pierwsza((n ** 2) + (a * n) + b):
                lista.append(n)
            else:
                break
        if len(odp['pierwsze']) < len(lista):
            odp['a'] = a
            odp['b'] = b
            odp['pierwsze'] = lista
        lista = []
print(odp['a']*odp['b'], odp)