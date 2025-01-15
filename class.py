# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self,ism,familiya,tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil

# talaba1 = Talaba("Alijon","Valiyev",2000)

# print(talaba1.ism)

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




class Car():
    """ docstring """
    def __init__(self, company: str, model: str, color: str, price: int, max_speed:int, year:int): # parametr
        self.company = company
        self.model = model
        self.color = color
        self.price = price
        self.max_speed = max_speed
        self.year = year

    def get_info(self):
        """  """

        info = f"Mashina haqidagi malumotlar: \nKampaniya: {self.company} \nModel: {self.model} n\Rangi: {self.color}   \
            \nNarx: {self.price} $ \nEng yuqori tezligi: {self.max_speed} \nIshlab chiqarilgan yili: {self.year} \n"
        return info
    

    def info_get(self):
        """  """
        
        return self.company, self.model

    

car1 = Car("Tesla", "Model 3", "black", 30_000, 220, 2022)
car2 = Car("BMw", "M5", "black", 50_000, 300, 2020)
car3 = Car("Ferrari", "Z Model", "black", 100_000, 400, 2024)

# print(car1.get_info())
# print(car2.get_info())
# print(car3.get_info())


print(car1.info_get())
print(car2.info_get())



# git config --global user.name "Your Name"
# git config --global user.email "youremail@domain.com"