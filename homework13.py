ad=input("adınızı giriniz")
maaş=float(input("maaşınızı giriniz"))
yıl=float(input("kaç yıl çalıştınız"))
zam1= maaş / 100 * 90
zam2= maaş / 100 * 85
zam3= maaş / 100 * 75
if yıl <= 5 :
  print("merhaba sayın",ad,"zamlı maaşınız",zam1,"TL")
elif 5 < yıl < 10:
   print("merhaba sayın",ad,"zamlı maaşınız",zam2,"TL")
elif 10 < yıl :   
   print("merhaba sayın",ad,"zamlı maaşınız",zam3,"TL")