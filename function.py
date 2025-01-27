"""2024-02-10"""
"""1-mashq"""
# def yosh_hisobla(t_yil, j_yil=2024):
#     """yoshni hisoblab beradigan dastur"""
#     print(f"siz {j_yil-t_yil} yoshdasiz")

# tyil = int(input("T_yilingizni kiriting: "))
# yosh_hisobla(tyil)


"""2-mashq"""
# def kv_kb(son):
#     """sonning kvadrati va kubini topib beradi"""
#     print(f"{son}ning kvadrati {son**2} va kubi {son**3}")

# s = int(input("son kiriting: "))
# kv_kb(s)



"""3-mashq"""
# def juft_top(son):
#     """sonni juft yoki toqligini topib beradi"""
#     if son%2==0:
#         natija=f"{son} juft son"
#     else:
#         natija=f"{son} toq son"
#     return natija


# n = int(input("son kiriting: "))
# print(juft_top(n))  # Natijani konsolga chiqarish
 



"""4-mashq"""
# def set_p():
#     """"""
#     while True:
#         savol = input("Biror parol kiriting: ")
#         if len(savol) >= 8:
#             s2 = input("parolni takrorlang: ")
#             if savol == s2:
#                 print("dastur tugadi")
#                 break
#             else:
#                 print("Parol mos kelmadi boshidan urining")
#         else:
#             print("boshidan kiriting")

# set_p()


"""5-mashq"""
# def katta_harf(matnlar):
#     for i in range(len(matnlar)):
#         matnlar[i]=matnlar[i].title()

# ismlar = ['ali', 'vali', 'hasan', 'husan']
# katta_harf(ismlar)
# print(ismlar)



"""6-mashq"""
# students = ['ali' , 'vali' , 'husan' , 'hasan']

# def bahola(ismlar):
#     baholar = {}
#     for ism in ismlar:
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#         baholar[ism]=baho
#     return baholar

# baholar = bahola(students)
# print(baholar)




"""7-mashq"""
# def summa():
#     sonlar = []
#     while True:
#         son = input("Son kiritng: ")
#         if son.isdigit():
#             sonlar.append(int(son))
#         elif son.lower() =="exit":
#             break
    
#     kopaytma = 1
#     for son in sonlar:
#         kopaytma = kopaytma * son

#     return kopaytma

# print(summa())


"""8-mashq"""

# def ism_familiya_kirit(name, **surname):
#     """Talabalarning ism va familiyasini chiqarib beradi"""
#     ism_familiya = {}
#     ism_familiya['ism'] = name
#     ism_familiya['familiya'] = surname['surname']
#     return ism_familiya


# student1 = ism_familiya_kirit("Mohlaroy", surname="Mahmudova")
# print(student1)



"""example"""
# def ism_familiya_kirit(name, surname, **kwargs):
#     """Talabalarning ism va familiyasini chiqarib beradi"""
#     kwargs['ism'] = name
#     kwargs['familiya'] = surname
#     return kwargs


# student1 = ism_familiya_kirit("Mohlaroy", "Mahmudova", tyil = 2009,  fan = "IT")
# print(student1)



# import avto_info_mod # avto_info_mod faylini (modulini) chaqiramiz

# avto1 = avto_info_mod.avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# avto_info_mod.info_print(avto1)




"""Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing"""
# def kopaytma(*sonlar):
#     """Sonlarni kopaytmasini topib beruvchi funksiya"""
#     kopaytmasi = 1
#     for son in sonlar:
#         kopaytmasi*=son
#     return kopaytmasi

# print(kopaytma(3,4,5,6,888,))


"""
Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing.
Talabaning ismi va familiyasi majburiy argument,
qolgan ma'lumotlar esa ixtiyoriy ko'rinishda 
istalgancha berilishi mumkin bo'lsin.
"""
# def s_info(ism, familiya, **kwargs):
#     kwargs['ism'] = ism
#     kwargs['familiya'] = familiya
#     return kwargs

# ism = input("Ism kiriting: ")
# familiya = input("Familiya kiriting:")
# fan = input("fan kiriting: ")
# yosh = int(input("yoshingizni kiriting: "))
# print(s_info(ism, familiya, yonalish=fan, t_yil=yosh))



# import random as r # random modulini r deb chaqirayapmiz

# ismlar = ['olim','anvar','hasan','husan']
# ism = r.choice(ismlar) # ismlar dan tasodifiy ism tanlaymiz
# print(ism)
# print(r.choice(ism)) # ismdan tasodifiy harf tanlaymiz





# def yosh_hisobla(ism, t_y):
#     "Foydalanuvchini yoshini hisoblaydigan dastur"
#     print(f"{ism.title()} {2024-t_y} yoshda")

# yosh_hisobla("mohlaroy", 2009)


# def yosh_hisobla(t_yil, j_y=2024):
#     print(f"{j_y-t_yil} yoshdasiz")

# yosh_hisobla(2009,2024)








"""20.11.2024------------------------------------------------------------------------------------------------------> """
# def salom_ber():
#     """Salom beruvchi funkisiya"""
#     print("Assalomu aleykum")

# salom_ber()

# def yosh_top():
#     ism = input("Ism kiriting: ")
#     t_yil = int(input(f"{ism.title()} tug'ilgan yilingizni kiriting: "))
    
#     print(f"{ism.title()} sizning yoshingiz {2024-t_yil}")

# yosh_top()


"""21.11.2024 ------------------------------------------------------------------------------------------------>"""
# def yosh_top(t_yil):
#     """Tug'ilgan yilni qabul qilib olib yoshni hisolaydigan funksiya"""
#     print(f"Sizning yoshingiz {2024-t_yil} da")


# yosh_top(2009)
# yosh_top(2005)


# x = int(input("T yil kirit: "))
# yosh_top(x)





"""25.11.2024------------------------------------------------------------------------------------------------------------------------->"""
# """ Parametrni key_word bilan birga berish """               
# def yosh_top(ism,tyil):
#     print(f"salom {ism.title()}, siz {tyil}-yilda tug'ilgansiz va yoshingiz {2024-tyil} da")      

# yosh_top("mohlaroy" , tyil=2009)  


# """ Standart qiymat """
# def yosh_top(ism, t_yil=2009):
#     print(f"Salom {ism.title()}, siz {t_yil}-yilda tug'ilgansiz va yoshingiz {2024-t_yil}")

# yosh_top("mohlaroy")  



# """ """
# def yosh_top(ism="mohlaroy", t_yil=2009):
#     print(f"Salom {ism.title()}, siz {t_yil}-yilda tug'ilgansiz va yoshingiz {2024-t_yil}da ")

# yosh_top()  











"""mashqlar ---------------------------------------------------------------------------------------------------->"""
"""1-mashq"""
# print(len.__doc__)
# print(max.__doc__)
# print(sum.__doc__)
# print(list.__doc__)



"""2-mashq"""
# def ball_top(ball):
#     """ball topib beruvch funksiya"""
#     if 0 <= ball <= 50:
#         print(f"Siz {ball} ball to'pdingiz va natijangiz qoniqarsiz ")
#     elif 51 <= ball <= 70:
#         print(f"Siz {ball} ball to'pdingiz va natijangiz qoniqarli  ")
#     elif 71 <= ball <= 90:
#         print(f"Siz {ball} ball to'pdingiz va natijangiz yaxshi ")
#     elif 91 <= ball <= 100:
#         print(f"Siz {ball} ball to'pdingiz va natijangiz a'lo ")
#     elif 0 > ball > 100 :
#         print(" ")

# ball_top(78)
# ball_top(34)


"""3-mashq"""
# def s_p_top(e=2, b=6):
#     """tog'ri to'rt burchakni perimetri va yuzini topib beruvchi funksiya"""
#     print(f"tomonlar {e} va {b} bo'lgan tog'ri to'rt burchakning perimetri {(e+b)*2} ga teng yuzi esa {e*b} ")

# s_p_top(4,5)
# s_p_top()


"""4-mashq"""
# sonlar = [44,-2212,-3456543,4565432,343.4323,-3323,-1]
# def tartibla(qiymat):
#     qiymat.sort()
#     print(qiymat)

# tartibla(sonlar)






""" 27-11-2024 -----------------------------------------------------------------------------------------------------------------------------> """
""" Funksiyadan qiymat qaytarish """
# def yosh_top(tyil):
#     """ Tug'ilgan yilni qabul qilib yoshni qaytaradigan funksiya """
#     yosh = 2024-tyil
#     return yosh 

# mohlaroyning_yoshi = yosh_top(2009)
# print(f"Mohlaroyning yoshi {mohlaroyning_yoshi}")


# def yosh_top(tyil, jyil=2024):
#     """ Tug'ilgan yilni qabul qilib yoshni qaytaradigan funksiya """
#     yosh = jyil-tyil
#     return yosh 

# mohlaroyning_yoshi = yosh_top(2009)
# print(f"Mohlaroyning yoshi {mohlaroyning_yoshi}")

"""  -----------------------------------------------------------------------------------------------------------------------------------------------------  """
# def yosh_top(tyil: int, ism: str, oila: list) -> int: # tyil - parametr
# def yosh_top(tyil: int) -> int: 
#     """ Tug'ilgan yilni qabul qilib yoshni qaytaradigan funksiya """
#     yosh = 2024-tyil
#     return yosh 

# mohlaroyning_yoshi = yosh_top(2009)
# print(f"Mohlaroyning yoshi {mohlaroyning_yoshi}")



# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#         baholar[ism]=baho
#     return baholar

# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar)
# print(ba


""" 28-11-2024 ------------------------------------------------------------------------------------------------------------------------------>"""
# def person(name: str, surname: str, age: int, email: str, number: int) -> dict:
#     """ """
#     new_person = {
#         "name":name,
#         "surname": surname,
#         "age":age,
#         "email":email,
#         "number":number
#     }

#     return new_person

# p1 = person("Mohlaroy", "Mahmudova", 15, "bmmmmmsssss09", 8888888)
# p2 = person("Oydina", "Mahmudova", 12, "qwerty", 55555)
# p3 = person("Humoyiddin Mirzo", "Mahmudov", 10, "sdfghjk", 777777)

# print(p1)
# print(p2)
# print(p3)




# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"O'quvchi {ism.title()}ning bahosini kiriting: ")
#         baholar[ism]=baho
#     return baholar

# oquvchilar = ['naima', 'mohlaroy', 'rahima', 'oydina']
# baholar = bahola(oquvchilar)
# print(baholar)





""" 4.12.2024 ----------------------------------------------------------------------------------------------------------------------------------------------------------------> """
# def info(name: str, age: int, grade="9 green") -> str: # sinf="9" -> standard qiymat
#     """    """
#     return f"{name.title()} your age {age}, your class {grade}"

# s1 = info(grade="10 green", age=15, name="Mohlaroy")
# print(s1)



""" mashq """
# def juft(son: int) -> list:
#     """  """
#     return list(range(0, son,2))

# s1 = juft(10)
# print(s1)




""" 5.12.2024 -------------------------------------------------------------------------------------------------------------------->"""
""" *arg """
# def my_sum(*sonlar): 
#     """ """
#     summa = 0
#     for s in sonlar:
#         summa += s
#     return summa 

# print(my_sum(4,56,2243,665,-44444,554,-444,3355))
# print(my_sum(2,5))
# print(my_sum())



""" 10-12-2024 """
# def yosh_top(ism: str, tyil: int, hyil=2024) -> str:
#     """ Foydalanuvchidan ismi va tuilgan yilini sorab yoshini hioblovchi funksiya"""
    
#     return f"{ism.title()}ning yoshi {hyil-tyil}da"


# m = yosh_top("Mohlaroy", 2009, 2009)
# l = yosh_top("lola", 1986, hyil=2021)
# o = yosh_top("oydina", 2006, hyil=2008)

# print(m)
# print(l)
# print(o)



""" 11.12.2024-------------------------------------------------------------------  """
def the_biggest(*numbers):
    """  """
    x = sorted(numbers)
    return x[-1]

# num1 = the_biggest(-44,445345634,5345343,45345345,-435345345,-3453453445353)
# print(num1)



"""-----------------------------------"""
def the_biggest(*numbers):
    """  """
    x = sorted(numbers)
    return x[0]

# num1 = the_biggest(-44,445345634,5345343,45345345,-435345345,-3453453445353)
# print(num1)


""" version 2 """
def the_biggest(*numbers):
    """  """
    maximum = 0
    for number in numbers:
        if number > maximum:
            maximum = number


    return maximum 

# num1 = the_biggest(-44,445345634,5345343,45345345,-435345345,-3453453445353)
# print(num1)



""" len """
def my_len(*numbers):
    x = 0
    for n in numbers:
        x += 1
    
    return x

# num1 = my_len(-44,445345634,5345343,45345345,-435345345,-3453453445353)
# print(num1)



""" 12-12-2024----------------------------------------------------------------------------------- """
""" range """
def my_range(x: int, y: int):
    """ """
    son = [x]
    for s in son: 
        if s < y - 1:
            son.append(s + 1)

    return son

# num1 = my_range(4,10)
# print(num1)



"""my sqrt"""
def my_sqrt(son: int) -> int:
    
    return son ** 0.5


# son = float(input("son kiriting:  "))
# print(f"{son} sonining kvadrat ildizi  ----> {my_sqrt(son)}")

""" unli va undosh """
def unli_undosh_top(harf: str):
    """ kiritilgan harfni unli yoki undoshligini chiqarib beruvchi funksiya"""
    unli = ["a",'u','i','e','o']
    if harf in unli:
        return "bu harf unli"
    else:
        return "bu harf undosh"

# harf = input("harf kiriting: ")
# print(unli_undosh_top(harf))




""" orta arifmetika"""
def orta_arifmetika(*sonlar):
        x = 0
        summa = 0

        for n in sonlar:
            x += 1
            summa += n

        return summa/x

# print(orta_arifmetika(4, 5, 6, 7))


# def ekub(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a

# def ekuk(a, b):
#     return abs(a * b) // ekub(a, b)

# # Misol
# a = 12
# b = 18

# print("EKUB:", ekub(a, b))
# print("EKUK:", ekuk(a, b))

