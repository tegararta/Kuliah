XOR Cipher Program
Overview
This Python program implements a simple XOR Cipher for encrypting and decrypting messages. XOR (exclusive or) cipher is a basic form of encryption that performs a bitwise XOR operation between the text to be encrypted and a key. The same process is used for both encryption and decryption, making it a symmetric encryption technique.

Features
Encrypt plaintext messages using a user-provided key.
Decrypt messages (provided in binary format) using the same key used for encryption.
The key is repeated or truncated to match the length of the plaintext message.
The encrypted message and various intermediate data are saved to a text file during encryption.
Interactive console-based user interface for easy operation.
How to Use
Start the Program: Run the program to see the main menu.
Choose an Option:
Select "1" for Encryption.
Select "2" for Decryption.
Select "3" to Exit the program.
For Encryption:
Enter the plaintext message when prompted.
Enter the key.
The program will display and save the encrypted message along with intermediate data.
For Decryption:
Enter the binary format of the encrypted message.
Enter the key used during encryption.
The program will display the decrypted message (original plaintext).
Encryption Process
Convert the plaintext message into its binary representation.
Convert the key into binary form, repeating or truncating it to match the plaintext length.
Perform a bitwise XOR operation between each bit of the binary plaintext and the binary key.
Convert the resulting binary sequence back into characters to form the encrypted message.
Save all relevant data to a file for reference.
Decryption Process
Split the binary encrypted message into 8-bit chunks.
Perform a bitwise XOR operation between each chunk and the corresponding chunk of the binary key.
Convert the resulting binary numbers back to characters, forming the decrypted message (original plaintext).
Requirements
Python 3.x
Note
This cipher is not secure for sensitive data encryption. It is mainly for educational purposes and demonstrates the basic concept of symmetric key encryption.
The effectiveness of the cipher greatly depends on the secrecy of the key.
