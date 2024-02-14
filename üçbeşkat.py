def add_ ():
    toplam=0
    sayıisteme=int(input("Lütfen bir sayı giriniz\n"))
    for katbulma in range(1,sayıisteme):
     if katbulma % 3 == 0 or katbulma % 5 == 0:
        toplam+=katbulma
    print(toplam)

add=add_()
