sayı1 = int(input("ilk sayıyı giriniz efendim \n"))
sayı2 = int(input("ikinci sayıyı giriniz efendim \n"))

if sayı2 > sayı1:
    while sayı1+1 != sayı2 :
       sayı1 += sayı1 +1
       print(sayı1)
else :
    while sayı2 +1 != sayı1 :
        sayı2 += sayı1 +1
        print(sayı2)      
             

