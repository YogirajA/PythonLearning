
from expenseTracker import expenseTracker

def main():
    tracker = expenseTracker()
        
    while True:
        option = showMenu()
        if(option==1):
            tracker.add()                        
        elif(option==2):
            tracker.view()
        elif(option==3):
            tracker.setBudget()
        elif(option==4):
            tracker.trackBudget()
        elif(option==5):
            tracker.saveExpenses()
        elif(option==6):
            break
        else:
            break

def showMenu():
    option = int(input("\nSelect one of the options from below for the budget tracking: \n \n" \
    "1. Add Expense\n" \
    "2. View Expenses\n" \
    "3. Set Budget\n" \
    "4. Track Budget\n" \
    "5. Save Expenses\n" \
    "6. Exit\n"))
    
    return option
    
if __name__ == "__main__":
    main()

