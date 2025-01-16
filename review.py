""" 9B001 --------------------------------------------------------------------------------------->"""
"""1-mashq"""
# ism = "Mohlaroy"
# familiya = "Mahmudova"
# y = 15
# kitoblar = ['wefwef' , 'ewfwef', 'efwef', 'jmfrg']
# kasb = "O'quvchi"
# print(type(ism))
# print(type(familiya))
# print(type(y))
# print(type(familiya))
# print(type(kasb))


"""2-mashq"""
# from math import sqrt
# print(round(sqrt(4364+1233), 2))


"""3-mashq"""
# s1 = int(input("1-sonni kiriting: "))
# s2 = int(input("2-sonni kiriting: "))
# print(s1**2/23)
# print(s2**2/23)


"""4-mashq"""
# son = input("butun son kiriting: ")
# print(float(son))
# print(int(son))


"""5-mashq"""
# k = []
# for s in range(5):
#     k.append(input(f"{s+1}-kiriting: "))
# print(k)


"""6-mashq"""
# s = ['Ali', 'Maruf', 'Bahrom']
# s.insert(0, "WRrfrv")
# s.insert(2, "ftgh")
# s.insert(5, "WRrdfthfrv")
# print(s)

# s[0] = "erth"
# s[3] = 'eqwfef'
# print(s)




""" 9B002 --------------------------------------------------------------------------------> """
"""1-mashq"""
# s1 = int(input("1-sonni kiriting: "))
# s2 = int(input("2-sonni kiriting: "))
# import random
# print(random.randrange(s1,s2))


"""2-mashq"""
# ism = input("Ism kiriting: ")
# k2 = []
# for s2 in range(5):
#     k2.append(input(f"{s2+1}-kiriting: "))
# print(k2)

# k2.pop(0)
# print(k2)
# k2.insert(2, "dfbsbg")
# k2.insert(3, "WErgtfsrg")
# print(k2)


"""3-mashq"""
# fanlar = ["dfvsergr","wefwfewefwef"]
# fanlar.append("Dweff")
# fanlar.insert(0, "wefefzdc")
# print(fanlar)
# fanlar[0] = "erth"
# fanlar[3] = 'eqwfef'
# print(fanlar)
# fanlar.pop(3)
# del fanlar[0]
# fanlar.remove("dfvsergr")
# print(fanlar)
# f = fanlar.copy()
# print(f)
# fanlar.clear()
# print(fanlar)



"""4-mashq"""
# oila = []
# son = int(input("Oila necha kishisiz: "))
# for s in range(son):
#     oila.append(input(f"{s+1}-ism kiriting: "))
# print(oila)



"""5-mashq"""
# m = ['mersedes benz' , 'bmw' , 'audi' , 'porche' , 'rolls royce']
# print(len(m))
# m.sort()
# print(m)
# m.sort(reverse=True)
# print(m)
# m.reverse()
# print(m)




""" 9B004 -----------------------------------------------------------------------------> """
"""1-mashq"""
# n = [45, -96,0,63,1257,-6752.2,42,3,542]
# n.sort()
# n.sort(reverse=True)
# n.reverse()
# print(n)


"""2-mashq"""
# mevalar = ['olma','orik','shaftoli','apelsin','malina','xurmo']
# for m in mevalar:
#     if m == 'olma' or m == 'malina':
#         print(f"{m.upper()}")
#     else:
#         print(f"{m.title()}")


"""3-mashq"""
# books = {
#     'ktiob1':"saefawef",
#     'kitob2':"efwef",
# }

# books.update({'kitob3':'wefwef'})
# books['kitob3'] = "sefwfe"
# print(books)

# books.update({'kitob3':'rgrger'})
# books['kitob3'] = "rgegerg"
# print(books)

# books.popitem()
# print(books)
# books.pop('kitob2')
# print(books)

# books.clear()
# print(books)



"""4-mashq"""
# from math import sqrt
# sonlar = list(range(102,2020))
# print(sonlar)
# for s in range(sonlar):
#     if s > 1000:
#         print(f"{s}ning 3-daraja {s**3}")
#     if s < 1500:
#         print(f"{s} sonidan 4ta kichigi {s-4}")
#     if s%7==0:
#         print(f"{s} ilidzi {sqrt(s)}")



"""5-mashq"""
# foiz = float(input("necha foiz oldingzi: ")) 
# orin = int(input("Nechinchi o'rinni oldingiz: "))
# if 0 < foiz > 100:
#     print("Iltimos to'g'ri son kiriting: ")
# elif 0 < foiz <= 64:
#     print("Imtihondan o'ta olmadi!!! ")
# elif 65 <= foiz < 85:
#     print("Imtihondan o'tdi!!")
# elif 85 <= foiz <= 100:
#     if orin == 1:
#         print("Siz 100% grant yutdingiz <3 ")
#     elif orin == 2:
#         print("Siz 75%$ grant :) ")
#     elif orin == 3:
#         print("Siz 50% grant yutdingiz !!")
#     elif orin == 4:
#         print("Siz 25% grant yutdingiz !")





""" 9B005 -------------------------------------------------------------->"""
"""1-mashq"""
# eng_uzb = {
# 	'apple':"olma",
# 	'pen':'ruchka',
# 	"rule":"qoida"
# }

# word = input("So'z kiriting: ")
# for k, v in eng_uzb.items():
# 	if word == k:
# 		print(f"{k}--->{v}")
# 	elif word == v:
# 		print(f"{v}--->{k}") 

# if word not in eng_uzb.keys() and word not in eng_uzb.values():
# 	print("Bunday soz yoq")



"""2-mashq"""
# r_menu = {
#     'lagmon':20000,
#     'osh':25000,
#     'somsa':15000,
#     'salad':4000,
#     'non':5000,
#     'manti':30000,
#     'mastava':18000,
#     'shorva':15000
# }
# print("Bizning menuda: ",end=" ")
# for k in r_menu.keys():
#     print(f"{k}",end=", ")
    
# print("\nNarhlari")
# for k, v in r_menu.items():
#     print(f"{k.title()} ----> {v}")


"""3-mashq"""
# ism = input("Ism kiriting: ")
# yosh = int(input("yoshingizni kirting: "))
# if 1 <= yosh <= 6:
#     print("Siz bog'cha yoshidasiz")
# elif 7 <= yosh <= 17:
#     print("Maktab o'quvchisi uchun")
# elif 18 <= yosh <=30:
#     print("Siz universitet talabasisiz")
# elif 31 <= yosh <= 100:
#     print("Siz maktab o'quvchisi emassiz") 
# elif yosh <= 0 or yosh >100:
#     print("Noto'g'ri son kiritdingiz")



""" 9G005 --------------------------------------------------------------------------------------------------------------------------------------------> """
"""1-mashq"""
# b, m, l, f, = 'edf','efwe','ded','5rdt'
# print(b)
# print(m)
# print(l)
# print(f)


"""2-mashq"""
# print("Ahmadning 'yuvvosh' mushugi meni ko'rsa, doim yugurib keladi")

"""3-mashq"""
# print(93434+94903-22344+7363)


"""4-mashq"""
# ism = "Mohlaroy"
# familiya = "Mahmudova"
# manzil = "Oromgoh"
# mk = "Boborahim mashrab"
# sinf = "9 green"

# print(f"Mening ismim {ism.title()} va familiyam {familiya.title()}, mazil {manzil}, maktab {mk.title()}, sinfim {sinf}")


"""5-mashq"""
# name = "Mohlaroy"
# surname = "Mahmudova"
# # f_n = name, surname
# print(f_n.title())



"""6-mashq"""
# gul = "                      Boychechak                               "
# print(gul.lstrip())
# print(gul.strip())
# print(gul.title())
# print(gul.upper())
# print(gul.lower())







""" 9G002 --------------------------------------------------------------------------------------------------------------------------------------------> """
"""1-mashq"""
# s1 = int(input("1-soni kiriting: "))
# s2 = int(input("2-soni kiriting: "))
# print(s1+s2)
# print(s1-s2)
# print(s1*s2)
# print(s1/s2)
# print((s1+s2)/2)
# print(s1**2)
# print(s1**3)
# print(s2**2)
# print(s2**3)


"""2-mashq"""
# yosh2 = int(input("Yosh kiriting: "))
# tyil = 2024 - yosh2
# print(tyil)


