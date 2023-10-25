import string
import os

def encrypt(chrt, msg, key):
    encrypt = ''
    key = 0
    for i in key:
        poskey = chrt.find(i)
        key += poskey

    for i in msg:
        position = chrt.find(i)
        newposition = (position + key) % len(chrt)
        encrypt += chrt [newposition]

    return encrypt

def decrypt(chrt, msg, key):
    decrypt = ''
    key = 0
    for i in key:
        poskey = chrt.find(i)
        key += poskey
    for i in msg:
        position = chrt.find(i)
        newposition = (position + -key) % len(chrt)
        decrypt += chrt [newposition]

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
