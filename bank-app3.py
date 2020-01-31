from Bank import BankAccount

print("Welcome to App3\n===============\n")
#ask for how much is being borrowed, the rate, and the monthly payment
initial_borrow, rate, monthly_payment = map(float, input("Enter amount to borrow, rate, and monthly payment: ").split())
#create the account
mortgage = BankAccount("Mortgage",initial_borrow)
print(mortgage)
#create amortization file
f1 = open("Amortization.txt","w")
f1.write("Month--Principal paid--Interest paid")
f1.close()

#initialize the counter
counter = 0
principal = 0
interest_paid = 0
mortgage.b = initial_borrow

while mortgage.b > 0:
    amount = monthly_payment - (rate/12) * mortgage.b
    mortgage.withdraw(amount)
    #increase principal paid and interest paid for each month
    principal = principal + amount
    interest_paid = (monthly_payment - amount) + interest_paid
    #increase counter
    counter = counter + 1
    f1 = open("Amortization.txt","a")
    f1.write("\n"+str(counter)+"--"+str(principal)+"--"+str(interest_paid))
    f1.close()
    
#convert the counter (in months) into years
years = float(counter)/12

print("You will be paying your loan after "+str(counter)+" month! (or "+str(years)+" years!)")
print("You borrowed $"+str(initial_borrow)+" but paid $"+str(interest_paid+initial_borrow)+" in total (with interests)")
