from Bank import BankAccount


print("Welcome to App1\n===============\n")
salary,initial_cbalance,initial_sbalance = map(float, input("Enter salary and initial balances for Checking and Saving accounts: ").split())
#create accounts
acc1 = BankAccount("Checking",initial_cbalance)
acc2 = BankAccount("Saving",initial_sbalance)

print(acc1)
print(acc2)
print("Month--salary--expense--saving")


def transfer(amount, source, destination):
        source.withdraw(amount)
        destination.deposit(amount)
    
for i in range(12):
    expense = .8*salary
    addsaving = .15*salary
    print(i+1,"--"+str(int(salary))+"--"+str(int(expense))+"--"+str(int(addsaving)), sep='')
    #deposit the money made into checking
    acc1.deposit(salary)
    #withdraw expenses
    acc1.withdraw(expense)
    #transfer saving money from checking into savings
    transfer(addsaving, acc1, acc2)
    salary = salary + salary*.002

print(acc1)
print(acc2)   
