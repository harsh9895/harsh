# class Book:
#     def __init__(self, name, pages, size, price):
#         self. name = name
#         self. pages = pages
#         self. price = price
#         self. size = size 

#     def getprice(self):
#         if hasattr(self,"discount"):
#             return self.prices - (self.prices* self.discount)
#         else:
#             return self.price
     
#     def setdiscount(self, amount):
#        self.discount = amount

#     def setdiscount (self,amount):
#        self.discount = amount
    
#     def __str__(self):
          
#           price = str (self.price)
#           return f"our book for dale: {self.title} is now on discount {price}"
       

# book1 = Book("harry porter","j.k. rowling", 223, 22.50)

# print(book1)

class cat:
    name: None
    age: None
    __isHappy : None

    #constructor
    def __init__(self, name, age, isHappy = True ):
        self.name = name
        self.age = age
        self. __isHappy = isHappy

def sound(self):
    print("meow")
    def display(self):
        print("****cat****")
        print("name:",self.name)
        print("age:", self.age)
        print("happy:" self.__isHappy)
         
         #getter
        def get_isHappy(self):
            return self._isHappy
        
        #setter
        def set_isHappy(self,new_happy):
            self._isHappy = new_happy

            #CHILD CLASS
            class domesticat(cat):
                owner: None

                def __init__(self, owner , name , age , ishappy= true):
                    super().__init__(name,age, isHappy)
                    self.owner = owner

                    class wildcat(cat):
                        def sound(self):
                            print("hiss")

                            cat1 = ("mao mao", 3)
                            print(cat.sound())
cat1 = cat("mao mao", 3)
print(cat.sound())

cat2 = domesticcat("mikhir","catty"2)
print(cat2.owner)
