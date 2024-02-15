kilo=float(input("kilonuzu giriniz\n"))
boy=float (input("boyunuzu metre cinsinden giriniz\n"))
vki= kilo /(boy*boy)
if 18<vki<25:
    print("normal")
elif 25<vki<30:
    print("kilolu")
elif 30<=vki:
    print("obez")
elif 35 <= vki:
    print("abi yeme obezitesin hemde aşırııııııı")
else :
    print("az ye be çubuk")