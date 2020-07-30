lista = []

for i in range(100):
    for j in range(i,10000):
        k = i*j
        string = str(k)+str(i)+str(j)
        if len(string) == 9:
            pom = 0
            for l in range(1, 10):
                if string.count(str(l)) == 1:
                    pom += 1
            if pom == 9 and k not in lista:
                lista.append(k)
print(sum(lista))