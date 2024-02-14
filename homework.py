print("Merhabalar")

butce = float(input("Başlangıç bütçenizi girin: "))

alinan_urunler = []

while True:
    
    urun = input("Alınan ürünü girin (Çıkmak için 'q' girin): ")
    

    if urun == 'q':
        break
    
    fiyat = float(input(urun + " için fiyatı girin: "))
    
    
    if fiyat > butce:
        print("Uyarı: Bütçeyi aştınız! Alışverişi tamamlıyorsunuz.")
        break
    else:
        butce -= fiyat
        alinan_urunler.append((urun, fiyat))
        print(urun + " başarıyla eklendi. Kalan bütçe: " + str(butce))

alinan_urunleri = "Alınan Ürünler:\n"
for urun, fiyat in alinan_urunler:
    alinan_urunleri += urun + ": " + str(fiyat) + " TL\n"

print(alinan_urunleri + "Alışveriş tamamlandı. Kalan bütçe: " + str(butce))