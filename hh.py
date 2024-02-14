Ana_Yemekler = {"İskender": 40, "Adana": 20, "Köfte": 15,}
Salatalar = {"çoban": 10, "Akdeniz": 10, "Gavurdağı": 15}
Tatlılar = {"Baklava": 25, "Künefe": 20, "Kadayıf": 15}

Seçilen_Ana_Yemekler = []
Seçilen_Salatalar = []
Seçilen_Tatlılar = []
toplam=0
while True:
    Seçim = input("Restoranımıza Hoş Geldiniz Sipariş Katogorisini Seçiniz\n"
                   "1 Ana Yemekler\n"
                   "2 Salatalar\n"
                   "3 Tatlılar\n"
                   "0 Çıkış Yap\n")
    if Seçim == "0":
        print("restoranddan çıkılıyor...")
        break

  #anayemek
    if Seçim == "1":
        print(Ana_Yemekler)
        katagori=input("hangi yemeği yicen\n")
        
    if katagori == "iskender":
        fiyat=40
        toplam+=fiyat
        Seçilen_Ana_Yemekler.append(katagori)
        Seçilen_Ana_Yemekler.append(fiyat)
        print(Seçilen_Ana_Yemekler)

    if katagori == "adana":
        fiyat=20
        toplam+=fiyat
        Seçilen_Ana_Yemekler.append(katagori)
        Seçilen_Ana_Yemekler.append(fiyat)
        print(Seçilen_Ana_Yemekler)

if katagori == "köfte":
        fiyat=15
        toplam+=fiyat
        Seçilen_Ana_Yemekler.append(katagori)
        Seçilen_Ana_Yemekler.append(fiyat)
print(Seçilen_Ana_Yemekler)




#salatalar

if Seçim == "2":
        print(Salatalar)
        katagori=input("hangi yemeği yicen\n")
        
if katagori == "çoban":
        fiyat=10
        toplam+=fiyat
        Seçilen_Salatalar.append(katagori)
        Seçilen_Salatalar.append(fiyat)
        print(Seçilen_Salatalar)

if katagori == "akdeniz":
        fiyat=10
        toplam+=fiyat
        Seçilen_Salatalar.append(katagori)
        Seçilen_Salatalar.append(fiyat)
        print( Seçilen_Salatalar)

if katagori == "gavurdağı":
        fiyat=15
        toplam+=fiyat
        Seçilen_Salatalar.append(katagori)
        Seçilen_Salatalar.append(fiyat)
print(Seçilen_Salatalar)


#tatlılar
if Seçim == "3":
        print(Tatlılar)
        katagori=input("hangi yemeği yicen\n")
        
if katagori == "baklava":
        fiyat=25
        toplam+=fiyat
        Seçilen_Tatlılar.append(katagori)
        Seçilen_Tatlılar.append(fiyat)
        print(Seçilen_Tatlılar)

if katagori == "künefe":
        fiyat=20
        toplam+=fiyat
        Seçilen_Tatlılar.append(katagori)
        Seçilen_Tatlılar.append(fiyat)
        print( Seçilen_Tatlılar)

if katagori == "kadayıf":
        fiyat=15
        toplam+=fiyat
        Seçilen_Tatlılar.append(katagori)
        Seçilen_Tatlılar.append(fiyat)
print(Seçilen_Tatlılar)