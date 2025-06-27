import csv
from datetime import datetime
from decimal import Decimal, InvalidOperation
from pathlib import Path


class expenseTracker:
    def __init__(self):
        filePath = "expenses.csv"
        self.expenses = self._readDataFromDisk(filePath)
        self.filePath = filePath
        self.budget = Decimal(0)

    def view(self):
        if(self.expenses):
            print("\ndate, category, amount, description")

        for index, item in enumerate(self.expenses):
            if(self._stringIsNullOfEmpty(item['date']) or
               self._stringIsNullOfEmpty(item['category']) or
               self._stringIsNullOfEmpty(item['amount']) or
               self._stringIsNullOfEmpty(item['description'])):
               print(f"Skipping invalid values found at row: {index}")
               continue
            else:
                print(f"{item['date']}, {item['category']}, {item['amount']}, {item['description']}")

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
           total = total + Decimal(item["amount"])

        print(total)

        if(total>self.budget):
            print(f"You have exceeded the budget by {total - self.budget} amount. \n")
        else:
            print(f"You have {self.budget-total} left in your budget. \n")


        #self.expenses(map(lambda T: T["amount"]))

    def saveExpenses(self):
        self._saveDataToDisk(self.filePath, self.expenses)
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

    def _saveDataToDisk(self, fullfilePath, data):
        with open(fullfilePath,"w",newline="") as file:
            fieldNames = ["date","category","amount","description"]
            writer = csv.DictWriter(file, fieldnames= fieldNames)
            writer.writeheader()
            writer.writerows(data)

    def _readDataFromDisk(self, fullfilePath):
        filePath = Path(fullfilePath)
        if(filePath.exists()):
            print(f"reading {fullfilePath}")
            with open(filePath,"r",newline="") as file:
                reader = csv.DictReader(file)
                return list(reader)
        else:
            print(f"file {fullfilePath} doesn't exist.")
            return list()

    def _stringIsNullOfEmpty(self, data):
        return data is None or str(data).strip() == ""