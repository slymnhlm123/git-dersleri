çarpılan=int(input("bölmek istediğniz sayıyı giriniz\n"))
çarpan=int(input("girdiğniz sayıyı hangi sayıyla bölmek istersiniz \n"))

toplam=0

for i in range(çarpılan):
  toplam -= çarpan
print(toplam)