#   DEĞİŞKENLER #

# kullanıcı adı ve şifresi

toplam = 0
sifre = "yeb1888"
kullanıcıadı = "yeb1888"
kullanıcıadınız = input("kullanıcı adınızı giriniz\n")
şifreniz = input("şifrenizi giriniz\n")


while True:
    if kullanıcıadınız == kullanıcıadı and şifreniz == sifre:
        print("Giriş Başarılı")
    else:
        print("kullanıcı adı veya şifre hatalı")
        break

    anay = {"1 = Tavuk Döner": 100, "2 = Pizza": 150, "3 = Pide": 80, "4 = Lahmacun": 50}
    tatlılar = ["5 = Sütlaç", 50, "6 = Künefe", 80, "7 = Yaş Pasta", 45, "8 = Baklava", 80]
    içeçek = ["9 = Gazoz", 10, "10 = Oralet", 5, "11 = Su", 2, "12 = Kahve", 20,
              "13 = Ayran", 15, "14 = White Chocolate Mocha Coffe", 80]
    salatalar = ["15 = Tavuk Salatası", 90, " 16 = Amerikan Salatası", 50]
    ana = []
    tatlı = []
    içek = []
    salat = []
    notlar = {"Ana Yemek": [], "Tatlı": [], "İçecek": [], "Salata": []}

    seçim = input("1 = Ana Yemek\n2 = Tatlı\n3 = İçecek\n4 = Salatalar\n0 = Çıkış\n")
    if seçim == "0":
        if toplam > 999:
            print("Ücretiniz : ", toplam / 0.3)
            print("Çıkılmaktadır Efenim...")
        else:
            print("Ücretiniz : ", toplam)
            print("Çıkılmıştır  ")
        break

    # ana yemek
    if seçim == "1":
        print(anay)
        siparis = int(input("Yukardakilerden Birini Seçiniz\n"))
        kaç_tane = int(input("Kaç tane Alınacak\n"))
        if siparis == 1:
            fiyat = 100 * kaç_tane
            toplam += fiyat
            ana.append(kaç_tane)
            ana.append("Tavuk Döner")
            ana.append(fiyat)
            print(ana)

        elif siparis == 2:
            fiyat = 150 * kaç_tane
            toplam += fiyat
            ana.append(kaç_tane)
            ana.append("Pizza")
            ana.append(fiyat)
            print(ana)

        elif siparis == 3:
            fiyat = 80 * kaç_tane
            toplam += fiyat
            ana.append(kaç_tane)
            ana.append("Pide")
            ana.append(fiyat)
            print(ana)

        elif siparis == 4:
            fiyat = 50 * kaç_tane
            toplam += fiyat
            ana.append(kaç_tane)
            ana.append("Lahmacun")
            ana.append(fiyat)
            print(ana)

    # tatlılar
    if seçim == "2":
        print(tatlılar)
        siparis = int(input("Yukardakilerden Birini Seçiniz\n"))
        kaç_tane = int(input("Kaç tane Alınacak\n"))
        if siparis == 5:
            fiyat = 50 * kaç_tane
            toplam += fiyat
            tatlı.append(kaç_tane)
            tatlı.append("Sütlaç")
            tatlı.append(fiyat)
            print(tatlı)

        elif siparis == 6:
            fiyat = 80 * kaç_tane
            toplam += fiyat
            tatlı.append(kaç_tane)
            tatlı.append("Künefe")
            tatlı.append(fiyat)
            print(tatlı)

        elif siparis == 7:
            fiyat = 45 * kaç_tane
            toplam += fiyat
            tatlı.append(kaç_tane)
            tatlı.append("Yaş pasta")
            tatlı.append(fiyat)
            print(tatlı)

        elif siparis == 8:
            fiyat = 80 * kaç_tane
            toplam += fiyat
            tatlı.append(kaç_tane)
            tatlı.append("Baklava")
            tatlı.append(fiyat)
            print(tatlı)

    # içecek
    if seçim == "3":
        print(içeçek)
        siparis = int(input("Yukardakilerden Birini Seçiniz\n"))
        kaç_tane = int(input("Kaç tane Alınacak\n"))
        if siparis == 9:
            fiyat = 10 * kaç_tane
            toplam += fiyat
            içek.append(kaç_tane)
            içek.append("Gazoz")
            içek.append(fiyat)
            print(içek)

        elif siparis == 10:
            fiyat = 5 * kaç_tane
            toplam += fiyat
            içek.append(kaç_tane)
            içek.append("Oralet")
            içek.append(fiyat)
            print(içek)

        elif siparis == 11:
            fiyat = 2 * kaç_tane
            toplam += fiyat
            içek.append(kaç_tane)
            içek.append("Su")
            içek.append(fiyat)
            print(içek)

        elif siparis == 12:
            fiyat = 20 * kaç_tane
            toplam += fiyat
            içek.append(kaç_tane)
            içek.append("Kahve")
            içek.append(fiyat)
            print(içek)

        elif siparis == 13:
            fiyat = 15 * kaç_tane
            toplam += fiyat
            içek.append(kaç_tane)
            içek.append("Ayran")
            içek.append(fiyat)
            print(içek)

        elif siparis == 14:
            fiyat = 80 * kaç_tane
            toplam += fiyat
            içek.append(kaç_tane)
            içek.append("white chocolate mocha coffe")
            içek.append(fiyat)
            print(içek)

        not_isteme = input("Not Girmek İster Misiniz (E/H)")
        if not_isteme == "E":
            girilen_not = input("Notunuzu Girin\n")
            notlar["İçecek"].append({"Sipariş": siparis, "Not": girilen_not})

    print("*******************************************************************************************************************************************")

    # salatalar
    if seçim == "4":
        siparis = int(input("Yukardakilerden Birini Seçiniz\n"))
        kaç_tane = int(input("Kaç tane Alınacak\n"))
        if siparis == 15:
            fiyat = 90 * kaç_tane
            toplam += fiyat
            salat.append(kaç_tane)
            salat.append("Tavuk Salatası")
            salat.append(fiyat)
            print(salat)

        elif siparis == 16:
            fiyat = 50 * kaç_tane
            toplam += fiyat
            salat.append(kaç_tane)
            salat.append("Amerikan Salatası")
            salat.append(fiyat)
            print(salat)

        elif siparis > 16 or siparis < 1:
            print("Öyle Bir Ürün Bulunamadı")


    print("*******************************************************************************************************************************************")

