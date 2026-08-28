class Product:
    def __init__(self,product_id,name,brand,price,stock):
        self.product_id = product_id
        self.name = name
        self.brand = brand
        self.price = price
        self.stock = stock

    def display(self):
            print(f"product_id : {self.product_id}")
            print(f"name       : {self.name}")
            print(f"brand      : {self.brand}")
            print(f"price      : {self.price}")
            print(f"stock     : {self.stock}")
# Create child classes
# Electronics
# Clothing
# Books

     

# Electronics
# Additional properties
# warranty
# model
class Electronics(Product):
    def __init__(self, product_id, name, brand, price, stock,additional_properties,warranty,model):
         super().__init__(product_id, name, brand, price, stock)
         self.additional_properties= additional_properties
         self.warranty= warranty
         self.model= model
    def display(self):
          super().display()
          print(f"additional_properties : {self.additional_properties}")
          print(f"warranty: {self.warranty}")
          print(f"model: {self.model}")
    

# Clothing
# size
# material
class Clothing(Product):
    def __init__(self, product_id, name, brand, price, stock,size,material):
         super().__init__(product_id, name, brand, price, stock)
         self.size = size
         self.material =  material
    def display(self):
            super().display()
            print(f"size : {self.size}")
            print(f"material: {self.material}")


# Books
# author
# publisher
class Books(Product):
    def __init__(self, product_id, name, brand, price, stock,author,publisher):
         super().__init__(product_id, name, brand, price, stock)
         self.author = author
         self.publisher = publisher
    def display(self):
         super().display()
         print(f"author : {self.author}")
         print(f"publisher : {self.publisher}")
