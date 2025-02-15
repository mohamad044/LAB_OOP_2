class BackAccount:
    def __init__(self,account_holder:str,balance:float=0):
        self.__account_holder = account_holder
        self.__balance = 0
        self.deposit(balance)
        
    def deposit(self,add_amount):
        
        if not isinstance(add_amount, (int, float)):
            raise ValueError("Amount must be a number.")
       
        if add_amount < 0 :
            raise Exception("number must be more than zero")
        self.__balance += add_amount
        return self.__balance
    
    def withdraw(self,amout):
        if  not isinstance(amout, (int,float)):
            raise ValueError("Amount must be a number.")
        if amout > self.__balance:
                raise Exception("you don't have this amount in your account.")
        self.__balance -= amout
        return self.__balance
    
    def get_account_holder(self):
        return self.__account_holder
    def get_balance(self):
        return self.__balance
    
