lista= [1,2,3,4,5,6,7,8]
lista.append(10)
print(lista)
for i in range(len(lista)):
    print(lista[i])
print("************************************")
for i in range(len(lista)):
    if lista[i] > 5:
        print(lista[i])
print("***********************************")
for item in lista:
    if item > 5:
        print(item)
print("************************************")
import random

lista = []
for i in range(10):
    lista.append(random.randint(0,40))
    print(lista[i])
print("***********************************")

lista = []
for i in range(len(lista)):
    if lista[i]%2 == 0: 
        print(lista)


for item in lista:
    if item %2 == 0:
        print(item)

jatekok = ["Fifa, Valorant, Fortnite, Pubg, Fall Guys"]
print(jatekok)
print("********************")
for i in range(len(lista)):
    print(lista[i])
print("********************")
for item in jatekok:
    

