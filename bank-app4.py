#create function to create a new list and removes duplicates
def removeDuplicates():
    #create empty lists
    new_cost_list = []
    new_expense_list = []
    #counter to tell index for cost_list
    counter = 0
    idx = 0
    #counter to tell index for new_cost_list
    counter_2 = 0
    #runs through expense list
    for i in expense_list:
        #create conditional to be added to simplified list or not
        if i not in new_expense_list:
            new_expense_list.append(i)
            new_cost_list.append(cost_list[counter])
        else:
            idx = new_expense_list.index(i)
            new_cost_list[idx]=new_cost_list[idx]+cost_list[counter]
        counter = counter + 1
    for i in new_expense_list:
        f2.write(i+"--"+str(new_cost_list[counter_2])+"\n")
        counter_2 = counter_2 + 1
    f2.write("Total--"+str(sum(new_cost_list)))
        
    
print("Welcome to App4\n===============\n")
print("Ok I load your expenses from expense.txt")
f1 = open("expenses.txt","r")
f2 = open("budget.txt","w")

#read the lines from expenses.txt
lines = f1.readlines()
#create two empty lists, one for expenses and the other for costs
expense_list = []
cost_list = []

#now add to the empty lists
for item in lines:
    expense,cost=item.split()
    expense_list.append(expense)
    cost_list.append(cost)
    
#make cost_list into float for summing
cost_list = list(map(float,cost_list))

removeDuplicates()
f1.close()
f2.close()
print("I have created the budget file budget.txt")

    
    
    
