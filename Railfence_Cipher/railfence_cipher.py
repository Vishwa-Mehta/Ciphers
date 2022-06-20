def encode(text: str, key: int) -> str:
    n = len(text)
    matrix = [['.' for i in range(n)] for j in range(key)]
    j = 0
    flag = 0
    while j < n:
        if flag % 2 == 0:
            i = 0
            while i < key:
                matrix[i][j] = text[j]
                j += 1
                i += 1
        else:
            i = key - 2
            while i > 0:
                matrix[i][j] = text[j]
                j += 1
                i -= 1
        flag += 1

    encoded = ""
    for i in range(key):
        for j in range(n):
            if matrix[i][j] != '.':
                encoded += matrix[i][j]
    return encoded

def decode(text: str, key: int) -> str:
    decoded = ""
    n = len(text)
    matrix = [['.' for i in range(n)] for j in range(key)]
    j = 0
    flag = 0
    while j < n:
        if flag % 2 == 0:
            i = 0
            while i < key:
                matrix[i][j] = '-'
                j += 1
                i += 1
        else:
            i = key - 2
            while i > 0:
                matrix[i][j] = '-'
                j += 1
                i -= 1
        flag += 1
    k = 0
    for i in range(key):
        for j in range(n):
            if matrix[i][j] == '-':
                matrix[i][j] = text[k]
                k += 1
    j = 0
    flag = 0
    while j < n:
        if flag % 2 == 0:
            i = 0
            while i < key:
                decoded += matrix[i][j]
                j += 1
                i += 1
        else:
            i = key - 2
            while i > 0:
                decoded += matrix[i][j]
                j += 1
                i -= 1
        flag += 1
    return decoded

text = input("Enter text: ")
key = int(input("Enter the key: "))
ch = input("Press E to encode or D to decode: ")
if ch == 'e' or ch == 'E':
    print("Encoded Text: " + encode(text.lower(), key))
elif ch == 'd' or ch == 'D':
    print("Decoded Text: " + decode(text.lower(), key))
