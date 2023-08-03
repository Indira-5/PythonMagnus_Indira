class Teacher:
    def Maths(self):
          print("Maths Teacher teaches Numbers etc")

class Student1(Teacher):
    pass
class Student2(Teacher):
    pass
obj1=Student1()
obj2=Student2()
obj1.Maths()
obj2.Maths()
