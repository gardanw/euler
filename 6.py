# -*- coding: utf-8 -*-

sum1 = 0
sum2 = 0
for i in range(101):
    sum1 += i**2
    sum2 += i
    
odp = -sum1 + (sum2**2)
print(odp) 