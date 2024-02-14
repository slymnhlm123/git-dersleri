sınavnotu1=float(input("1.sınav notunuzu giriniz\n"))
sınavnotu2=float(input("2.sınav notunuzu giriniz\n"))
performans=float(input("performans notunuzu giriniz\n"))
oratlama=(sınavnotu1 + sınavnotu2 +performans )/3
if oratlama <= 50 :
    print("başarısız")
else: 
   print("başarılı")
      