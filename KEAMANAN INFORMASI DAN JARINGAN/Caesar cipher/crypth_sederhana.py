import string
import os
def encrypt(alphabet, msg, key):
    encrypt = ''
    for i in msg:
        position = alphabet.find(i)
        newposition = (position + int(key)) % len(alphabet)
        encrypt += alphabet [newposition]

    return encrypt

def decrypt(alphabet, msg, key):
    decrypt = ''
    for i in msg:
        position = alphabet.find(i)
        newposition = (position + -int(key)) % len(alphabet)
        decrypt += alphabet [newposition]

    return decrypt

def main():
    alp = string.ascii_letters + string.digits + string.punctuation + ' '
    out = True
    while out:
        select = input("Menu :\n1. Encrypt\n2. Decrypt\n3. Exit\nSelect : ")
        if select == '3':
            out = False
        elif select == '1':
            Private_key = input("Input Key: ")  
            message = input ('Masukan text untuk di encrypt : ')
            result = encrypt(alp, message, Private_key)
            print(f'Encrypted Message: {result}' )
        elif select == '2':
            message = input ('Masukan text untuk di decrypt : ')
            Private_key = input("Key? ")
            result = decrypt(alp, message, Private_key)
            print('Decrypted Message: ' + (result) )
        else:
            os.system('cls || clear')
            print("Tidak Tersedia")
            continue
main()
