""" Class"""
# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self,ism,familiya,tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil

# talaba1 = Talaba("Alijon","Valiyev",2000)

# print(talaba1.ism)



"""                                       """
# class Me:
#     """"""
#     def __init__(self,ism,familiya,tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil


# me1 = Talaba("Mohlaroy","Mahmudova",2009)
# print(me1.ism)
# print(me1.familiya )







""" 09.01.2024 """
# class Car():
#     """ docstring """
#     def __init__(self, company: str, model: str, color: str, price: int, max_speed:int, year:int): # parametr
#         self.company = company
#         self.model = model
#         self.color = color
#         self.price = price
#         self.max_speed = max_speed
#         self.year = year

#     def get_info(self):
#         """  """

#         info = f"Mashina haqidagi malumotlar: \nKampaniya: {self.company} \nModel: {self.model} n\Rangi: {self.color}   \
#             \nNarx: {self.price} $ \nEng yuqori tezligi: {self.max_speed} \nIshlab chiqarilgan yili: {self.year} \n"
#         return info
    

# car1 = Car("Tesla", "Model 3", "black", 30_000, 220, 2022)
# car2 = Car("BMw", "M5", "black", 50_000, 300, 2020)
# car3 = Car("Ferrari", "Z Model", "black", 100_000, 400, 2024)

# print(car1.get_info())
# print(car2.get_info())
# print(car3.get_info())



""" car information"""
# class Car():
#     """ docstring """
#     def __init__(self, company: str, model: str, color: str, price: int, max_speed:int, year:int): # parametr
#         self.company = company
#         self.model = model
#         self.color = color
#         self.price = price
#         self.max_speed = max_speed
#         self.year = year

#     def get_info(self):
#         """  """

#         info = f"Mashina haqidagi malumotlar: \nKampaniya: {self.company} \nModel: {self.model} n\Rangi: {self.color}   \
#             \nNarx: {self.price} $ \nEng yuqori tezligi: {self.max_speed} \nIshlab chiqarilgan yili: {self.year} \n"
#         return info
    

#     def info_get(self):
#         """  """
        
#         return self.company, self.model

    

# car1 = Car("Tesla", "Model 3", "black", 30_000, 220, 2022)
# car2 = Car("BMw", "M5", "black", 50_000, 300, 2020)
# car3 = Car("Ferrari", "Z Model", "black", 100_000, 400, 2024)

# print(car1.get_info())
# print(car2.get_info())
# print(car3.get_info())


# print(car1.info_get())
# print(car2.info_get())



""" 16.01.2025 """

class Student():
    def __init__(self, name:str, surname:str, grade:int, mark:int, friends:list, year:int) -> str:
        self.name = name
        self.surname = surname
        self.grade = grade
        self.mark = mark
        self.friends = friends
        self.year = year


    def get_info(self):
        """  """
        return f"{self.name} {self.surname}, {self.grade} - {self.mark}"
    

    def orta_baho(self):
        """  """
        return sum(self.mark)/len(self.mark)
    
    
    def friends_name(self):
        """  """
        info = f"{self.name}ning dostlari: "
        for friend in self.friends:
            info += f"{friend}, "

        return info
    
    def get_age(self, now=2025):
        """  """
        return now - self.year
    

    def set_grade(self):
        """ Talabaning kursini oshiruvchi funksiya (1-6)"""
        if self.grade < 6:
            self.grade += 1
        else:
            return "Siz hozirda eng so'ngi kursda siz!!"
        
        return self.grade
    

    def get_grade(self):
        """  """
        return self.grade 

# student1 = Student("Mohlaroy", "Mahmudova", 9, [5,5,5,5,5]), ["Oydina","Rahima","Naima"]


# print(student1.get_info())
# print(student1.orta_baho())
# print(student1.set_grade())
# print(student1.set_grade())
# print(student1.set_grade())
# print(student1.set_grade())
# print(student1.set_grade())
# print(student1.set_grade())




""" book class"""
class Book():
    """"""
    def __init__(self, name:str, author:str, year: int, publisher:str, price:int):
        """ """
        self.name = name
        self.author = author
        self.year = year
        self.publisher = publisher
        self.price = price


    def __str__(self):
        return self.name


    def get_info(self):
        return f"Kitobning malumotlari: \nNomi: {self.name} \nAvtor: {self.author} \nYil: {self.year} \nPublisher: {self.publisher} \nNarx: {self.price} $"

    def get_name(self):
        return self.name
        
    def get_price(self):
        return self.price


book1 = Book("nimadir", "kimdir", 2012, "yana kimdir", 50_000)

print(book1)


print(book1.get_info())













""" kutubxona """
class Library():
    """ Kutubxona klassi"""
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.books = []
        self.books_count = 0

    def __str__(self):
        return self.name

    # def __repr__(self):
    #     return self.name


    def get_info(self):   
        """ Kutubxona haqidagi malumotlar"""
        return f"Kutubxona nomi: {self.name}, \nmanzil: {self.address}, \nqoshilgan kitoblar soni: {self.books_count}"


    def add_book(self, book):
        """ Kutubxonaga kitob qoshuvchi funksiya """
        self.books.append(book)
        self.books_count += 1
    
        return self.books


    def get_book(self):
        """ Kutubxonadagi kitoblar nomini qaytaradigan funksiya """
        info = f"{self.address} kutubxonasi, \nmanzil: "
        for book in self.books:
            info += f"{book}, "

        return info


kitob1 = Library("Nodira Begim", "lola")


# print(kitob1.add_book("yasha"))
# print(kitob1.get_book())
# print(kitob1.get_info())

# print(kitob1)



