# Contoh Sibtitusi Sederhana Caesar Cipher

## Algoritma dari kode ini

Plaintext to Chipertext
```bash
def encrypt(chrt, msg, key):
    encrypt = ''
    key = 0
   # Mencari posisi chart pada kata kunci agar di jadikan key encrypt 
    for i in key:
        poskey = chrt.find(i)
        key += poskey
   # 
    for i in msg:
        position = chrt.find(i)
        newposition = (position + key) % len(chrt)
        encrypt += chrt [newposition]

    return encrypt
```

## Langkah Menggunakan
1. Jalankan file crypth_sederhana.py pada komputer anda
2. Lalu akan menampilkan beberapa menu
   ```bash
     Menu :    
      1. Encrypt
      2. Decrypt
      3. Exit   
      Select : 
     ```
3. Menu Encrypt untuk mengubah Plaintext ke Chipertext dan Decrypt ialah mengubah Chipertext ke Plaintext. 
4. Lalu akan di mintai kata kunci sebagai penggeseran setiap huruf dalam pesan asli sejumlah langkah tertentu dalam alfabet.
5. Contoh Output :
   ```bash
   Menu :    
   1. Encrypt
   2. Decrypt
   3. Exit   
   Select : 1
   Input Key: aku
   Masukan text untuk di encrypt : hallo
   Encrypted Message: LEPPS
   Menu :
   1. Encrypt
   2. Decrypt
   3. Exit
   Select : 2
   Masukan text untuk di decrypt : LEPPS
   Key? aku
   Decrypted Message: hallo
   Menu :
   1. Encrypt
   2. Decrypt
   3. Exit
   Select : 2
   Masukan text untuk di decrypt : LEPPS
   Key? lupa
   Decrypted Message: ]<{{~
   ```

   ## Referensi
   [bobthebot101](https://github.com/bobthebot101/Encrypt-Decrypt-Python)
