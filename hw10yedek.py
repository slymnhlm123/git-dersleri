oto=float(input("otoparkta kaç saat kaldınız"))
besüstü= oto*3
birbesarası=oto*4
if oto <= 1:
    print("ÖDEMENİZ GEREKEN MİKTAR 5 TL ")
elif 1 < oto <= 5 :
    print("ödemeniz gereken miktar", birbesarası , "TL")
else :
    print("ödemeniz gereken miktar", besüstü , "TL")
