ALPHABET = "abcdefghijklmnopqrstuvwxyz"
KEYS = ['{:0{}b}'.format(i, 5) for i in range(1, len(ALPHABET)+1)]

def encode(text: str, sentence: str) -> str:
    encoded_digi = ""
    encoded_text = ""
    for char in text:
        encoded_digi += KEYS[ALPHABET.index(char)]

    count = 0
    new_sentence = ""
    for char in sentence:
        if char.isalpha():
            count += 1
            new_sentence += char

    if count < len(encoded_digi):
        return "ERROR: Sentence length not enough to encode!!! :("

    i = 0
    new_text = ""
    while i < len(encoded_digi):
        if int(encoded_digi[i]) == 1:
            new_text += new_sentence[i].upper()
        else:
            new_text += new_sentence[i]
        i += 1
    if len(new_sentence) > len(new_text):
        new_text += new_sentence[len(new_text):]

    i = 0
    j = 0
    while i < len(sentence):
        if sentence[i].isalpha() != True:
            encoded_text += sentence[i]
        else:
            encoded_text += new_text[j]
            j += 1
        i += 1
    return encoded_text

def decode(text: str) -> str:
    bin_str = ""
    decoded_text = ""
    new_text = ""
    for char in text:
        if char.isalpha():
            new_text += char

    bin_str = ""
    for char in new_text:
        if char.isupper():
            bin_str += '1'
        else:
            bin_str += '0'

    int_list = []
    for i in range(0, len(bin_str), 5):
        int_list.append(int(bin_str[i:i+5], 2))
    
    for i in int_list:
        if i - 1 > 0:
            decoded_text += ALPHABET[i - 1]

    return decoded_text

text = input("Enter text to encode/decode: ")
ch = input("Press E to encode or D to decode: ")
if ch == 'e' or ch == 'E':
    sentence = input("Enter sentence to encode in: ")
    print("Encoded Text: " + encode(text.lower(), sentence.lower()))
elif ch == 'd' or ch == 'D':
    print("Decoded Text: " + decode(text))
