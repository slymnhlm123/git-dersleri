plaka = int(input('plaka kodu giriniz \n'))

if plaka == 1903 or plaka <= 81 :
    if plaka == 6 :
        print("angara")
    elif plaka == 7 :
        print("antalya")
    elif plaka == 8 :
        print("artvin")
    elif plaka == 57 :
        print("Sinop")
    elif plaka == 58 :
        print("Sivas")    
    elif plaka == 1903 :
        print("Beşiktaşşş")
    else :
        print("Türkiye")
else:
    print("bu bir plaka kodu değil")