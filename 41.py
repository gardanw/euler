def prime(number):
    for i in range(2, int((number) ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

number = 987654321
while True:
    if '0' not in str(number) and number % 2 != 0 :
        temp = 0
        for i in range(len(str(number)) + 1, 10):
            if str(number).count(str(i)) > 0:
                temp += 1
                break
        for i in range(1, len(str(number)) + 1):
            if str(number).count(str(i)) > 1:
                temp += 1
                break
        if temp == 0 and prime(number):
            print(number)
            break
    number -= 1
