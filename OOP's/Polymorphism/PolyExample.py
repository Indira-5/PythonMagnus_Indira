class Car_2022:

    def roof(self):
        print("Sun roof")

    def wheels(self):
        print("Normal Alloy wheels")

    def Music(self):
        print('7" Music System with touch player')

class Car_2023(Car_2022):

     def roof(self):
         #print("Panaromic sun roof")
              super().roof()

     def Music(self):
         print('11" Music System with Touch player')

     def mobileConnect(self):
         print("Benz Blue mobile connect which can manage the car operation from mobile")

obj1=Car_2023()
obj1.roof()
obj1.wheels()
obj1.Music()
obj1.mobileConnect()

