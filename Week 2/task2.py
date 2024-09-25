#Task - 2 : Dictionary Based Contact Book
import time
class Main:
    def __init__(self):
        self.call_heads()
        self.contact_book = {}
        self.call_menu()


    def call_menu(self):

        while True:
            print("1)Add New Contacts\n2)Delete Contacts\n3)View Contacts\n ")
            ask_user = int(input("Select the operations (1-3) :  "))

            if ask_user == 1:
                self.add_contacts()
                continue
            if ask_user == 2:
                self.delete_contacts()
            if ask_user == 3:
                self.view_contacts()


    def call_heads(self):
        head = ("Welcome to Contact Book | Where you can save and retrieve your numbers.")
        print(head.center(150))
        credits = ("Program made by Muhib with 💖\n")
        print(credits.center(250))


    def add_contacts(self):
        while True:
            ask_name = input("Enter the name : ")
            ask_number = input("Enter the number : ")

            if ask_name == "" or ask_number == "":
                print("No entry found !")
                continue
            self.contact_book[ask_name] = ask_number

            ask_again = input("Do you want to add more ? (Y/N) ").lower()
            if ask_again == "y" or ask_again =="yes" or ask_again =="":
                continue

            elif ask_again == "n" or ask_again == "no":
                print("Closing....\n")
                time.sleep(0.3)
            break
                    
        print(self.contact_book)


    def delete_contacts(self):
        while True:
            ask_name = input("Enter the name : ")
            if ask_name not in self.contact_book.keys():
                print(f"No findings related to name : {ask_name}")
                break
            del self.contact_book[ask_name]
            print(f"Contact {ask_name} deleted successfully !\n")
            print(self.contact_book)

            ask_again = input("Do you want to delete more ? (Y/N) ").lower()
            if ask_again == "y" or ask_again =="yes" or ask_again =="":
                continue
            elif ask_again == "n" or ask_again == "no":
                print("Closing....")
                time.sleep(0.3)
                break


    def view_contacts(self):
        count = 0
        print("Contact List : \n".center(150))
        for name, num in self.contact_book.items():
            print(f" {count+1} :  | {name} : {num} |".center(150))
            count +=1
            

testing = Main()
