liczba = 10**6
lista = []
while liczba > 1:
    ciag = []
    p_ciagu = liczba
    ciag.append(p_ciagu)
    while p_ciagu > 1:
        if p_ciagu % 2 == 0:
            p_ciagu = p_ciagu/2
        else:
            p_ciagu = 3*p_ciagu + 1
            ciag.append(p_ciagu)
    lista.append(ciag)
    if liczba % 1000 == 0:
        print(liczba)
    liczba -= 1
lista_pom = []
for i in lista:
    lista_pom.append(len(i))
print(lista[lista_pom.index(max(lista_pom))])