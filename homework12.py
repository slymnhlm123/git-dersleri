kilo = float(input("kilonuzu giriniz"))
boy = float(input("boyunuzu metre cinsinden yaziniz"))

vki = kilo / (boy*boy)

if 18 < vki < 25:
    print("normal")
elif 25 < vki < 30 :
    print("kilolu")
elif 30 <= vki:
    print("obez")
elif 35 <= vki:
    print("ciddi obezzzz")
else :
    print("çubuk")