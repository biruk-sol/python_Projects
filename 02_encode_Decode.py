SYMBOLS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ,;."
LENGTH = len(SYMBOLS)
encoded_text = []
decoded_text = []
def encode():
    text = input("Enter the text to be encoded: ")
    key = int(input("Enter the Key: "))
    for symbol in text:
        index = SYMBOLS.find(symbol)
        encode_index = index + key
        while (LENGTH < encode_index ):
            encode_index -= LENGTH
        encoded_symbol = SYMBOLS[encode_index]
        encoded_text.append(encoded_symbol)
        encrypted = "".join(encoded_text)
    return encrypted
def decode():
    text = input("Enter the text to be encoded: ")
    key = int(input("Enter the Key: "))
    for symbol in text:
        index = SYMBOLS.find(symbol)
        decode_index = index - key
        while (LENGTH < abs(decode_index)):
            decode_index += LENGTH
        decoded_symbol = SYMBOLS[decode_index]
        decoded_text.append(decoded_symbol)
        encrypted = "".join(decoded_text)
    return encrypted


while True:
    action = input("What do you want to do: \n \t A.encode B.decode \n")
    action = action.capitalize()
    choices = ["A", "B"]
    if action in choices:
        break
    else:
        print("Error! Please try again. \n")
if action == "A":
   encoded_text = encode()
   print("The encoded message is: ", encoded_text)
else:
    decoded_text = decode()
    print("The encoded message is: ", decoded_text) 