import sys

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def encode_text(text: str) -> str:
    temp_text = list(text)
    temp_encoded = []
    i = 0
    while i < len(temp_text):
        if temp_text[i] != " " and ALPHABET.index(temp_text[i]) + 3 < len(ALPHABET):
            temp_encoded.append(ALPHABET[ALPHABET.index(temp_text[i]) + 3])
        elif temp_text[i] != " " and ALPHABET.index(temp_text[i]) + 3 >= len(ALPHABET):
            temp_encoded.append(ALPHABET[3 - (26 - (ALPHABET.index(temp_text[i])))])
        else:
            temp_encoded.append(" ")
        i += 1
    encoded = "".join(temp_encoded)
    return encoded

def decode_text(text: str) -> str:
    temp_text = list(text)
    temp_decoded = []
    i = 0
    while i < len(temp_text):
        if temp_text[i] != " " and ALPHABET.index(temp_text[i]) - 3 > 0:
            temp_decoded.append(ALPHABET[ALPHABET.index(temp_text[i]) - 3])
        elif temp_text[i] != " " and ALPHABET.index(temp_text[i]) - 3 <= 0:
            temp_decoded.append(ALPHABET[ALPHABET.index(temp_text[i]) - 3])
        else:
            temp_decoded.append(" ")
        i += 1
    decoded = "".join(temp_decoded)
    return decoded

text = input("Enter text: ")
ch = input("Press E to encode or D to decode: ")
if ch == 'e' or ch == 'E':
    print("Encoded Text: " + encode_text(text.lower()))
elif ch == 'd' or ch == 'D':
    print("Decoded Text: " + decode_text(text.lower()))
