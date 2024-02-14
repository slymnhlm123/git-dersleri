#3)  0-100 (100 dâhil) arasındaki sayılardan 5’e tam bölünenleri 
# döngüsü ile ekrana yazdırınız. 

sayı = 0 
 
while sayı <= 100 :
    if sayı % 5 == 0 :
        print(sayı)
    sayı += 5   