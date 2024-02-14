import random

print("1.oyuncunun kadrosu")
kl=input("Favori Kalecin\n")
deff=input("Favori Defansın\n")
def2=input("Favori Defansın\n")
slb=input("Favori Solbek\n")
sgb=input("Favori Sağbek\n")
dos=input("Favori Defansif Orta Saha\n")
gö=input("Favori Göbek\n")
Os =input("Favori Ofansif Ortasaha\n")
sla=input("Favori Solaçık\n")
sğa=input("Favori Sağaçık\n")
fv=input("Favori Forvetin\n")
kadro1puan=0
print("FAVORİ KADRO :\n",kl,"\n",deff,"\n",def2,"\n",slb,"\n",sgb,"\n",dos,"\n",gö,"\n",Os,"\n",sla,"\n",sğa,"\n",fv)





print("2. oyuncunun kadrosu")

kl2=input("Favori Kaleci\n")
deff2=input("Favori Defans\n")
def22=input("Favori Defans\n")
slb2=input("Favori Solbek\n")
sgb2=input("Favori Sağbek\n")
dos2=input("Favori Defansif Orta Saha\n")
gö2=input("Favori Göbek\n")
Os2 =input("Favori Ofansif Ortasaha\n")
sla2=input("Favori Solaçık\n")
sğa2=input("Favori Sağaçık\n")
fv2=input("Favori Forvetin\n")
kadro2puan=0
print("FAVORİ KADRO :\n",kl2,"\n",deff2,"\n",def22,"\n",slb2,"\n",sgb2,"\n",dos2,"\n",gö2,"\n",Os2,"\n",sla2,"\n",sğa2,"\n",fv2)


#kaleci
kl1o=int(input("ilk kalecinin ortalamasını girin\n"))
kl2o=int(input("ikinci kalecinin ortalamasını girin\n"))
if kl1o>kl2o:
   kadro1puan+=1
   print("ilk kaleci ikinciden",kl1o-kl2o,"kadar yüksek.ilk kadroya +1 puan eklendı")
elif kl2o>kl1o:
   kadro2puan+=1
   print("ikinci kaleci ilkinden",kl2o-kl1o,"kadar yüksek.ilk kadroya +1 puan eklendı")
else:
   kadro1puan+=1
   kadro2puan+=1
   print("iki kalecide eşit,her kadroya +1 puan eklendi")


#defans1
deffo=int(input("ilk defansin ortalamasını girin\n"))
deff2o=int(input("ikinci defansin ortalamasını girin\n"))
if deffo>deff2o:
   kadro1puan+=1
   print("ilk defans ikinciden",deffo-deff2o,"kadar yüksek.ilk kadroya +1 puan eklendı")
elif deffo<deff2o:
   kadro2puan+=1
   print("ikinci defans ilkinden",deff2o-deffo,"kadar yüksek.ilk kadroya +1 puan eklendı")
else:
   kadro1puan+=1
   kadro2puan+=1
   print("iki defans eşit,her kadroya +1 puan eklendi")


#defans2  
def2o=int(input("ilk defansın ortalamasını girin\n"))
deff22o=int(input("ikinci defansın ortalamasını girin\n"))
if def2o>deff22o:
   kadro1puan+=1
   print("ilk defans ikinciden",def2o-deff22o,"kadar yüksek.ilk kadroya +1 puan eklendı")
elif def2o<deff22o:
   kadro2puan+=1
   print("ikinci defans ilkinden",deff22o-deff2o,"kadar yüksek.ilk kadroya +1 puan eklendı")
else:
   kadro1puan+=1
   kadro2puan+=1
   print("iki defans eşit,her kadroya +1 puan eklendi")




#solbek

solbeko=int(input("ilk solbek ortalamasını girin\n"))
solbek2o=int(input("ikinci solbek ortalamasını girin\n"))
if solbeko>solbek2o:
   kadro1puan+=1
   print("ilk solbek ikinciden",solbeko-solbek2o,"kadar yüksek.ilk kadroya +1 puan eklendı")
elif solbeko<solbek2o:
   kadro2puan+=1
   print("ikinci solbek ilkinden",solbek2o-solbeko,"kadar yüksek.ilk kadroya +1 puan eklendı")
else:
   kadro1puan+=1
   kadro2puan+=1
   print("iki solbek eşit,her kadroya +1 puan eklendi")




   #sağbek

sağbeko=int(input("ilk sağbek ortalamasını girin\n"))
sağbek2o=int(input("ikinci sağbek ortalamasını girin\n"))
if sağbeko>sağbek2o:
   kadro1puan+=1
   print("ilk sağbek ikinciden",sağbeko-sağbek2o,"kadar yüksek.ilk kadroya +1 puan eklendı")
elif solbeko<solbek2o:
   kadro2puan+=1
   print("ikinci sağbek ilkinden",sağbek2o-sağbeko,"kadar yüksek.ilk kadroya +1 puan eklendı")
else:
   kadro1puan+=1
   kadro2puan+=1
   print("iki sağbek eşit,her kadroya +1 puan eklendi")



   #dos

doso=int(input("ilk defansif orta saha ortalamasını girin\n"))
dos2o=int(input("ikinci defansif orta saha ortalamasını girin\n"))
if doso>dos2o:
   kadro1puan+=1
   print("ilk defansif orta saha ikinciden",doso-dos2o,"kadar yüksek.ilk kadroya +1 puan eklendı")
elif doso<dos2o:
   kadro2puan+=1
   print("ikinci defansif orta saha ilkinden",dos2o-doso,"kadar yüksek.ilk kadroya +1 puan eklendı")
else:
   kadro1puan+=1
   kadro2puan+=1
   print("iki defansif orta saha eşit,her kadroya +1 puan eklendi")








 #gö

göo=int(input("ilk göbek ortalamasını girin\n"))
göo2=int(input("ikinci göbek ortalamasını girin\n"))
if göo>göo2:
   kadro1puan+=1
   print("ilk göbek ikinciden",göo-göo2,"kadar yüksek.ilk kadroya +1 puan eklendı")
elif doso<dos2o:
   kadro2puan+=1
   print("ikinci göbek ilkinden",göo2-göo,"kadar yüksek.ilk kadroya +1 puan eklendı")
else:
   kadro1puan+=1
   kadro2puan+=1
   print("iki göbek eşit,her kadroya +1 puan eklendi")




 #os

oso=int(input("ilk ofansif orta saha ortalamasını girin\n"))
oso2=int(input("ikinci ofansif orta saha ortalamasını girin\n"))
if oso>oso2:
   kadro1puan+=1
   print("ilk ofansif orta saha ikinciden",oso-oso2,"kadar yüksek.ilk kadroya +1 puan eklendı")
elif oso<oso2:
   kadro2puan+=1
   print("ikinci ofansif orta saha ilkinden",oso2-oso,"kadar yüksek.ilk kadroya +1 puan eklendı")
else:
   kadro1puan+=1
   kadro2puan+=1
   print("iki ofansif orta saha eşit,her kadroya +1 puan eklendi")











 #sla

slao=int(input("ilk solaçık ortalamasını girin\n"))
slao2=int(input("ikinci solaçık ortalamasını girin\n"))
if slao>slao2:
   kadro1puan+=1
   print("ilk solaçık ikinciden",slao-slao2,"kadar yüksek.ilk kadroya +1 puan eklendı")
elif slao<slao2:
   kadro2puan+=1
   print("ikinci solaçık ilkinden",slao2-slao,"kadar yüksek.ilk kadroya +1 puan eklendı")
else:
   kadro1puan+=1
   kadro2puan+=1
   print("iki solaçık eşit,her kadroya +1 puan eklendi")



#sga

sgao=int(input("ilk sağaçık ortalamasını girin\n"))
sgao2=int(input("ikinci sağaçık ortalamasını girin\n"))
if sgao>sgao2:
   kadro1puan+=1
   print("ilk sağaçık ikinciden",sgao-sgao2,"kadar yüksek.ilk kadroya +1 puan eklendı")
elif slao<slao2:
   kadro2puan+=1
   print("ikinci sağaçık ilkinden",sgao2-sgao,"kadar yüksek.ilk kadroya +1 puan eklendı")
else:
   kadro1puan+=1
   kadro2puan+=1
   print("iki sağaçık eşit,her kadroya +1 puan eklendi")





 #fv

fvo=int(input("ilk forvet ortalamasını girin\n"))
fvo2=int(input("ikinci forvet ortalamasını girin\n"))
if fvo>fvo2:
   kadro1puan+=1
   print("ilk forvet ikinciden",fvo-fvo2,"kadar yüksek.ilk kadroya +1 puan eklendı")
elif slao<slao2:
   kadro2puan+=1
   print("ikinci  forvet ilkinden",fvo2-fvo,"kadar yüksek.ilk kadroya +1 puan eklendı")
else:
   kadro1puan+=1
   kadro2puan+=1
   print("iki forvet eşit,her kadroya +1 puan eklendi")



if kadro1puan>kadro2puan:
   print("kadro 1",kadro1puan-kadro2puan,"fark atıp galip oldu,kazanan kadro 1\n kadro2 yenildi")
elif kadro1puan== kadro2puan:
   print("iki takimin da puanı eşit")
   seçım=input("yazı tura yapılsın mi\n")
   if seçım == "evet":
    yazıtura = random.randint(1,2)
    if yazıtura==1:
      print("kadro 1 yazı turada galip geldi")
    else:
      print("kadro 2 yazı turada galip geldi")
   else:
      print("takimlar eşit,turnuva eşitlikle sonuçlandı")
else:
   print("kadro 2",kadro2puan-kadro1puan,"fark atıp galip oldu,kazanan kadro 2\nkadro1 yenildi")