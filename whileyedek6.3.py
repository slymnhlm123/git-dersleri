sayı1=int(input("ilk sayıyı giriniz"))
sayı2=int(input("2.sayıyı giriniz"))
if sayı2 > sayı1:
    while sayı1+1 != sayı2:
        sayı1+= sayı1+1
        print(sayı1)
else :
    while sayı2 +1 != sayı1:
        sayı2 += sayı1 +1 
        print (sayı2)