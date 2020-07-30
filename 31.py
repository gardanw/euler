cel = 200
menety = [1, 2, 5, 10, 20, 50, 100, 200]
drogi = [1] + [0] * cel

for moneta in menety:
    for i in range(moneta, cel + 1):
        drogi[i] += drogi[i - moneta]
print(drogi[-1])


