import time
import winsound

# Define the Morse code dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', ' ': '/'
}

# Duration of a single dit (in milliseconds)
DIT_DURATION = 100

def play_morse_code(text):
    # Convert text to uppercase
    text = text.upper()

    # Iterate over each character in the text
    for char in text:
        if char in MORSE_CODE_DICT:
            morse_code = MORSE_CODE_DICT[char]
            for symbol in morse_code:
                if symbol == '.':
                    winsound.Beep(440, DIT_DURATION)  # Play a dit
                elif symbol == '-':
                    winsound.Beep(440, 3 * DIT_DURATION)  # Play a dah
                else:
                    time.sleep(3 * DIT_DURATION / 1000)  # Pause for space
        else:
            # If character is not in the dictionary, ignore it
            pass

def text_to_morse(text):
    # Convert text to uppercase
    text = text.upper()

    # Initialize the result string
    result = ""

    # Iterate over each character in the text
    for char in text:
        if char in MORSE_CODE_DICT:
            # Append the Morse code for the character
            result += MORSE_CODE_DICT[char] + " "
        else:
            # If character is not in the dictionary, ignore it
            result += char

    r = result.strip()
    print("\nThe Morse code for the text: ", text, " is: \n ")
    print(r)

text = input("Enter the text below: \n")
text_to_morse(text)
play_morse_code(text)

