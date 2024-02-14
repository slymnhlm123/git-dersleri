ürün1=float(input("1. ürünün fiyatını giriniz"))
ürün2=float(input("2. ürünün fiyatını giriniz"))
toplam= ürün1+ürün2
indirim= toplam*0.75
if toplam <= 200 :
    print("ödenecek miktar",toplam,"TL")

else :
    print("ödenec miktar",indirim,"TL") 