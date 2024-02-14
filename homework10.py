oto=float(input("otoparkta kaç saat kaldınız \n"))
birbesarası= oto * 4
besustu= oto * 3

if oto <= 1 :
    print("ÖDEMENİZ GEREKEN MİKTAR 5 TL")
elif 1 < oto <= 5 :
    print("ödemeniz gereken miktar", birbesarası , "TL")
else :
    print("ödemeniz gereken miktar", besustu , "TL")