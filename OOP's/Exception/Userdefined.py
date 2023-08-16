class EligibleError(Exception):
    pass

class Sample:
    def eligible(self,age,percentage):
        if age<18 or percentage<60:
            raise EligibleError("Not eligible for Registration")
        else:
            print("Registration Success")


obj1=Sample()

try:
    obj1.eligible(18,70)
except EligibleError as e:
    print(e)
