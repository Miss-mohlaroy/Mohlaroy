"""11.10.24"""
""" 1-mashq
4 dan 873 gacha bo’lgan toq sonli ro’yhat yarating
va ro’yhatdagi har bir sonning ildizini chiqaring.
"""
from math import sqrt
# sonlar = list(range(3,873,2))
# for s in sonlar:
#     print(f"{s}ning ildizi {sqrt(s)}")


""" 2-mashq 
Foydalanuvchidan uning ismini so’rang va unga quida keltirilgan javoblardan mosini qaytaring.
Dasturni tuzishda or operatoridan foydalanig !
Muslima  – Salom Muslima. Davramizda hush ko’rdik.
Zilola/Sevara  – Assalomu aleykum. Zilola/Sevara sizga qanday yordam berishim mumkin?
Anvar/Aziz  – Salom Anvar/Aziz . Bugun Qayerga boramiz ?
"""

# ism_kirit = input("ism kiriting: ")
# if ism_kirit == "Muslima":
#     print(f"Salom {ism_kirit.title()}. Davramizda hush kordik")
# elif ism_kirit == "Zilola" or ism_kirit == "Sevara":
#     print(f"Assalomu aleykum, {ism_kirit.title()} sizga qanday yordam berishim mumkin?")
# elif ism_kirit == "Anvar" or ism_kirit == "Aziz":
#     print(f"Salom {ism_kirit.title} Bugun Qayerga boramiz ?")


""" 3-mashq 
102 dan 2020 gacha bo’lgan sonladan iborat ro’yhat yarating va ro’yhatdagi:
1000 gacha bo’lgan sonning 3-darajasini toping.
1500 dan katta barcha sonlarning o’zidan 4 taga kichik sonni toping.
Ro’yhatdagi 7 ga qoldiqsiz bo’linadigan sonlarning ildizini toping.
"""
# numbers = list(range(102 , 2020))
# # print(numbers)
# for n in numbers:
#     if n < 1000:
#         print(f"{n}ning kubi {n**3}")
#     elif n > 1500:
#         print(f"{n}---> {n-4}")

# for l in numbers:
#     if l%7 == 0:
#         print(f"{l}")



""" 4-mashq
 -322 dan -2 gacha bo’lgan barcha toq sonlarning:
1) 5 chi va 7 chi darajasini toping;
2) Ro’yhatdagi har bir sondan 4 taga kichik sonni konsulga chiqaring;
3) Ro’yhatning uzunligini o’lchang;
4) Ro’yhatdagi har bir sonning ildizini toping;
5) Ro’yhatni avval o’sish tartibida keyin esa kamayish tartibida tartiblab konsulga chiqaring;
"""
num = list(range(3,322,2))
# print(num)
for o in num:
    print(f"{o}ning 5 va 7 darajasi {o**5} {o**7}  ")
    print(f"{o}---> {o-4}")
    print(len(num))
    print(f"{o}ning ildizi ----> {sqrt(o)}")


""" 5-mashq """
# a = float(input("1-sonni kirirting:"))
# b = int(input("2-sonni kirirting:"))
# if a<b:
#     print(f"{a}>{b}")
# elif a<b:
#     print(f"{a}<{b}")
# elif a != b:
#     print(f"{a}={b}")

