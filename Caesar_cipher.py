# Caesar cipher encrypting a message
def encrypt_mess(text):
    cipher = ''
    for char in text:
        if not char.isalpha():
            continue
        char = char.upper()
        code = ord(char) + 1
        if code > ord('Z'):
            code = ord('A')
        cipher += chr(code)
    return cipher

#Caesar cipher decrypting a message
def decrypt_mess(text):
    decrypt = ''
    for char in text:
        if not char.isalpha():
            continue
        char = char.upper()
        code = ord(char) - 1
        if code < ord('A'):
            code = ord('Z')
        decrypt += chr(code)
    return decrypt


print(encrypt_mess(input('Enter your message: ')))
print(decrypt_mess(input('Enter your message: ')))
