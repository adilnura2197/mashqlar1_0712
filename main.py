#1-misol
harorat = int(input("Haroratni kiriting (°C): "))

if harorat > 30:
    print("Juda issiq, uyda qoling!")
elif 20 <= harorat <= 30:
    print("Havo yaxshi, sayr qiling!")
elif 10 <= harorat < 20:
    print("Havo salqin, ko‘ylagi kiying!")
elif harorat < 0:
    print("Juda sovuq, ehtiyot bo‘ling!")


#2-misol
o = input("Ovqat turini kirit: ")

if o == "pizza":
    print("50 ming so'm")
elif o == "burger":
    print("30 ming so'm")
elif o == "salat":
    print("20 ming so'm")
else:
    print("Bizda bunday taom yo'q!")


#3-misol
yosh = int(input("Yosh kirit: "))

if yosh < 18:
    print("Sizga 50% chegirma bor!")
elif 18 <= yosh <= 60:
    print("Chegirma yo'q, to'liq narx: 100 ming so'm")
elif yosh > 60:
    print("Keksalarga 30% chegirma bor!")
