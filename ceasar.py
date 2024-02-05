alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

logo = '''  ___   __   ____  ____   __   ____         ___  __  ____  _  _  ____  ____ 
 / __) / _\ (  __)/ ___) / _\ (  _ \       / __)(  )(  _ \/ )( \(  __)(  _ \.
( (__ /    \ ) _) \___ \/    \ )   /      ( (__  )(  ) __/) __ ( ) _)  )   /
 \___)\_/\_/(____)(____/\_/\_/(__\_)       \___)(__)(__)  \_)(_/(____)(__\_)
'''


def encrypt(text, shift):
    shift %= 26
    encrypted = ''
    for ele in text:
        for i in range(len(alphabet)):
            if ele == alphabet[i]:
                encrypted += alphabet[i + shift - 26]
        if ele not in alphabet:
            encrypted += ele
    print(encrypted)


def decrypt(text, shift):
    decrypted = ''
    for ele in text:
        for i in range(len(alphabet)):
            ind = i - shift + 26
            ind %= 26
            if ele == alphabet[i]:
                decrypted += alphabet[ind]
        if ele not in alphabet:
            decrypted += ele
    print(decrypted)


print(logo)
recipher = True

while recipher:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)

    want = input("do u want to continue? Yes/No").lower()
    if want == "yes":
        recipher = True
    else:
        recipher = False
        print("Goodbye!!!")
