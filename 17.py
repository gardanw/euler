# -*- coding: utf-8 -*-
baza = {1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 10:3, 11:6, 12:6, 13:8, 15:7, 18:8, 20:6, 30:6, 40:5, 50:5, 60:5, 70:7, 80:6, 90:6, 1000:11}
for i in range(13, 20):
    if i not in baza:
        baza[i] = 4 + baza[i-10]
for j in range(20,100,10):
    for i in range(1,10):
        baza[j+i] = baza[j] + baza[i]
for i in range(100,1000,100):
    baza[i] = baza[i/100] + 7
    for j in range(1,100):
        baza[i+j] = baza[i] + baza[j] + 3
suma = 0
for i in range(1, 1001):
    suma += baza[i]
print(suma)