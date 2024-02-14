sayı1 = float(input("ilk sayıyı giriniz"))
sayı2 = float(input("ikinci sayıyı giriniz"))
sayı3 = float(input("üçünçü sayıyı giriniz"))

if sayı1 > sayı2 and sayı1 > sayı3 :
    if sayı2 > sayı3 :
        print(sayı1,">",sayı2,">",sayı3)
    else :
        print(sayı1,">",sayı3,">",sayı2)
elif sayı2 > sayı1 and sayı2 > sayı3 :
    if sayı1 > sayı3 :
        print(sayı2,">",sayı1,">",sayı3)
    else :
        print(sayı2,">",sayı3,">",sayı1)
elif sayı3 > sayı1 and sayı2 :
    if sayı2 > sayı1 :
        print(sayı3,">",sayı2,">",sayı1)
    else :
        print(sayı3,">",sayı1,">",sayı2)