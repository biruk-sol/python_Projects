def addEmail():
    user = input("\n Enter your name: ")
    email = input("Enter you email: ")
    with open('email_List.txt', 'a') as f:
       f.write( user + "|" + email + "\n")
def viewEmail():
    with open('email_List.txt', 'r') as f:
     for line in f.readlines():
            data = line.rstrip()
            user, email = data.split("|")
            username, domain = email.split("@")
            print("The username for the email under the name: ", user, " is ", username, " and the domain is: ", domain)
while True:
    print("\t Welcome to your email manager \n")
    response = input("What would you like to view exsisting emails or add a new one? (add or view)").lower()
    if response == "add" or response == "view":
        if response == "add":
            addEmail()
        else:
            viewEmail()
        break
    else:
        print("Error! Please enter again. \n")