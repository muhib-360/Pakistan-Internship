# Task 3 : Expense Tracker

class Expense:
    def __init__(self, amount, date, description, category):
        self.amount = amount
        self.date = date
        self.description = description
        self.category = category

class TrackExpenses:
    def __init__(self):
        self.expenses = []

    def add_expenses(self , amount , date, description , category):
        expenses = Expense(amount , date , description , category)
        self.expenses.append(expenses)
        print("Expenses Saved !")

    def show_expenses(self):
        for expense in self.expenses:
        
            print(f"Amount : {expense.amount} , Category : {expense.category} , Description : {expense.description} , Date : {expense.date}\n")
        

    def show_total_expenses(self):
        total = sum(expense.amount for expense in self.expenses)
        print(f"Total Expense : {total}")

    def expense_by_category(self , category):
        for expense in self.expenses:
            if expense.category == category:
                print(f"Category : {category} , Amount : {expense.amount} , Date : {expense.date} , Description : {expense.description}")
            else:
                print(f"No category named {category} found")
    


    def main_menu(self):
        tracker = TrackExpenses()
        while True:
            print(" | Welcome to Expense Tracker | where you can track your expenses easily.".center(150))

            print("\nExpense Tracker Menu : \n")
            print("1. Add Expenses")
            print("2. Show All Expenses")
            print("3. View Total Expenses")
            print("4. View Expenses by Category")
            print("5. Exit\n")

            choice = input("Choose an option : (1-5) ")

            if choice == '1':
                ask_amount = float(input("Enter the amount : "))
                ask_category = input("Category : ")
                ask_date = input("Date (yy-mm-dd) : ")
                ask_description = input("Description : ")
                self.add_expenses(ask_amount,ask_date , ask_description , ask_category)

            elif choice == '2':
                self.show_expenses()

            elif choice == '3':
                self.show_total_expenses()

            elif choice == '4':
                ask_catg = input("Enter category : ")
                self.expense_by_category(ask_catg)
            elif choice == '5':
                print("Exiting the program..")
                break

testing = TrackExpenses()
testing.main_menu()

