magassag = int(input("Mekkora karácsonyfa legyen?"))
for i in range(magassag):
    for j in range(magassag-i):
        print(' ',end=' ')
    for k in range(2*i+1):
        print('*',end=' ')
    print()
for i in range(5):
    for j in range(5-i):
        print(' ',end=' ')
    for k in range(2*i+1):
        print('*',end=' ')
    print()

for i in range(magassag):
    for j in range(magassag-1):
        print(' ',end=' ')
    print('* * * *')
