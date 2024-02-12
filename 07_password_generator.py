import random
import string

def password_generator():
    while True:
        print("\n \t Welcome to the password generator app. \n \n This app generates a strong password using a combination of letters, digits and special characters.")
        password_len = input("How long should the password be: ")
        if password_len in string.digits:
            password_len = int(password_len)
            password_list = []
            s1 = list(string.ascii_lowercase)
            s2 = list(string.ascii_uppercase)
            s3 = list(string.digits)
            s4 = list(string.punctuation)
            random.shuffle(s1)
            random.shuffle(s2)
            random.shuffle(s3)
            random.shuffle(s4)
            part1 = round(password_len * (30/100))
            part2 = round(password_len * (20/100))
            for x in range(part1):
                password_list.append(s1[x])
                password_list.append(s2[x])
            for x in range(part2):

                password_list.append(s3[x])
                password_list.append(s4[x])
            random.shuffle(password_list)
            generated_Password = "".join(password_list)
            print("\n The password generated is: ", generated_Password, "\n")
            keepGenerating()     
        else:
            print("\n Error! Please only enter a number! \n")
def keepGenerating():
        while True:
            choice = input("Would like to generate a new password? (Y or N) \n")
            choice = choice.capitalize()
            choices = ["Y", "N"]
            if choice in choices:
                break
            else:
                 print("Wrong choice! Try Again. \n")
        if choice == "Y":
            password_generator()
        else:
            print("Have a Good day! \n")
password_generator()

