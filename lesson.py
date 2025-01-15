"""1) otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida 3 ta 
    m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida 

2) Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin. 
    Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh

3) Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z(atamani) kiriting 
    (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.

4) Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering.
    Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring

6) Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. Lug'atdagi har bir kalit va 
    qiymatni for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib konsolga chiqaring. 
  """


"""1-mashq +----------------------------------------------------------+"""
# ota =  {
#     "ism" : "Mukhiddin",
#     "yosh" : 39,
#     "viloyat" : "Namangan",
#     "tyil" : "1985.07.07"
# }

# print(f"Otamning ismi {ota['ism']}, yosh {ota['yosh']}, viloyat {ota['viloyat']} , tyil {ota['tyil']}")



# ona =  {
#     "ism" : "Muyassar",
#     "yosh" : 34,
#     "viloyat" : "Namangan",
#     "tyil" : "1989.11.30"
# }

# print(f"Onamning ismi {ona['ism']}, yosh {ona['yosh']}, viloyat {ona['viloyat']} , tyil {ona['tyil']}")


# singlim =  {
#     "ism" : "Oydina",
#     "yosh" : 12,
#     "viloyat" : "Namangan",
#     "tyil" : "2012.03.09"
# }

# print(f"Singlimning ismi {singlim['ism']}, yosh {singlim['yosh']}, viloyat {singlim['viloyat']} , tyil {singlim['tyil']}")




# uka =  {
#     "ism" : "Humoyiddin Mirzo",
#     "yosh" : 9,
#     "viloyat" : "Namangan",
#     "tyil" : "2014.11.14"
# }

# print(f"Ukamning ismi {uka['ism']}, yosh {uka['yosh']}, viloyat {uka['viloyat']} , tyil {uka['tyil']}")



"""2-mashq +-----------------------------------------------------------+"""
# taomlar = {
#     'dad':'manti',
#     'mum':'shashlik',
#     'me':"lagmon",
#     'sis':"chuchvara",
#     'bro':"osh"
#     }

# taom = taomlar['ali']
# print(f"mening sevimli taomi {taom}")



"""3-mashq +-----------------------------------------------------------+"""
# eng_uzb = {
#     "if": "agar",
#     "float":"onlik son",
#     "integer":"butun son",
#     "string":"matn",
#     "else":"aks holda",
# }


# kalit = input("Kalit so'z kiriting: ").lower()
# tarjima = eng_uzb.get(kalit)
# if tarjima==None:
#     print("Bunday so'z mavjud emas")
# else:
#     print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")
    


"""3-mashq +-----------------------------------------------------------+"""
# while True: # abadiy tsikil
#     savol = input("Biror son kiriting(chiqish uchun \"exit\" yoki \"chiqish\"deb yozing): ")
    
#     if savol == "exit" or savol == "chiqish":
#         print("Dastur tugadi")
#         break

#     elif savol.isdigit(): # ma'lumotni son ekanligfini teksahiradi
#         print(f"{savol} ning kvadrati {int(savol)**2} ga teng.") 






""" mashq -----------------------------------------------------------------------------------------> """
# ismlar = ['Mohlaroy', 'Naima', 'Abdul ahad', 'Oydina', 'Xadicha', 'Mubina', 'Rahima', 'Sarvinoz', 'MuhammadYusuf']
# shartlar = ['punishment yozadi' , 'somsa qil', 'otirib turish', 'xona tozala','uyga vazifa qilib ber','musirni tashlab kel' ]
# import random

# print(f"{ismlar[random.randrange(0, len(ismlar))]}----> {shartlar[random.randrange(0, len(shartlar))]}")


# y = "***"
# for y in range(3):
#     print('***')
    


# y = "***"
# for y in range(1):
#     print('***')
#     for y in range(1):
#         print("*")
#         for y in range(1):
#             print("***")
    

# y = "***"
# for y in range(1):
#     print('***')
#     for y in range(1):
#         print("**")
#         for y in range(1):
#             print("*")
#             y = "*"
#             for y in range(1):
#                 print('**')
#                 for y in range(1):
#                     print("***")
        
                
   
# """ mashq"""
# print("* * * *")
# for a in range(1,3):
#     print("*     *")

# print("* * * *")

