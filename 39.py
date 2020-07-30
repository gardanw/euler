dic = {}
for i in range(1, 500):
    for j in range(i, 500):
        if (i + j + (i ** 2 + j ** 2) ** 0.5) % 1 == 0 and i + j + (i ** 2 + j ** 2) ** 0.5 <= 1000:
            if i + j + (i ** 2 + j ** 2) ** 0.5 not in dic:
                dic[i + j + (i ** 2 + j ** 2) ** 0.5] = [[i, j, (i ** 2 + j ** 2) ** 0.5]]
            else:
                dic[i + j + (i ** 2 + j ** 2) ** 0.5].append([i, j, (i ** 2 + j ** 2) ** 0.5])
for i in dic:
    print(dic[i])
print(sum([240, 252, 348.0]))