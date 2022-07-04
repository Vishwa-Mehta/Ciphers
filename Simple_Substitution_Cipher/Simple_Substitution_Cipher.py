import random
import time

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
KEY = random.sample(ALPHABET, 26)

def encode(text: str) -> str:
    encoded = ""
    for ch in text:
        if ch != ' ':
            encoded += KEY[ALPHABET.index(ch)]
        else:
            encoded += ' '
    return encoded

def decode(text: str) -> str:
    decoded = ""
    for ch in text:
        if ch != ' ':
            decoded += ALPHABET[KEY.index(ch)]
        else:
            decoded += ' '
    return decoded

text = input("Enter text: ")
print("Encoded Text: " + encode(text.lower()))
print("Decoding text...")
time.sleep(5)
print("Decoded Text: " + decode(encode(text.lower())))
