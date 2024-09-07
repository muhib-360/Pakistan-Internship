#Simple Calculator Using Python


head = " | Welcome to Calculator | "
print(head.center(150))


def ask_user():
    num1 = int(input("Enter number 1 : \n"))
    num2 = int(input("Enter number 2 : \n"))

    options = " | Operations ---> add, sub, mul, div |  \n"
    print(options)

    ask_user = input("What operation do you want to perform ?")

    match ask_user:
        case "add" | "+" : 
            result = num1 + num2
            print(f"The result is : {result}")
        case "sub" | "-" : 
            result = num1 - num2
            print(f"The result is : {result}")
        case "mul" | "*" : 
            result = num1 * num2
            print(f"The result is : {result}")
        case "div" | "/" :
            if num2<=0: print(ZeroDivisionError) 
            result = num1 / num2
            print(f"The result is : {result}")
        case default:
            print("Invalid Input ! ")

ask_user()

