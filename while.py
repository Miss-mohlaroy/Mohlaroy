"""while -------------------------------------------------------------------------->"""
# while True: # abadiy tsikil
#     savol = input("Biror son kiriting(chiqish uchun \"exit\" yoki \"chiqish\"deb yozing): ")
    
#     if savol == "exit" or savol == "chiqish":
#         print("Dastur tugadi")
#         break

#     elif savol.isdigit(): # ma'lumotni son ekanligfini teksahiradi
#         print(f"{savol} ning kvadrati {int(savol)**2} ga teng.") 



"""mashq-------------------------------------------------------------------+"""
# parol = "ujtrui"
# while True:
#     savol = input("Biror parol kiriting:")
#     if savol == parol:
#         print("Dastur tugadi")
#         break
#     else:
#         print(f"parol qabul qilindi!!!")


"""2-mashq------------------------------------------------------------------+"""
# while True:
#     savol = input("Biror parol kiriting: ")
#     if len(savol) >= 8:
#         s2 = input("parolni takrorlang: ")
#         if savol == s2:
#             print("dastur tugadi")
#             break
#         else:
#             print("Parol mos kelmadi boshidan urining")
#     else:
#         print("boshidan kiriting: ")



"""----------------------------------------------------------------------------->"""
# kitoblar = []
# while True:
#     kitoblar.append(input("Biror kitob nomini kiriting: "))

#     savol = input("yana kitob qo'shmoqchimisiz(yes/no): ")
#     if savol.lower() == "no":
#         break 
#     elif savol.lower() == "yes":
#         continue

# print(kitoblar)



"""------------------------------------------------------------------------>"""
# talabalar = ["hasan", "husan", "olim", "botir"]
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#     print(f"{talaba.title()} baholandi")
#     baholangan_talabalar[talaba] = int(baho)




""" While ------------------------------------------------------------------------------------------------------------------------------------> """
# ismlar = []
# while True:
#     ismlar.append(input("Ism kiriting: "))
#     s = input("Dastur tugasinmi(ha\yoq): ").lower()
#     if s == "ha":
#         print("Dastur tugadi")
#         break
    

# while True:
#     son = int(input("son kiriting: "))
#     print(f"Siz kiriting {son} ning kvadrati {son**2} ga teng")

#     savol = input("chiqishni hohlaysizmi(ha\yoq): ").lower()
#     if savol == "ha":
#         print("Dastur tugadi")
#         break
#     elif savol == "yoq":
#         continue



""" mashq """
# j_y = 2024
# while True:
#     yosh_sora = int(input("Yosh kiriting: "))
#     print(f"sizni t_yilingiz {j_y-yosh_sora}")

#     savol = input("dastur tugasinmi(exit\quit\ha): ").lower()
#     if savol == "exit" or savol == "quit":
#         print("Dastur tugadi")
#         break
#     elif savol == "ha":
#         continue




""" .isdigit() ------------------------------------------------------>"""
# while True:
#     yil = input("Tu'gilgan yilingizni kiriting(chiqib ketish uchun 'exit' deb kiriting): ")
    
#     if yil.isdigit():
#         print(f"Sizning yoshingiz {2024-int(yil)} da")
        
#     if yil == 'exit':
#         print("Dastur tugadi")
#         break



""" mashq --------------------------------------------------------------------->"""
"""Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 
7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 65 dan kattalarga bepul. Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin va 
chipta narhini chiqarsin. Foydalanuvchi exit yoki quit deb yozganda dastur 
to'xtasin (ikkita shartni ham tekshiring).  
"""


"""mashq"""
# while True:
#     son1 = input("1-sonni kiriting: ").lower()
#     if son1 == "stop":
#         print("Dastur tugadi")
#         break
    
#     son2 = input("2-sonni kiriting: ").lower()
#     if son2 == "stop":
#         print("Dastur tugadi")
#         break

#     if son1.isdigit() and son2.isdigit():
#         son1 = int(son1)
#         son2 = int(son2)

#         if son1 > son2:
#             print(f"{son1} > {son2}")
#         elif son1 < son2:
#             print(f"{son1} < {son2}")
#         else:
#             print(f"{son1} = {son2}")




""" mashq ------------------------------------------------------>"""
while True:
    son = input("Son kiriting: ").lower()

    if son == "chiqish":
        print("dastur tugadi")
        break

    if son.isdigit():
        son = int(son)
        if son%2 == 0:
            print(f"{son} juft")
        else:
            print(f"{son} toq")
    else:
        print("Faqat son yoki 'chiqish' deb kiritishingiz mumkin ")





""" mashq """
# x = 0 
# parol = "qwerty"
# while True:
#     ask = input("Parol kirit: ").lower()
#     x += 1
#     if ask == parol:
#         print("hush kelibsiz")
#         break
#     if x >= 3:
#         while True:
#             print("hato")  

