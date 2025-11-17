class BankAccount:
    def __init__(self, name:str='John', balance:int=1000):
        self.name = name
        self.balance = balance
        
    def deposit(self, somme):
        self.balance += somme

    def withdraw(self, somme):
        self.balance -= somme

    def display(self):
        print(f'Le compte du titulaire {self.name}, a un solde de : {self.balance}')

titulaire_1 = BankAccount()
titulaire_1.deposit(150)
titulaire_1.display()
titulaire_1.withdraw(50)
titulaire_1.display()