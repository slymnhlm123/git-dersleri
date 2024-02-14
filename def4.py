def indirim():


 fiyat1 = float(input('ilk fiyatı girin efendim'))
 fiyat2 = float(input('ikinci fiyatı girin efendim'))
 toplam = fiyat1 + fiyat2
 indirim = toplam * 0.75
if indirim <= 200 :
    print("ödenecek miktar",indirim,"TL")
else :
    print("indirimli fiyat",indirim,"TL")