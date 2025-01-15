"""09.09"""

"""
------> --- grammer
+-----+ --- exercise
------- --- review

"""




"""+---------------------------------------------------------+"""
# talaba_0 = {
#     'ism':'alijon',
#     'familiya':'shamshiyev',
#     'yosh':22,
#     'fakultet':'matematika',
#     'kurs':4
#     }

# # print(talaba_0.items())

# for k, q in talaba_0.items():
#     print(f"kaliq: {k}")
#     print(f"qiymat: {q}") 


"""+--------------------------------------------------------+"""
# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
#     }

# for k, q in telefonlar.items():
#     print(f"{k.title()}ning telefoni ------> {q}")



"""+----------------------------------------------------------+"""
# mahsulotlar = { # Do'kondagi mahsulotlar
#     'olma':10000,
#     'anor':20000,
#     'uzum':40000,
#     'anjir':25000,
#     'shaftoli':30000
#     }

# print(mahsulotlar.keys())

# print("Do'kondagi mahsulotlar !!!")
# for m in mahsulotlar.keys():
#     print(m.title())

# b = ['anor' , 'banan' , 'non' , 'olma']
# for m in mahsulotlar:
#     if m in b:
#         print(f"{m.title()} {mahsulotlar[m]} som ")


"""+----------------------------------------------------+"""
# dad =  {
#     "ism" : "Mukhiddin",
#     "yosh" : 39,
#     "viloyat" : "Namangan",
#     "tyil" : "1985.07.07"
# }

# print(f"Otamning ismi {dad['ism']}, yosh {dad['yosh']}, viloyat {dad['viloyat']} , tyil {dad['tyil']}")



# mum =  {
#     "ism" : "Muyassar",
#     "yosh" : 34,
#     "viloyat" : "Namangan",
#     "tyil" : "1989.11.30"
# }

# print(f"Onamning ismi {mum['ism']}, yosh {mum['yosh']}, viloyat {mum['viloyat']} , tyil {mum['tyil']}")


# sis =  {
#     "ism" : "Oydina",
#     "yosh" : 12,
#     "viloyat" : "Namangan",
#     "tyil" : "2012.03.09"
# }

# print(f"Singlimning ismi {sis['ism']}, yosh {sis['yosh']}, viloyat {sis['viloyat']} , tyil {sis['tyil']}")




# bro =  {
#     "ism" : "Humoyiddin Mirzo",
#     "yosh" : 9,
#     "viloyat" : "Namangan",
#     "tyil" : "2014.11.14"
# }

# print(f"Ukamning ismi {bro['ism']}, yosh {bro['yosh']}, viloyat {bro['viloyat']} , tyil {bro['tyil']}")



# """+-----------------------------------------+"""
# taomlar = {
#     'ali':'manti',
#     'vali':'shashlik',
#     'hasan':"lagmon",
#     'husan':"chuchvara",
#     'olim':"osh"
#     }

# taom = taomlar['ali']
# print(f"Alining sevimli taomi {taom}")



# """+------------------------------------------------+"""
# dic = {
#     'integer':"Butun son",
#     'float':"O'nlik son",
#     'string':"Matn",
#     'list':"Ro'yxat",
#     'tuple':"O'zgarmas ro'yxat"}
# # print(python_izohli_lugati['tuple'])

# kalit = input("Kalit so'z kiriting:").lower()
# print(dic.get(kalit,"Bunday so'z mavjud emas"))

# kalit = input("Kalit so'z kiriting:").lower()
# tarjima = dic.get(kalit)
# if tarjima==None:
#     print("Bunday so'z mavjud emas")
# else:
#     print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")
    


"""16.09.2024"""
""" Qiymat qo'shish ------------------------------------------------------------------------------------------------------------------------------------------->"""
# t = {
#     'hasan':'lagmon',
#     'ali':'manti',
#     'vali':'shashlik',
#     'hasan':"lagmon",
#     'husan':"chuchvara",
#     'olim':"osh"
# }


# t['nodir'] = 'norin'
# t['bobur'] = input("Boburning taomi ? ")
# print(t)

# t.update({"akramjon":"manpar"})
# print(t)


""" Qiymatni o'zgartirish / update() -------------------------------------------------------------------------------------------------------------------------->"""
# t['husan'] = "qozon_kabob"
# print(t)

# t.update({"olim" : "mastava"})
# print(t)


""" Qiymat o'chirich ------------------------------------------------------------------------------------------------------------------------------------------->"""
# del t['olim']
# print(t)

# t.pop("vali")
# print(t)

# t.popitem() # royhatning oxiridagi elementni olib tashlaydi
# print(t)



""" Qiymatni o'zgartirish / update()
# taomlar["hasan"] = 'qozon_kabob'
# print(taomlar)

# taomlar.update({"olin":"manti"})
# print(taomlar)


 Qiymatni o'chirish 
# del taomlar["olim"]
# print(taomlar)

# taomlar.pop("hasan")
# print(taomlar)



 Ro'yhatni tozalash 
# taomlar.clear()
# print(taomlar)

 Ro'yhatdan nusha olish 
# meals = taomlar.copy()
"""



"""----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------->
Thame: Lug'atlar(Dictionary) va Ro'yhatlar(List) bilan ishlash
"""

""" Lug'at ichida lug'at """

# insonlar = {
#     "inson_1" : {
#         "ism":"ALi",
#         "familya":'Valiyev',
#         "t_yil":2000,
#         "kasbi":{
# 			'kasb1':"talaba",
# 			"kasb2":"dasturchi"
# 		}   
#     },
    
#     "inson_2" : {
#         "ism":"Nodir",
#         "familya":"Jo'rayev",
#         "t_yil":"1989",
#         "kasbi":"Haydovchi"    
#     },
    
#     "inson_3" : {
#         "ism":"Hasan",
#         "familya":'Husanov',
#         "t_yil":1991,
#         "kasbi":"shifokor"    
#     }
# }

# print(insonlar['inson_1']['kasbi']['kasb1'])
# print(insonlar['inson_1']['kasbi'])

# print(f"Salom bu inson {insonlar['inson_2']['ism']} \
# {insonlar['inson_2']['familya']} \
# kasbi {insonlar['inson_2']['kasbi']}")


""" Lug'at ichida ro'yhat """

# qizlar = {
#     "anora":['atirgul','lola'],
#     "ezoza":['binafsha','moychechak'],
#     "dilshoda":['nastarin','chinnigul'],
#     "nigina":['kaktus','atirgul']    
# }

# print(qizlar['anora'][0])
# print(qizlar['dilshoda'][1])
# print(qizlar['ezoza'][0])

# for ism, gullar in qizlar.items():
#     print(f"\n{ism.title()} quyidagi gullarni yoqtiradi: ", end=' ')
#     for gul in gullar:
#         print(f"{gul.title()}", end=' ')
    

""" ro'yhat ichida lug'at  """

# talaba_1 = {
#  	'ism':"Jasurbek",
#  	'familya':"Ibrohimov",
#  	'guruh':"4-KB_20",
#  	'fan':"Iqtisod",
# }

# talaba_2 = {
#  	'ism':"Azamhon",
#  	'familya':"Burxonxo'jayev",
#  	'guruh':"4-KB_20",
#  	'fan':" Makroiqtisodiyot",
# }
# talabalar = [talaba_1, talaba_2]

# print(talabalar[0]['fan'])

# for talaba in talabalar:
# 	for key, value in talaba.items():
# 		print(f"{key} - {value}")
    

""" ro'yhat ichida ro'yhat """

# guruh_1 = ['azimjon','ilxomjon','behruzbek']
# guruh_2 = ['anora','umarbek']

# guruhlar = [guruh_1, guruh_2]

# print(guruhlar[0][2])
# print(guruhlar[1][1])



""" -------- Vazifa --------

1)  Ro'yhat ichida  ro'yhat
Telefonlar yoki koputerlar kompanialari va ularnig modellari ni ro'yhat ichiuda ro'yhat 
ko'rinishida jamlab ularni honsolga chiqaring

Misol:
lg = ['X5','Q7','X Power 1']
sumsung = ['S7',"A50"]
telefonlar = [lg, sumsung]
print(.....)

2)
<> lug'at ichida lug'at
Oilalar degan lu'gat yarating uning kalitlarilari o'rnida olila bo'sin, 
va o'sha oila kaliti o'rnida oilanging azosi bo'lsin va uning ichidagi lug'atda  
oila azosining malulotlari chiqib tursin

Misol:

oilalar = {
	'oila1':{
		'ota':{
			'ism':"Alijon",
            'familya':"Mamajonov",
            'yosh':'32',
            'kasb':"Duradgor",
		},
		'ona':{
			'ism':'Munisa',
            'familya':"Mamajonova",
            'yosh':'30',
            'kasb':"Tikuvchi",
		},
	'oila2':{
		...
	}
	}
}

print("For va if larni ishlatib barcha oila va uning zaolari haqida malumotlarni
chiroyli qilib chiqaring ")


3) Lug'at ichida ro'yhat
3 ta ko'chadagi do'stingizdan, 3 ta sinfdoshingizdan va 3 ta kursdagi o'rtog'ingiz 
haqidagi malumotlarni lugatga quyidagi kabi joylang va ichida ro'yhat ochib unga sevimli taomlarini kiritsin

Misol:
dostalar = {
	'sinfdoshlar':{
		'ali':['hotdog','osh','norin'],
        'anvar':['gamburger','lavash','chizburger'],
        'olim':['kabob','somsa','norin']
	},
	"dostlar":{
		'abbos':['qazi','somsa','norin']
	},
	...	
}
For va if larni ishlatib barcha dostlaringiz va ularning taomlari haqidagi malumotlarni
chiroyli qilib chiqaring


4) ro'yhat ichida lug'at

car_1 = {
 	'model':"S3",
 	'brend':"BMW",
 	'year':"2021",
 	'price':"23000",
}

car_2 = {
 	'model':"Nexia-3",
 	'brend':"Chevrolet",
 	'year':"2016",
 	'price':"16000",
}
cars = [car_1, car_2, ...]

"""


"""
Theme: Dictionary(Lug'atlar)
"""

taomlar = {
    'ali':'osh',
    'vali':'shashlik',
    'hasan':'lagmon',
    'husan':'mastava',
    'olim':'somsa',
    'nodir':'kabob'
}


"""taomlar = {'ali':'osh'}
nomi = {'key':'value'}
"""

# print(taomlar)
# print(type(taomlar)) #dictionary --> dict --> lugat

# print(taomlar['ali'])
# print(f"Olimning sevimli taomi {taomlar['olim']}")



# b = {
#     'ism':'Ali',
#     'yosh':23,
#     'student':True,
#     'oila':{'ota','ona','aka'}
# }

# print(b)



"""23.10.2024-------------------------------------------------------------------------------------------------------------------------------------------------------------->"""
# green_9 = {
#     'mahmudova':"Mohlaroy",
#     'botirova':'Hadicha',
#     'malikova':'Naima',
#     'tohirova':'Rahima'
# }

# print(green_9)


"""elemeny qo'shish"""
# green_9.update({'mamadova':'Oydina'})
# print(green_9)

# green_9['madaminova'] = "Oydina"
# print(green_9)

# green_9[input("familiya kiriting: ").lower()] = input('ism kiriting: ')


"""Elementni qiymatini yangilash"""
# green_9.update({'mamadova':'Muslima'})
# print(green_9)

# green_9['malikova'] = 'Sarvinoz'


"""elementni ochirish"""
# del green_9['botirova']
# print(green_9)

# green_9.pop("tohirova")
# print(green_9)

# green_9.popitem()
# print(green_9)



""" Lug'atni o'chirish"""
# del green_9
# print(green_9)


# """ Nusxa olish """
# math_students = green_9.copy()  # 1-usul
# print(math_students)

# math_students_2 = dict(green_9) # 2-usul
# print(math_students_2)



# """ Lug'    tozalash"""
# green_9.clear()
# print(green_9)


# """ .get() - metodi """
# print(green_9.get("Abdulahad", "Bunday ism yoq"))
# print(green_9.get(input("Key kiriting: "), "Bunday ism yoq"))


"""keys(), values(), item() -metodlari----------------------------------------------->"""
# green_9 = {
# 	'mahmudova':"Mohlaroy",
# 	'olimjanova':"Sarvinoz",
# 	"tohirova":"Rahima"
# }

# print(green_9.keys())
# print(green_9.values())

# print(f"9 Green sinfida quidagi o'quvchilar bor: ",end=" ")
# for familiya in green_9.keys():
# 	print(familiya, end=" ")

# print(f"\n9 Green sinfida quidagi o'quvchilar bor:", end=" ")
# for ismlar in green_9.values():
# 	print(ismlar, end=" ")

# #  item() - metodi
# print(green_9.items())
# for key, value in green_9.items():
# 	print(f"{key}-{value}")



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




"""1-mashq"""
# c_c = {
# 	"usa":'Washington',
# 	"korea":"Seoul",
# 	"canada":"Ottowa",
# 	"thailand":"Bangkok",
# 	"russia":"Moskwa"
# }

# for k in sorted(c_c.keys()):
# 	print(k.title())

# for v in sorted(c_c.values()):
# 	print(v.title())


"""2-mashq"""
# davlatlar = {
#     "o'zbekiston":'toshkent',
#     'aqsh':'washington d.c.',
#     'rossiya':'moskva',
#     'tojikiston':'dushanbe',
#     "qirg'iziston":'bishkek',
#     'qozog\'iston':'nursulton',
#     'malayziya':'kuala-lumpur',
#     'singapur':'sungapur',
#     'italiya':'rim'}

# print('Dunyo davlatlari:')
# for davlat in sorted(davlatlar):
#     print(davlat.upper())

# print('\nDavlatlarning poytaxtlari')
# for poytaxt in sorted(davlatlar.values()):
#     print(poytaxt.title())

# country = input('Qaysi davlatning poytaxtini bilishni istaysiz?:').lower()
# capital = davlatlar.get(country)
# if capital==None:
#     print('Kechirasiz, bizda bu haqida ma\'lumot yo\'q')    
# else:
#     print(f"{country.upper()}ning poytaxti {capital.title()} shahri")
    





