A = 5
B = 7

ALPHABET = list("abcdefghijklmnopqrstuvwxyz")

def encode(text: str) -> str:
    encoded = ""
    for char in text:
        if char != ' ':
            c = ((A * ALPHABET.index(char)) + B) % len(ALPHABET)
            encoded += ALPHABET[c]
        else:
            encoded += ' '
    return encoded

def decode(text: str) -> str:
    decoded = ""
    for char in text:
        if char != ' ':
            p = (pow(A, -1, len(ALPHABET)) * (ALPHABET.index(char) - B)) % len(ALPHABET)
            decoded += ALPHABET[p]
        else:
            decoded += ' '
    return decoded

text = input("Enter text: ")
ch = input("Press E to encode or D to decode: ")
if ch == 'e' or ch == 'E':
    print("Encoded Text: " + encode(text.lower()))
elif ch == 'd' or ch == 'D':
    print("Decoded Text: " + decode(text.lower()))
