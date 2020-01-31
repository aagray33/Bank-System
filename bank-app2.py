from Bank import BankAccount

print("Welcome to App2\n===============\n")

initial_balance, interest_rate = map(float, input("Enter initial balance and interest rate for saving account: ").split())
#create account
acc1 = BankAccount("Saving",initial_balance,interest_rate)
print(acc1)



print("\nHow many years will it take to triple my balance?")
#initialize account balance and counter
counter = 0
acc1.b=initial_balance
while acc1.b < 3*initial_balance:
    acc1.addcompound()
    counter = counter+1
print("You will triple your initial balance after "+str(counter)+" years!")
print(acc1)

print("\nWould this be better if I keep contributing 5% of my initial amount every year?")
#initialize account balance and counter
counter = 0
acc1.b=initial_balance
while acc1.b < 3*initial_balance:
    acc1.addcompound()
    acc1.deposit(0.05*initial_balance)
    counter = counter+1
print("You will triple your initial balance after "+str(counter)+" years!")
print(acc1)

print("\nWould this be even better if in addition my interest rate grows up by 0.5% every year?")
#initialize account balance and counter
counter = 0
acc1.b=initial_balance
while acc1.b < 3*initial_balance:
    acc1.addcompound()
    acc1.deposit(0.05*initial_balance)
    acc1.r=acc1.r*1.005
    counter = counter+1
print("You will triple your initial balance after "+str(counter)+" years!")
print(acc1)
