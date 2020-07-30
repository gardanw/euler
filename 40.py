string = ''
iterator = 1
while len(string) < 1000000:
    string += str(iterator)
    iterator += 1
print(int(string[0])*int(string[9])*int(string[99])*int(string[999])*int(string[9999])*int(string[99999])*int(string[999999]))