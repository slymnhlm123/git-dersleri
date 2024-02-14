fiyat1 = float(input('ilk fiyatı girin efendim'))
fiyat2 = float(input('ikinci fiyatı girin efendim'))
toplam = fiyat1 + fiyat2
indirim = toplam * 0.75
if toplam <= 200 :
    print("ödenecek miktar",toplam,"TL")
else :
    print("indirimli fiyat",indirim,"TL")