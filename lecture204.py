class Phone:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

    def phone_name(self):
        return f"{self.brand} {self.model}"   


    def __repr__(self):
        return f'{self.brand} {self.model} and price is {self.price}' 

    def __str__(self):
        return f'{self.brand} {self.model}'     

    def __add__(self,other):
        return self.price + other.price         

my_phone=Phone('nokia','1100','1000')

def __len__(self):
        return len(self.phone_name())


print(str(my_phone))
print(repr(my_phone))
print(len(my_phone))

class SmartPhone(Phone):
    def __init__(self,brand,model,price,camera):
        super().__init__(brand,model,price)
        self.camera=camera

    def phone_name(self):
        return f"{self.brand} {self.model}  and price is {self.price}"
my_phone=Phone('nokia','1100','1000')
my_smartphone=Phone('samsung','1600','1200')
print(my_smartphone.phone_name())         
print(my_phone.phone_name()) 





