import requests
from currency_List import currency_List
def Converter():
    while True:
        from_currency = str(input("Enter the currency you want to convert from: ")).upper()
        to_currency = str(input("Enter the currency you want to convert to: ")).upper()
        if from_currency in currency_List and to_currency in currency_List:
            break
        else:
            print("ERROR! Enter a valid currency: \n")
    amount = int(input("Enter the amount you want to convert: "))


    response = requests.get(
        f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}")

    print(
        f"{amount} {from_currency} is {response.json()['rates'][to_currency]} {to_currency} \n")
    keepConverting()
def keepConverting():
        while True:
            choice = input("Would like to do another conversion? (Y or N) \n")
            choice = choice.capitalize()
            choices = ["Y", "N"]
            if choice in choices:
                break
            else:
                 print("Wrong choice! Try Again. \n")
        if choice == "Y":
            Converter()
        else:
            print("Have a Good day! \n")
Converter()