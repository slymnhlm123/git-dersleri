def bagaj_ucret_hesapla(agirlik):
    bagaj_limit = 20
    ek_ucret_miktari = 10
    
    if agirlik <= bagaj_limit:
        print("Herhangi bir ücret ödemeniz gerekmiyor.")
    else:
        fazla_agirlik = agirlik - bagaj_limit
        ek_ucret = fazla_agirlik * ek_ucret_miktari
        print("Fazla bagaj için" ,ek_ucret," TL ödemelisiniz.")

# Kullanıcıdan bagaj ağırlığını alınması için örnek:
bagaj_agirlik = float(input("Bagaj ağırlığınızı kilogram cinsinden giriniz: "))
bagaj_ucret_hesapla(int(bagaj_agirlik))
