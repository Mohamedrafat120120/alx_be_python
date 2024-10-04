class BankAccount:
    
    
    def __init__(self,account_balance) -> None:
        self.account_balance=account_balance
        account_balance=0
        
        
    def deposit(self,amount) ->int:
        
        self.account_balance+=amount
    
    
    def withdraw(self,amount) ->int:
        
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            return False
        
        
        
        
        
    def display_balance(self) -> int:    
    
        print(f"Current Balance: $[{self.account_balance}]")
        
            
          