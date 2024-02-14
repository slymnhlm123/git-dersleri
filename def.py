def notal(sınavno):
    sınav_notu = float(input(sınavno + ". notunuzu girin\n : "))
    return sınav_notu
      

def notu ():
    birinci_sınav_notu = notal("1")
    ikinci_sınav_notu = notal("2")
    performans_notu = notal ("3")
    Toplam = ( int(birinci_sınav_notu) + int(ikinci_sınav_notu) + int(performans_notu) )
    Ortalama= ( Toplam / 3)
    if (Ortalama > 50) :
           print("Başarılı")
    elif (Ortalama < 50) :   
           print("Başarısız")
    return Ortalama