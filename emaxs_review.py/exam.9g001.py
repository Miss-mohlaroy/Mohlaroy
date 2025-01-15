"""13.09.2024"""
"""1-mashq------------------------------------------------------------------------------------------------------------------------------------------->
Bir vaqtni o’zida 4 ta o’zgaruvchi yarating(Bu ishni bir qatorda bajarish zarur !).
Hamda o’zgaruvchilarni konsulga chiqaring.
"""
m,o,h,l,a,r,o,y = "M","o","h","l","a","r","o","y"
print(m,o,h,l,a,r,o,y)

""" 2-mashq ---------------------------------------------------------------------------------------------------------------------------------------->
“Ahmadning “yuvvosh” mushugi meni ko’rsa, doim yugurib keladi.”
"""
print("Ahmadning “yuvvosh” mushugi meni ko’rsa, doim yugurib keladi.")


""" 3-mashq ---------------------------------------------------------------------------------------------------------------------------------------->
93434 ga 94903 ni qoshing, hosil bo’lgan natijadaan 22344 ni ayring
va unga 7363 ni qo’shing
"""

print(93434+94903-22344+7363)


""" 4-mashq----------------------------------------------------------------------------------------------------------------------------------------> 
Ism, yosh, manzil, maktab, sinf deb nomlangan 
o’zgaruvchilar yarating 
va ularni konsulga f”” yordamida chiqaring.
"""

ism = "Mohlaroy"
yosh = 15
maktab = "BM school"
sinf = 9
print(f"ismim {ism.title()}, yoshim {yosh}, {maktab}da va {sinf} sinfda oqiyman")



""" 5-mashq---------------------------------------------------------------------------------------------------------------------------------------->
Name, surname deb nomlangan o’zgaruvchilar yarating
va ularni yangi full_name deb nomlangan o’zgaruvida jamlang.
Hamda full_name deb nomlangan o’zgaruvchining qiymatini ba’zi metodlar
ishlatgan holda barcha hariflarini kichhik qilib konsulga chiqaring.
"""

name = "Mohlaroy"
surname = "Mahmudova"
full_name = [name,surname]
print(name.lower(), surname.lower())


""" 6-mashq -------------------------------------------------------------------------------------------------------------------------------------->
Quidagi o’zgaruvchini   --->    gul = “	   BoyCHeCHak	   ” 
1)	Chap tomonidagi bo’shliqni olib tashlab;
2)	Har ikki tomonidagi bo’shliqni olib tashlab;
3)	Birinchi harifni katta qilib;
4)	Barcha hariflarini katta qilib;
5)	Barcha hariflarini kichik qilib  konsulga chiqaring.
"""
gul = "            BoyCHeCHak            "
print(gul.lstrip())
print(gul.strip())
print(gul.title())
print(gul.upper())
print(gul.lower())


