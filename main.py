from decimal import *
import pytest
## питання non-data desctipto без сеттер ідуть дані !!
class Getter:
    def __set_name__(self,owner,name):
        self.name = "__" + name
    def __get__(self,instance, owner):
    
        #return instance.__dict__[self.name]
        return getattr(instance,self.name)
    
   # def __set__(self, instance, value):
     # instance.__dict__[self.name] = value
        setattr(instance, self.name,value)

class Sneakers:         
    brand = Getter()
    size = Getter() 
    color = Getter()
    price = Getter()
    quantity = Getter()
    material = Getter()
    numberOfSales = Getter()

    def __init__(self, brand:str, size: float, color: str, price: int|float, quantity: int, material:str, numberOfSales: int):
        self.__validator_brand_name(brand)
        self.__validator_size(size)
        self.__validator_color(color)
        self.__validator_price(price)
        self.__validator_quantity(quantity)
        self.__validator_material(material)
        self.__validator_numberOfSales(numberOfSales)
        self.brand = brand
        self.size = size
        self.color = color
        self.price = price
        self.quantity = quantity
        self.material = material
        self.numberOfSales = numberOfSales

    def __str__(self):
        return f'Brand is: {self.brand},Size is: {self.size} , Color is: {self.color}'
          
         

    @classmethod
    def __validator_brand_name(cls,brand):
        if type(brand) != str:
            raise TypeError('Brand have tp be STRING')
    @classmethod
    def __validator_size(cls,size):
        try:
            size = float(size)
        except:
            raise ValueError("Parse size exeption") 
        
    @classmethod
    def __validator_color(cls,color):
        if type(color) != str:
            raise TypeError('Color have tp be STRING')
        
    @classmethod
    def __validator_price(cls,price):
        try:
            price = Decimal(price)
        except:
            raise ValueError("Parse price exeption")
      
    @classmethod
    def __validator_quantity(cls,quantity):
        if type(quantity) != int:
            raise TypeError('Quantyity have tp be INT')
        
    @classmethod
    def __validator_material(cls,material):
        if type(material) != str:
            raise TypeError('Material have tp be STRING')
        
    @classmethod
    def __validator_numberOfSales(cls,numberOfSales):
        if type(numberOfSales) != int:
            raise TypeError('numberOfSales have tp be INT')





class ShoesStore:

    @classmethod 
    def __validator_sneakers(cls,sneakrs):
        if type(sneakrs) != Sneakers:
                 raise TypeError("Only Sneakers can be added to this shop")
    
    def __init__(self,*args):
         self.__things = []
         for sneakrs in args:
             self.__validator_sneakers(sneakrs)
             self.__things.append(sneakrs)   

    def addSneaker(self,*args):
        for sneakrs in args:
             self.__validator_sneakers(sneakrs) 
             self.__things.append(sneakrs)

    def print_inventory(self):
    
        for item in self.__things:
            print('-' * 130)
            print(f'Brand is: {item.brand}', end=' | ')
            print(f'Size is: {item.size}', end=' | ')
            print(f'Color is: {item.color}', end=' | ')
            print(f'Price is: {item.price}', end=' | ')
            print(f'Quantity: {item.quantity}', end=' | ')
            print(f'Material is: {item.material}')
            print('-' * 130)

    def bubble_sort(self, key, reverse=False):
        n = len(self.inventory)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if not reverse:
                    if getattr(self.inventory[j], key) > getattr(self.inventory[j + 1], key):
                        self.inventory[j], self.inventory[j + 1] = self.inventory[j + 1], self.inventory[j]
                else:
                    if getattr(self.inventory[j], key) < getattr(self.inventory[j + 1], key):
                        self.inventory[j], self.inventory[j + 1] = self.inventory[j + 1], self.inventory[j]

    def sort_by_price(self):
        self.bubble_sort('price')
        return self.inventory

    def sort_by_quantity(self):
        self.bubble_sort('quantity', reverse=True)
        return self.inventory

    def top_selling_sneakers(self, n=5):
        # Assuming numberOfSales is already sorted in descending order
        return self.inventory[:n]
        
    def chose_by_brand(self,s_brand):
        find_sneakr = []
        for senaker in self.__things:
           if senaker.brand == s_brand:
                
                find_sneakr.append(senaker)
        for item in find_sneakr:
            print(item)

 
#realization
if __name__ == '__main__':
    Nike = Sneakers("Nike", 10, "Black", 100, 35, "Leather", 1000)
    Adidas = Sneakers("Adidas", 9, "White", 80, 3, "Mesh", 800)
    Reebok = Sneakers("Reebok", 11, "Red", 120, 9, "Synthetic", 1200)
    Vans = Sneakers("Vans", 9, "Checkerboard", 65, 3, "Canvas", 750)
    New_Balance= Sneakers("New Balance", 10, "Gray", 95, 4, "Mesh", 850)
    Puma = Sneakers("Puma", 8, "Red", 75, 2, "Suede", 750)    
    Puma2 = Sneakers("Puma", 4, "Reed", 755, 2, "Suede", 750)    
    ShoesStorePro = ShoesStore(Nike,Adidas,Reebok,Vans,New_Balance,Puma2,Puma)
    WrongSnekaers = Sneakers('wrong info',10,'red',100,34,True,3245)
    print('Hi Git')
    print(WrongSnekaers.__dict__)
else:
    print("Code is imported")
