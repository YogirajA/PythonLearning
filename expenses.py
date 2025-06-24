from decimal import Decimal,InvalidOperation
from datetime import datetime
import csv
import io

class expense:
    def __init__(self):
        self.expenses = list()
        self.budget = Decimal(0)

    def view(self):
        for item in self.expenses:
            print(item['date'],item['amount'])

    def add(self):
        expenseDate = self._getDate()
        expenseCategory = input("Enter category of the expense: ")
        expenseAmount = self._getAmount(inputmessage='Enter Expense amount: ')
        expenseDescription = input("Enter brief description of the expense: ")
        
        expense = dict(date= expenseDate,category = expenseCategory,  amount= expenseAmount ,  description= expenseDescription)

        self.expenses.append(expense)

        print("added \n")
        
    def setBudget(self):
        self.budget = self._getAmount(inputmessage="Enter budget amount: ")
    

    def trackBudget(self):
        total = Decimal(0)    
        for item in self.expenses:
           total = total + item["amount"]

        print(total)

        if(total>self.budget):
            print(f"You have exceeded the budget by {total - self.budget} amount. \n")
        else:
            print(f"You have {self.budget-total} left in your budget. \n")


        #self.expenses(map(lambda T: T["amount"]))

    def saveExpenses(self):    
        self._saveDataToDisk(self.expenses)
        print("saved \n")
       
    
    def _getDate(self):
        while True:
            try:
                value = input("Enter Date of the expense in the format YYYY-MM-DD: ")
                return datetime.strptime(value, "%Y-%m-%d")
            except ValueError:
                print("Input valid date format")

    def _getAmount(self, inputmessage='Enter amount: '):
        while True:
            try:
                value = input(inputmessage)
                return Decimal(value)
            except InvalidOperation:
                print("Input amount value")  

    def _saveDataToDisk(self, data):
        with open("expenses.csv","w",newline="") as file:
            fieldNames = ["date","category","amount","description"]
            writer = csv.DictWriter(file, fieldnames= fieldNames)
            writer.writeheader()
            writer.writerows(data)       
        
def main():
    e = expense()
        
    while True:
        option = showMenu()
        if(option==1):
            e.add()                        
        elif(option==2):
            e.view()
        elif(option==3):
            e.setBudget()
        elif(option==4):
            e.trackBudget()
        elif(option==5):
            e.saveExpenses()
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

