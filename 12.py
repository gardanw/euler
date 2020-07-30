dzielniki = []
iterator = 1
liczba = 0
while 2*len(dzielniki) <= 500:
	dzielniki = []
	liczba += iterator
	dzielniki.append(liczba)
	for i in range(1, int(((liczba+1)/2)**0.5)+1):
		if liczba % i == 0:
			dzielniki.append(i)
	if liczba % 100000 == 0:
		print(liczba)
		print(2*len(dzielniki), dzielniki)
	iterator += 1
print(liczba)
			