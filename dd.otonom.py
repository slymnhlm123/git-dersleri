film_list={}
print("uygulamamıza hoşgeldiniz")
def film_selected():
   name=input("filmin adını girin\n")
   director=input("filmin yapımcısını giriniz\n")
   year=int(input("filmin yılını giriniz\n"))
   key=len(film_list.items())+1
