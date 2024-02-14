print("merhabalar muhterem efendim")

sınav_notu1 =float(input("1. sınav notunuz giriniz muhterem efendim\n"))
sınav_notu2 =float(input("2. sınav notunuz giriniz muhterem efendim\n"))
performans_notu =float(input("son olarak performans notunuz giriniz muhterem efendim \n"))
ortalama=(sınav_notu1+sınav_notu2+performans_notu)/3


if ortalama >= 50 :
    print("başarılısınız muhterem efendin")

else:
    print("üzgünüz ki başarısızsınız muhterem efendim ")