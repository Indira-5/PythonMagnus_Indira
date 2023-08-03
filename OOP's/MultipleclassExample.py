class Father:
    def home(self):
        print("5 Flats and 5 plots with houses")

class  Mother:
   def car(self):
        print("2 Cars")

   def cash(self):
        print("1Million Cash")

class Son(Father,Mother):
     pass

obj1=Son()
obj1.home()
obj1.cash()
obj1.car()
