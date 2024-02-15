# 13. Soru
tek_sayilar = []

for sayi in range(1, 31):
    if sayi % 2 == 1:
        tek_sayilar.append(sayi)

print("\n1 ile 30 arasındaki tek sayılar:")
for tek_sayi in tek_sayilar:
    print(tek_sayi)