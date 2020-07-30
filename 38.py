list_namber = []
for number in range(1, 10000):
    string = ''
    iterator = 1
    while len(string) < 9:
        string += str(number * iterator)
        iterator += 1
    if '0' not in string:
        temp = 0
        for i in range(1,10):
            if string.count(str(i)) != 1:
                temp += 1
        if temp == 0:
            list_namber.append(int(string))
print(max(list_namber))
