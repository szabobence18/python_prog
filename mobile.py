mobilok = ["Iphone 11", "Samsung Galaxy A80", "Xiaomi 11", "Nokia Lumia 620"]

print(mobilok)
for item in mobilok:
    print(item)
print("**************************")

mobilok.append("Alcatel OneTouch POP")
mobilok.pop(0)
mobilok.pop(1)
mobilok.clear()
for i in range(len(mobilok)):
    print(mobilok[i])



