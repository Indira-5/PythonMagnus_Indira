
from abc import ABC,abstractmethod
class Accounts:
    def savings(self):
        print("This is my saving account")

class Loans(ABC):
    @abstractmethod
    def Pl(self):
        print("This is the personal loan")
    @abstractmethod
    def hl(self):
          print("This is the housing loan")

obj1=Accounts()
obj1.savings()

class FinalAccount(Loans):
    def  Pl(self):
        print("This is the personal loan")
    def hl(self):
        print("This is the housing loan")

obj2=FinalAccount()
obj2.Pl()
obj2.hl()
