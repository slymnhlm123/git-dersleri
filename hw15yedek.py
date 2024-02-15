tercih = input("sinemaya mı gideceksiniz tiyatroya mı \n")
tercih2 = input("öğrenci misiniz yoksa yetişkin misiniz \n")

if tercih == "tiyatro":
    if tercih2 == "öğrenci":
        print("ödeyeceginiz fiyat 5 tl")
    elif tercih2 == "yetişkin" :
        print("ödeyeceginiz miktar 10 tl")
elif tercih== "sinema" :
    if tercih2 == "ögrenci":
        print("ödeyeceginiz miktar 7.5 tl")
    elif tercih2 == "yetişkin" :
        print("ödeyeceginiz miktar 15tl")
