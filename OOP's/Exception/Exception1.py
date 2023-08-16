class Sample:
    def m1(self):
        a=10
        b=0
        try:
         print(a/b)
        except Exception as e:
         print(e)
obj1=Sample()
obj1.m1()
print("End of the program")
