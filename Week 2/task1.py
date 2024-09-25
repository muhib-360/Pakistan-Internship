#Task - 1 : List Manipulation
import time

class Main:

    def __init__(self):
        self.num_list = []
        self.display = self.headings()


    def headings(self):
        head = "Welcome to the List Manipulation Program\n\n"
        print(head.center(150))
        time.sleep(0.3)

    def operations_menu(self):
        print("Operations Menu: \n 1) Sorting \n 2)Find Large Number \n3) Find Small Number\n 4) Find Sum\n")

        ask_user = int(input("Which one to perform? (1-4) "))
        while True:
            if ask_user == 1:
                ask_again = input("Descending or Ascending ?  (Des/Asc)" ).lower()
                if (ask_again == "des") or (ask_again == "d"):
                    self.call_descend()
                    break
                elif ask_again == "asc" or ask_again == "a":
                    self.call_ascend()
                    break
            if ask_user == 2:
                self.find_large_num()
                break
            if ask_user == 3:
                self.find_small_num()
                break
            if ask_user == 4:
                self.find_sum()
                break

    def exit_or_not(self):
        ask_user = input("Do you want to exit ?  (Y/N)").lower()
        while True:
            if ask_user == "y" or ask_user == "yes":
                print("Exiting the program....")
                time.sleep(0.3)
                break
            elif ask_user == "n" or ask_user == "no":
                print("Going back to the main screen...")
                time.sleep(0.4)
                break

    def find_large_num(self): #[6,3,1,8]
        zero_number = 0
        for nums in self.num_list:
            while nums > zero_number:
                zero_number = nums
            large_num = max(zero_number , nums)
        print(f"The large number is : {large_num}")
    
    def find_small_num(self):
        high_number = 10**18
        for nums in self.num_list:
            if nums < high_number :
                small = nums
            small_num = min(high_number, small)
        print(f"The smallest number is : {small_num}")


    def find_sum(self):
        zero_number = 0
        for nums in self.num_list:
            sum_of_numbers = nums + zero_number
            zero_number = sum_of_numbers
        print(f"Sum : {sum_of_numbers}")

    
    def call_descend(self):
        list_length = len(self.num_list)
        for length in range(list_length):
            for j in range(0 , list_length-length-1):
                if self.num_list[j] < self.num_list[j+1]:
                    self.num_list[j],self.num_list[j+1] = self.num_list[j+1] , self.num_list[j]
        print(self.num_list)

    def call_ascend(self):
        list_length = len(self.num_list)
        for length in range(list_length):
            for j in range(0 , list_length-length-1):
                if self.num_list[j] > self.num_list[j+1]:
                    self.num_list[j],self.num_list[j+1] = self.num_list[j+1] , self.num_list[j]
        print(self.num_list)


    def take_numbers(self):
        self.take_size = int(input("Enter the list size in digits : "))
        for size in range(self.take_size):
            self.take_num = int(input(f"Enter number {size+1} : "))
            self.num_list.append(self.take_num)
        
        print("Creating list.....")
        time.sleep(0.3)
        print("List Created Successfully !")
        print(self.num_list)



testing = Main()
testing.take_numbers()
if testing.operations_menu():
    testing.exit_or_not()

