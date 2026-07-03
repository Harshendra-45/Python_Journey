import random
class BankAccount:
    bank_name = "Abc Bank"
    rate_interest = 7.5
    def __init__(self,acc,name,bal):
        self.acc_no = acc
        self.name = name
        self.bal = bal
    def deposit(self,amt):
        self.bal = self.bal + amt
        print("Deposit successful")
        print("Updated balance",self.bal)
    def withdraw(self,amt):
        if amt<=self.bal:
            self.bal-=amt
            print("Withdrwal successful")
            print("Updated balance",self.bal)
        else:
            print("Not enough money in account")
    def transfer_money(self,r,amt):
        if amt<=self.bal:
            self.bal-=amt
            r.bal+=amt
            print("Withdrwal successful")
            print("Updated balance",self.bal)
        else:
            print("Not enough money in account")
    def display_bal(self):
        print(f"Account No : {self.acc_no}")
        print(f"Name       : {self.name}")
        print(f"Balance    : ₹{self.bal}")
    @classmethod
    def change_interest_rate(cls,new_rate):
        cls.rate_interest=new_rate
    @classmethod
    def change_bank_name(cls,new_name):
        cls.bank_name=new_name
    @classmethod
    def display_bank_info(cls):
        print(f"Bank Name      : {cls.bank_name}")
        print(f"Interest Rate  : {cls.rate_interest:.2f}%")
    
    @staticmethod
    def validate_account_number(acc_no):
        ac = str(acc_no)
        if len(ac)==4 and ac.isdigit():
            print("Valid")
        else:
            print("Invalid")
    @staticmethod
    def calculate_interest(amt,rate):
        print((amt * rate) / 100)
    @staticmethod
    def gen_trn_id():
        print(f"Transaction ID: TXN{random.randint(4000,9000)}")

b1 = BankAccount(1001,"Deepika",50000)
b1.withdraw(5000)
b1.deposit(5000)
b1.display_bal()
b2=BankAccount(1002,"virat",5000000000)
b1.transfer_money(b2,5000)
BankAccount.change_bank_name("HDFC Bank")
BankAccount.change_interest_rate(8.990)
BankAccount.display_bank_info()
b1.validate_account_number(1054)
b1.calculate_interest(500,10)
b1.gen_trn_id()