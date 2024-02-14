açı1 = int(input("ilk açıyı girin \n"))
açı2 = int(input("ikinci açıyı girin \n"))
açı3 = int(input("son açıyı girin \n"))
toplam = açı1 + açı2 + açı3
if açı1 != 0 and açı2 != 0 and açı3 != 0:
 if toplam == 180:
     if açı3 == açı1 == açı2 :
        print("eşkenar üçgen")
     elif açı2 == açı1 or açı3 == açı2 or açı1 == açı3 :
        print("ikizkenar üçgen")
     else :
        print("çeşitkenar üçgen")
else :
    print("bunun bir üçgen olduguna emin misin")