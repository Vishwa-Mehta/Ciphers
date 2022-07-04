import random
import time

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
ENCRYPTION_LETTERS = random.sample(ALPHABET, 5)
KEY = random.sample(ALPHABET, 25)
MATRIX = []

for i in range(0,25,5):
    MATRIX.append(KEY[i:i+5])

print("Cipher Matrix:")
for i in range(6):
    for j in range(6):
        if i == 0 and j == 0:
            print(' ', end = '')
            print(" ", end='')
            print(" ", end = '')
        elif i == 0:
            print(ENCRYPTION_LETTERS[j-1], end = '')
            print(" ", end='')
        elif j == 0:
            print(ENCRYPTION_LETTERS[i-1] + "|", end = '')
            print(" ", end='')
        else:
            print(MATRIX[i-1][j-1], end = '')
            print(" ", end='')
    print()

def search(ch: chr) -> [int]:
    for i in range(5):
        for j in range(5):
            if MATRIX[i][j] == ch:
                return [i, j]
    return [-1, -1]

def encode(text: str) -> str:
    encoded = ""
    i,j = 0,0
    for ch in text:
        if ch != ' ':
            i,j = search(ch)
            if i == -1 and j == -1:
                encoded += "__"
            else:
                encoded += ENCRYPTION_LETTERS[i]
                encoded += ENCRYPTION_LETTERS[j]
        else:
            encoded += '  '

    return encoded

def decode(text: str) -> str:
    decoded = ""
    i,j = 0,0
    for ch in range(0, len(text), 2):
        if text[ch] != ' ' and text[ch] != '_':
            i = text[ch]
            j = text[ch+1]
            decoded += MATRIX[ENCRYPTION_LETTERS.index(i)][ENCRYPTION_LETTERS.index(j)]
        elif text[ch] == '_':
            for i in ALPHABET:
                if i not in KEY:
                    x = i
            decoded += x
        else:
            decoded += ' '
    return decoded

text = input("Enter text: ")
print("Encoded Text: " + encode(text.lower()))
print("Decoding text...")
time.sleep(5)
print("Decoded Text: " + decode(encode(text.lower())))
