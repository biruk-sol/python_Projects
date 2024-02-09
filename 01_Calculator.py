def addition():
        num1 = int(input("Enter the first number: \n"))
        num2 = int(input("Enter the second number: \n"))
        sum_Result = num1 + num2
        print("The sum of ", num1, "and ", num2, "is ", sum_Result, ".\n" )
        while True:
             choice = input("What do you want to do: A.Keep calculating B.leave \n")
             choice = choice.capitalize()
             choices = ["A", "B"] 
             if choice in choice:
                  break
        if choice == "A":
             mainMenu()
        else:
             print("Have a Good day! \n")  
def subtraction():
        num1 = int(input("Enter the first number: \n"))
        num2 = int(input("Enter the second number: \n"))
        difference_Result = num1 - num2
        print("The difference between ", num1, "and ", num2, "is ", difference_Result, ".\n" )
        while True:
             choice = input("What do you want to do: A.Keep calculating B.leave \n")
             choice = choice.capitalize()
             choices = ["A", "B"] 
             if choice in choice:
                  break
        if choice == "A":
             mainMenu()
        else:
             print("Have a Good day! \n")  
def Multiply():
        num1 = int(input("Enter the first number: \n"))
        num2 = int(input("Enter the second number: \n"))
        product = num1 * num2
        print("The product ", num1, "and ", num2, "is ", product, ".\n" )
        while True:
             choice = input("What do you want to do: A.Keep calculating B.leave \n")
             choice = choice.capitalize()
             choices = ["A", "B"] 
             if choice in choice:
                  break
        if choice == "A":
             mainMenu()
        else:
             print("Have a Good day! \n") 
def Division():
        num1 = int(input("Enter the first number: \n"))
        num2 = int(input("Enter the second number: \n"))
        quotient = num1 / num2
        print(num1, "divided by ", num2, "is ", quotient, ".\n" )
        while True:
             choice = input("What do you want to do: A.Keep calculating B.leave \n")
             choice = choice.capitalize()
             choices = ["A", "B"] 
             if choice in choice:
                  break
        if choice == "A":
             mainMenu()
        else:
             print("Have a Good day! \n") 
def mainMenu():
    while True:
        calculate = input("What do you want to do: A.ADD B.SUBTRACT C.DIVIDE D.Multiply \n")
        calculate = calculate.capitalize()
        choice = ["A", "B", "C", "D"]
        if calculate in choice:
            break
        else:
            print("Wrong choice! please try again")
    if calculate == "A":
        addition()
    elif calculate == "B":
         subtraction()
    elif calculate == "C":
         Division()
    else:
         Multiply()
    return calculate
calculate = mainMenu()

                


