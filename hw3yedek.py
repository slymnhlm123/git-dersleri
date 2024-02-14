max=20

bagaj_kg=float(input("bagaj kilonuzu giriniz"))

ybbagaj=round(bagaj_kg,0)

if ybbagaj <= max:
    print("ek ücret ödemeyeceğniz")
else:
    print("ödemeniz gereken ücret""tl")

