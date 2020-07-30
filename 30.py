lista = []
for i in range(2, 200000):
    x = str(i)
    suma = 0
    for cyfra in x:
        suma += int(cyfra) ** 5
    if suma == i:
        lista.append(i)
print(lista, sum(lista))
