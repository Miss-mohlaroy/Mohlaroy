"""
08/01/2021

Dasturlash asoslari

"SONNI TOPISH" O'YINI

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""
import random

def sontop(x=10):
    tasodifiy_son = random.randint(1,x)
    print(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi?", end="")
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin = int(input(">>>"))
        if taxmin<tasodifiy_son:
            print("Xato. Men o'ylagan son bundan kattaroq. Yana harakat qiling:", end="")
        elif taxmin>tasodifiy_son:
            print("Xato. Men o'ylagan son bundan kichikroq. Yana harakat qiling:", end="")
        else:
            break
        
    print(f"Tabriklayman. {taxminlar} ta taxmin bilan topdingiz!")
    return taxminlar
    

def sontop_pc(x=10):
    input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing. Men topaman.")
    quyi = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = random.randint(quyi,yuqori)
        else:
            taxmin = quyi
        javob = input(f"Siz {taxmin} sonini o'yladingiz: to'g'ri (t),"
                      f"men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)".lower())
        if javob == "-":
            yuqori = taxmin - 1
        elif javob == "+":
            quyi = taxmin + 1
        else:
            break
    print(f"Men {taxminlar} ta taxmin bilan topdim!")
    return taxminlar

def play(x=10):
    yana = True
    while yana:
        taxminlar_user = sontop(x)
        taxminlar_pc = sontop_pc(x)
        
        if taxminlar_user>taxminlar_pc:
            print(f"Men {taxminlar_pc} taxmin bilan topdim va  yutdim!")
        elif taxminlar_user<taxminlar_pc:
            print(f"Siz {taxminlar_user} taxmin bilan topdingiz va yutdingiz!")
        else:
            print("Durrang!")
        yana = int(input("Yana o'ynaymizmi? Ha(1)/Yo'q(0):"))
            
# play()







# """
# 09/01/2021

# Dasturlash asoslari

# "SO'Z TOPISH" O'YINI

# Muallif: Anvar Narzullaev

# Web sahifa: https://python.sariq.dev
# """

# import random
# from uzwords import words

# def get_word():
#     word = random.choice(words)
#     while "-" in word or ' ' in word:
#         word = random.choice(words)    
#     return word.upper()

# def display(user_letters,word):
#     display_letter=""
#     for letter in word:
#         if letter in user_letters:
#             display_letter += letter
#         else:
#             display_letter += "-"
#     return display_letter

# def play():
#     word = get_word()
#     # So'zdagi harflar
#     word_letters = set(word)
#     # Foydalanuvchi kiritgan harflar
#     user_letters = ''
#     print(f"Мен {len(word)} хонали сўз ўйладим. Топа оласизми?")
#     # print(word)
#     while word_letters:
#         print(display(user_letters,word))
#         if user_letters:
#             print(f"Шу вақтгача киритган ҳарфларингиз: {user_letters}")
        
#         letter = input("Ҳарф киритинг: ").upper()
#         if letter in user_letters:
#             print("Бу ҳарфни аввал киритгансиз. Бошқа ҳарф киритинг.")
#             continue        
#         elif letter in word:
#             word_letters.remove(letter)
#             print(f"{letter} ҳарфи тўғри.")
#         else:
#             print("Бундай ҳарф йўқ.")
#         user_letters += letter
#     print(f"Табриклайман! {word} сўзини {len(user_letters)} та уринишда топдингиз.")
  