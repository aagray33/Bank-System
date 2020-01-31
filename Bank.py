class BankAccount:
    def __init__(self,name,balance,rate=None):
        self.n=name
        self.b=balance
        self.r=rate
        
    def __str__(self):
        if self.r == None:
            return self.n+" balance "+str(self.b)
        else:
            return self.n+" balance "+str(self.b)+"; rate "+str(self.r)
    
    def deposit(self,amount,info=False):
        self.b = self.b + amount
        if info==True:
            print(self.n+" deposit requested "+str(amount))
            print("\tNew",self)   
        
    def withdraw(self,amount,info=False):
        #first check if subtracting the wanted withdrawal will make the account go negative
        if self.b-amount < 0 and info==True:
            print(self.n+" withdrawal requested "+str(amount))
            print("\tSorry your withdrawal is limited to "+str(self.b))
            #set the balance to zero if would go negative
            self.b = 0
        elif self.b-amount < 0:
            self.b = 0
        elif self.b-amount > 0 and info==True:
            self.b = self.b - amount
            print(self.n+" withdrawal requested "+str(amount))
            print("\tNew",self)
        else:
            self.b = self.b - amount

    def addcompound(self):
        self.b = self.b*(1+(self.r/12))**(12)
        return self.b

        
def main():
    #create a bank account named Checking with $1000
    acc1=BankAccount("Checking",1000)
    #print info about its balance
    print(acc1)
    #deposit $250
    acc1.deposit(250)
    #deposit again $250 but record the transaction (i.e print some info)
    acc1.deposit(250,True)
    #withdraw $700 and record the transaction
    acc1.withdraw(700,True)
    #try to withdraw $850
    acc1.withdraw(850,True)
    #print new info about its balance
    print(acc1)

if __name__ == "__main__":
    main()
