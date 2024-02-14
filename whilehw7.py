say1  = float(input("ilk sayıyı girin \n"))
say2 = float(input("ikinci sayıyı giriniz\n"))
ort = (say1+say2)/2

while say1<say2:
    ort+=say1
    say1 += 1
print(ort)