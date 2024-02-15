import random
import string
from words import SYMBOLS_list

def add(key):
    user = input("What is your account name: ")
    pwd = input("What is the password: ")
    encrypted_user = encode(user, key)
    encrypted_pwd = encode(pwd, key)
    with open('passsword.txt', 'a') as f:
       f.write(encrypted_user + "|" + encrypted_pwd + "\n")
def view():
    with open('passsword.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, pwd = data.split("|")
            decrypted_pwd = str(decode(pwd,key))
            decrypted_user = decode(user, key)
            print("User: ", decrypted_user, ", password: ", decrypted_pwd)
def encode(user, key):
    encoded_text = []
    LENGTH = len(SYMBOLS_list)
    symbols = "".join(SYMBOLS_list)
    for symbol in user:
        index = symbols.find(symbol)
        encode_index = index + key
        while (LENGTH < encode_index ):
            encode_index -= LENGTH
        encoded_symbol = symbols[encode_index]
        encoded_text.append(encoded_symbol)
        encrypted = "".join(encoded_text)
    return encrypted
def decode(user, key):
    symbols = "".join(SYMBOLS_list)
    decoded_text = []
    LENGTH = len(SYMBOLS_list)
    for symbol in user:
        index = symbols.find(symbol)
        decode_index = index - key
        while (LENGTH < abs(decode_index)):
            decode_index += LENGTH
        decoded_symbol = symbols[decode_index]
        decoded_text.append(decoded_symbol)
        encrypted = "".join(decoded_text)
    return encrypted
print("Hello! Welcome to the password manager. \n")
user_pwd = input("What is your master password: ")
user_key = int(input("What is your key: "))
master_user = "Biruk"
master_key = 15
if user_pwd in master_user and user_key == master_key:
    while True:
        mode = input("Would you like to view exsisting passwords or add a new one: (View or add) \n").lower()
        if mode == "view":
            view()
        elif mode == "add":
            add(master_key)
        else:
            print("ERROR! Wrong choice, Try again. /n")
            continue
else:
    print("Wrong choice. \n")
