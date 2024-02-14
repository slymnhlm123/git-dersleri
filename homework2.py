üçgen = int(180)

açı1 = float(input('1.İç açıyı giriniz efendim'))
açı2 = float(input('2.İç açıyı giriniz efendim'))
açı3 = float(input('3.İç açıyı giriniz efendim'))

iç_açı_toplamı = float(açı1 + açı2 + açı3 )

if iç_açı_toplamı  == üçgen :
    print('Bu bir Üçgendir efendim.')
else:
    print('Bu Bir Üçgen Değildir efendim.')