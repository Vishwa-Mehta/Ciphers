ALPHABET = "abcdefghijklmnopqrstuvwxyz"
REVALPHA = "zyxwvutsrqponmlkjihgfedcba"

def encode(text: str) -> str:
    encoded = ""
    for alpha in text:
        if alpha == " ":
            encoded += " "
        else:
            encoded += REVALPHA[ALPHABET.index(alpha)]
    return encoded

def decode(text: str) -> str:
    decoded = ""
    for alpha in text:
        if alpha == " ":
            decoded += " "
        else:
            decoded += ALPHABET[REVALPHA.index(alpha)]
    return decoded

text = input("Enter text: ")
ch = input("Press E to encode or D to decode: ")
if ch == 'e' or ch == 'E':
    print("Encoded Text: " + encode(text.lower()))
elif ch == 'd' or ch == 'D':
    print("Decoded Text: " + decode(text.lower()))
