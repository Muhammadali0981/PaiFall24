

class Account:
    def __init__(self,number:str,balance:float,code:str) :
        self.__account_no = number
        self.__account_bal = balance
        self.__security_code = code
    def printdata(self) :
        print(f"Account number = {self.__account_no}\nAccount balance = {self.__account_bal}\nSecurity Code = {self.__security_code}")

acc = Account("98762355008898",12300.70,'PK0090')
acc.printdata()