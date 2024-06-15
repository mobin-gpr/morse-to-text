import argparse

# Dictionary containing the mapping of characters to Morse code
MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
                   'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
                   'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
                   'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
                   'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', 
                   '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
                   '8': '---..', '9': '----.', ' ': '/'}

# Function to convert text to Morse code
def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + ' '
    return morse_code

# Function to convert Morse code to text
def morse_to_text(morse_code):
    text = ''
    morse_code = morse_code.split(' ')
    for code in morse_code:
        for key, value in MORSE_CODE_DICT.items():
            if code == value:
                text += key
    return text

# Main function
def main():
    # Parsing command line arguments
    parser = argparse.ArgumentParser(description="Convert text to Morse code and vice versa")
    parser.add_argument("--text", metavar='"TEXT"', help="Text to convert to Morse code")
    parser.add_argument("--morse_code", metavar='"MORSE_CODE"', help="Morse code to decode to text")
    args = parser.parse_args()


    # Checking if text argument is provided
    if args.text:
        morse_code = text_to_morse(args.text)
        print(f"Text '{args.text}' converted to Morse code: {morse_code}")
    # Checking if morse_code argument is provided
    elif args.morse_code:
        decoded_text = morse_to_text(args.morse_code)
        print(f"Morse code '{args.morse_code}' decoded: {decoded_text}")
    else:
        print("Please provide either --text or --morse_code to convert")

# Calling the main function if the script is executed directly
if __name__ == "__main__":
    main()