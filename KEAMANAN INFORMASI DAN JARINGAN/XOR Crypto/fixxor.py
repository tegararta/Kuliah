
def encrypt(text, key):
    char = list(text)
    bit = []
    bits = bit

    # Mengubah pesan Plaintext enjadi representasi bit
    for i in range(len(char)):
        num = ord(char[i])
        bit_representation = bin(num)
        biner = bit_representation[2:].zfill(8)
        bit.append(biner)
    p = "Plaintext   : " + ''.join(bits)
    print(p)

    # Mengubah kunci menjadi representasi bit
    key_char = list(key)
    key_bit = []
    for i in range(len(char)):  # Mengulang kunci sesuai panjang pesan
        # Menggunakan modulus untuk mengulang kunci secara periodik
        num = ord(key_char[i % len(key_char)])
        bit_representation = bin(num)
        biner = bit_representation[2:].zfill(8)
        key_bit.append(biner)

    k = "key         : " + ''.join(key_bit)
    print(k)

    enc = []
    # Melakukan XOR pada setiap bit
    for i in range(len(bit)):
        bit[i] = int(bit[i], 2)
        key_bit[i] = int(key_bit[i], 2)
        bit[i] = bit[i] ^ key_bit[i]
        bit[i] = bin(bit[i])[2:].zfill(8)
        enc.append(bit[i])

    c = "Chiphertext : " + ''.join(enc)
    print(c)
    characters = []
    dec = []
    for bit_representation in bits:
        desimal = int(bit_representation, 2)
        character = chr(desimal)
        dec.append(desimal)
        characters.append(character)

    encrypted_text = "Char    : " + ''.join(characters)
    d = "desimal : " + ''.join(str(dec))

    # Menulis hasil enkripsi ke dalam file teks
    with open("file.txt", "w") as file:
        file.write("Encrypt \n")
        file.write(p)
        file.write("\n")
        file.write(k)
        file.write("\n")
        file.write(c)
        file.write("\n")
        file.write(d)
        file.write("\n")
        file.write(encrypted_text)
        file.close()


def decrypt(text, key):
    # Split binner menjadi potongan 8 bit
    chip = [text[i:i+8] for i in range(0, len(text), 8)]
    key_bin = [key[i:i+8] for i in range(0, len(key), 8)]

    # Melakukan XOR pada setiap bit
    decrypted_text = []
    for i in range(len(chip)):
        num = int(chip[i], 2)
        key_index = i % len(key_bin)
        key_num = int(key_bin[key_index], 2)
        decrypted_num = num ^ key_num
        decrypted_text.append(chr(decrypted_num))

    result = ''.join(decrypted_text)
    print("Hasil dekripsi:", result)


def main():
    out = True

    while out:

        print("Program XOR Cipher")
        print("==================")
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Keluar")
        print("==================")
        pilihan = input("Masukkan pilihan: ")
        if pilihan == "1":
            print("Enkripsi")
            print("========")
            inpt = input("Masukkan pesan: ")
            key = input("Masukkan kunci: ")
            encrypt(inpt, key)

        elif pilihan == "2":
            print("Dekripsi")
            print("========")
            inpt = input("Masukkan pesan Biner: ")
            key = input("Masukkan kunci: ")
            decrypt(inpt, key)
        elif pilihan == "3":
            out = False


main()
