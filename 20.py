# -*- coding: utf-8 -*-
x = 1
for i in range(1,101):
    x *= i
print(sum([int(i) for i in str(x)]))