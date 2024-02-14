üçgen=180
açı1=int(input("1. açıyı giriniz\n"))
açı2=int(input("2.açıyı giriniz\n"))
açı3=int(input("3.açıyı giriniz\n"))

iç_açı_toplamı=(açı1+açı2+açı3)

if iç_açı_toplamı == üçgen:
    print("bu bir üçgen")
else:
    print("bu bir üçgen değil")
   