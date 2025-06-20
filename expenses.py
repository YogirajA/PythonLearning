from decimal import Decimal,InvalidOperation
from datetime import datetime
class expense:
    def __init__(self):
        self.expenses = list()
    def view(self):
        pass
    def add(self):
        expenseDate = self._getDate()
        expenseCategory = input("Enter category of the expense: ")
        expenseAmount = self._getAmount()
        expenseDescription = input("Enter brief description of the expense: ")
        
        expense = dict(date= expenseDate,category = expenseCategory,  amount= expenseAmount ,  description= expenseDescription)

        self.expenses.append(expense)

        print("added \n")

    def _getDate(self):
        while True:
            try:
                value = input("Enter Date of the expense in the format YYYY-MM-DD: ")
                return datetime.strptime(value, "%Y-%m-%d")
            except ValueError:
                print("Input valid date format")

    def _getAmount(self):
        while True:
            try:
                value = input("Enter amount: ")
                return Decimal(value)
            except InvalidOperation:
                print("Input amount value")       
        
    def setBudget(self):
        pass
    def trackBudget(self):
        pass    
    def saveExpenses(self):
        for item in self.expenses:
            print(item['date'],item['amount'])
        print("saved \n")
       
        
        
def main():
    e = expense()
        
    while True:
        option = showMenu()
        if(option==1):
            e.add()                        
        elif(option==2):
            e.view()
        elif(option==3):
            e.trackBudget()
        elif(option==4):
            e.saveExpenses()
        elif(option==5):
            break

def showMenu():
    option = int(input("Select one of the options from below for the budget tracking: \n" \
    "1. Add Expense\n" \
    "2. View Expenses\n" \
    "3. Track Budget\n" \
    "4. Save Expenses\n" \
    "5. Exit\n"))
    
    return option
    
if __name__ == "__main__":
    main()

