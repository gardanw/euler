# -*- coding: utf-8 -*-
kale = {2:28, 7:31}
for i in range(12):
    if i < 6:
        if (i+1)%2 == 0 and i+1 not in kale:
            kale[i+1] = 30
        elif (i+1)%2 != 0 and i+1 not in kale:
            kale[i+1] = 31
    else:
        if (i+1)%2 == 0 and i+1 not in kale:
            kale[i+1] = 31
        elif (i+1)%2 != 0 and i+1 not in kale:
            kale[i+1] = 30
#for i in range(1,13):
#    print(kale[i])
sun = 0
rok = 1
i = 1
pom = 0
while i < 1200:
    if i%12 == 0:
        rok += 1
    for j in range(1,13):
        if j == 2 and rok%4 == 0:
#            print(((kale[j]+1)%7+ pom)%7)
            if ((kale[j]+1)%7 + pom)%7 == 0:
                pom += (kale[j]+1)%7
                pom = pom%7
                sun += 1
            else:
                pom += (kale[j]+1)%7
                pom = pom%7
        else:
#            print(((kale[j])%7+ pom)%7)
            if ((kale[j])%7 + pom)%7 == 0:
                pom += kale[j]%7
                pom = pom%7
                sun += 1
            else:
                pom += kale[j]%7
                pom = pom%7
        i += 1
print(sun)