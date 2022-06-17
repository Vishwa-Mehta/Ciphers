ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def encode(text: str, n: int) -> str:
    x = n % 26
    rotalpha = ALPHABET[-x:] + ALPHABET[:-x]
    encoded = ""
    for alpha in text:
        if alpha == " ":
            encoded += " "
        else:
            encoded += rotalpha[ALPHABET.index(alpha)]
    return encoded

def decode(text: str, n: int) -> str:
    x = n % 26
    rotalpha = ALPHABET[-x:] + ALPHABET[:-x]
    decoded = ""
    for alpha in text:
        if alpha == " ":
            decoded += " "
        else:
            decoded += ALPHABET[rotalpha.index(alpha)]
    return decoded

text = input("Enter text: ")
n = int(input("Enter the value for rotate: "))
ch = input("Press E to encode or D to decode: ")
if ch == 'e' or ch == 'E':
    print("Encoded Text: " + encode(text.lower(), n))
elif ch == 'd' or ch == 'D':
    print("Decoded Text: " + decode(text.lower(), n))
