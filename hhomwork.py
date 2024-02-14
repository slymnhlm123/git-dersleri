anayemek= {"Ana yemekler : \n iskender : 50tl" "\ndöner : 30 tl","\nlahmacun: 15 TL"}
tatlılar=["sütlaç : 10 tl","baklava : 20 tl","künefe : 25 tl"]
salatalar=["havuç salatası : 2 tl","gevrdağı :  15 tl","bol yeşillik :5 tl","mevsim salata : 5tl","çoban salata : 5 tl"]


anayemeks={}
tatlılars={}
salatalars=[]
toplam=[]
while True :
    sipariş=input(" sipariş verecek misiniz evet ise (e) hayır ise (h)\n")

    if sipariş == "h":
        print("birdaha bekleriz efendim")
        break

    if sipariş == "e" :
        print("hangi kategoriden olsun efendim")
        print(anayemek,"\n",salatalar,"\n",tatlılar,"\n")

    katagori_giriniz=input("katagori seçiniz \n")
    if katagori_giriniz == "ana yemek":
        ne=input("hangi yemeği alacaksınız")
        kaç=int(input("ne kadar alacaksan bu üründen"))
    if ne == ("iskender "):
        fiyat=50
        anayemeks.append("iskender")
        toplam += fiyat
        
        
        
    
