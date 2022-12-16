hetnapjai = ["Hétfő","Kedd","Szerda","Csütörtök","Péntek","Szombat","Vasárnap"]
# print(hetnapjai)
# for i in range(len(hetnapjai)):
#     hetnapjai[i] = hetnapjai[i].lower()
hetnapjai_kisbetu = [item.lower() for item in hetnapjai]
hetnapjai_nagybetu = [item.upper() for item in hetnapjai]

beker = input("Kérem a napot!").upper()

if beker in hetnapjai_nagybetu:
    print(f"{beker} nap bene van a klistában")
else:
    print(f"{beker} nap nincs a listában")



