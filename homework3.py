max=20

bagajkilosu=float(input("kaç kilo bagaj kullanıyorsunuz efendim"))

ybagaj= round(bagajkilosu,0)

if ybagaj <= 20 :
    print("ek ücret ödemenize gerek yoktur efendim")


else :
    ekücret= ybagaj * 10
    print("ödemeniz gereken ücret",ekücret,"tl")