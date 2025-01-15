"""Kod: 9G009
9 Green sinfi uchun haftalik(15-11-24) imtihon savollari
1-mashq | 10 Ball
10 dan 200 gacha bo’lgan sonladan iborat ro’yhat yarating va ro’yhatdagi:
•	100 gacha bo’lgan sonning 3-darajasini toping.
•	150 dan katta barcha sonlarning ildizni toping.
•	Ro’yhatdagi 5 ga qoldiqsiz bo’linadigan sonlarning ildizini toping.
2-mashq | 10 Ball
Usernames deb nomlangan ro’yhat yarating unda o’zingiz bilgan 3, 4 ta ism bo’lsin. Keyin esa 
foydalanuvchidan uning ismini ham so’rang agar uning ismi sizning ro’yhatingizda bo’lsa, 
“Kechirasiz sizning ismingiz mening ro’yhatimda bor ekan” degan habarni agar ro’yhatda bo’lmasa 
“Guruhga hush kelibsiz” degan habarni konsulga chiqaring.
3-mashq | 10 Ball
Foydalanuvchidan 2 ta son kiritishini so'rab, ulardan qay biri katta, kichik yoki tengligini topib beruvchi dastur tuzing.
 Dastur faqat  “stop” so’zi kiritilganda to’xtasin.
4-mashq | 10 Ball
Foydalanuvchidan tug’ilgan yilini so’rab u necha yosh ekanligini topib beruvchi dastur tuzing. 
Dastur faqat “exit” yoki “quit” so’zlari kiritilganda to’xtasin.
5-mashq | 10 Ball
Foydalanuvchidan son olib, son juft yoki toqligini topuvchi dastur tuzing.
Dastur faqat  “chiqish” so’zi kiritilganda to’xtasin.
"""

""" 1-mashq """
# from math import sqrt
# sonlar = list(range(10,200))
# for s in sonlar:
#     if s > 100:
#         print(f"{s}ning kubi {s**3}")
#     if s < 150:
#         print(f"{s} ning ildizi {sqrt(s)}")
#     if s%5 == 0:
#         print(sqrt(s))






""" 2-mashq """
# while True:
#     s1=input("1-soni kiriting: ")
#     if s1 == "stop":
#         print("Dastur tugadi")
#         break
#     s2=input("2-soni kiriting: ")
#     if s2 == "stop":
#         print("Dastur tugadi")
#         break

#     if s1.isdigit() and s2.isdigit():
#         s1 = int(s1)
#         s2 = int(s2)
#         if s1 < s2 :
#             print(f"{s1}<{s2}")
#         elif s1 > s2:
#             print(f"{s1}>{s2}")
#         elif s1 == s2:
#             print(f"{s1}={s2}")



""" 3-mashq """
# while True:
#     tyil = input("tyil kiriting(chiqib betmoqchi bolsangiz (exit/quit)): ")
#     if tyil == "exit" or tyil == "quit":
#         print("dastur tugadi")
#         break
    
#     if tyil.isdigit():
#         tyil = int(tyil)
#         print(f"Mening yoshim {2024-tyil}")


""" 4-mashq """
# while True:
    # s1=input("1-soni kiriting: ")
    # if s1 == "stop":
    #     print("Dastur tugadi")
    #     break


    # if s1.isdigit():
    #     s1 = int(s1)
    #     if s1%2== 0:
    #         print(f"{s1} juft")
    #     elif s1%2==1:
    #         print(f"{s1} toq")





""" 06.01.24 """
""" 1-mashq  """
# from math import sqrt
# sonlar = list(range(1,500))
# for s in sonlar:
#     if s < 200:
#         print(f"{s}ning kvadrati {s**2}")
#     if s > 300:
#         print(f"{s}ning {sqrt(s)}")


""" 2-mashq """
# friends = []
# while True:
#     ism = input("Ism kiriting(chqsh uchun 'stop/quit' bosing): ")
#     if ism == "stop" or ism == "quit":
#         break
#     else:
#         friends.append(ism.title())

# print(friends)



""" 3-mashq """
# def info(ism: str, familiya:str, yosh: int, telefon: int, gmail: str, username: str, manzil: str):
#     person_info = {
#         "ism": ism,
#         "familiya":familiya,
#         "yosh": yosh, 
#         "telefon":telefon,
#         "gmail":gmail,
#         "username":username,
#         "manzil":manzil
#     }
    











