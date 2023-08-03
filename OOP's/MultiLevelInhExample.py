class GrandParent:
    def a1(self):
        print("GrandParents having 2 Assets")

class Parent(GrandParent): # a1 and a2
    def a2(self):
        print("Parents having 3 Assets")

class Son(Parent): # a1 , a2 and a3

     def  a3(self):
         print("Son Have only 1 Asset")

obj1=Son()
obj1.a1()
obj1.a2()
obj1.a3()

obj2=Parent()
obj2.a1()
obj2.a2()
