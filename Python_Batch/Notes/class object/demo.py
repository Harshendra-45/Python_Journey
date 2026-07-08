class Bank_Balance:
    def __init__(self,bal):
        self.__bal = bal
    def deposit(self,bal):
        print("Deposit Successful")
        self.__bal = self.__bal+bal
    def withdraw(self,amt):
        if self.__bal>amt:
            print("withdraw successfull")
            self.__bal=self.__bal-amt
        else:
            print("Not enough Balance")
    def get_bal(self):
        print( self.__bal)
b1 = Bank_Balance(50)
b1.deposit(500)
b1.get_bal()
b1.withdraw(5000)
b1.withdraw(400)
b1.get_bal()