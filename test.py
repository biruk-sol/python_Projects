
def encode(text, key):
    SYMBOLS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ,;."
    LENGTH = len(SYMBOLS)
    encoded_text = []
    decoded_text = []
    for symbol in text:
        index = SYMBOLS.find(symbol)
        encode_index = index + key
        while (LENGTH < encode_index ):
            encode_index -= LENGTH
        encoded_symbol = SYMBOLS[encode_index]
        encoded_text.append(encoded_symbol)
        encrypted = "".join(encoded_text)
    return encrypted

def decode(text, key):
    SYMBOLS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ,;."
    LENGTH = len(SYMBOLS)
    decoded_text = []
    for symbol in text:
        index = SYMBOLS.find(symbol)
        decode_index = index - key
        while (LENGTH < abs(decode_index)):
            decode_index += LENGTH
        decoded_symbol = SYMBOLS[decode_index]
        decoded_text.append(decoded_symbol)
        encrypted = "".join(decoded_text)
    return encrypted