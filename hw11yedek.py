açı1=int(input("1.açıyı giriniz \n"))
açı2=int(input("2.açıyı giriniz \n"))
açı3=int(input("3.açıyı giriniz \n"))
toplam=açı1+açı2+açı3
if açı1!= 0 and açı2 != 0 and açı3 != 0 :
    if toplam == 0:
        if açı3==açı1==açı2 :
            print("eşkenar üçgen")
        elif açı1== açı2  or açı3== açı2 or açı1==açı3:
            print("ikiz kenar üçgen")
        else :
            print("çeşitkenar üçgen")
    else :
        print("bunun üçgen olduğuna eminmisin")