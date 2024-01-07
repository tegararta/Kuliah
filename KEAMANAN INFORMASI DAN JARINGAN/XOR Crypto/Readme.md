# XOR Cipher Program

## Overview
This Python program implements the XOR Cipher, a simple yet fascinating method of encryption and decryption. It leverages the XOR (exclusive or) operation, which is a fundamental function in the realm of cryptography. This program allows users to encrypt plaintext messages and decrypt them using a specified key. The process is symmetric, which means the same key is used for both encrypting and decrypting.

## Features
- **Encryption**: Converts plaintext into an encrypted format using a key.
- **Decryption**: Reverts the encrypted message back to plaintext using the same key.
- **Key Management**: Automatically repeats or truncates the key to match the length of the plaintext.
- **File Output**: Generates a text file containing the encrypted data and various stages of the encryption process.
- **Interactive Interface**: User-friendly, console-based interface for ease of use.

## Installation
To use this program, you should have Python 3.x installed on your system. You can clone the repository or download the source code to run the program.

## Usage
1. **Starting the Program**: Run the program to access the main menu.
2. **Navigating the Menu**:
   - Select "1" for Encrypting a message.
   - Select "2" for Decrypting a message.
   - Select "3" to Exit the program.
3. **Encryption Process**:
   - Enter the plaintext message and the key as prompted.
   - The program encrypts the message and displays the result along with intermediate data.
4. **Decryption Process**:
   - Enter the binary format of the encrypted message and the key.
   - The program decrypts the message and displays the original plaintext.

## How it Works
### Encryption
- Converts the plaintext message into its binary representation.
- Adjusts the key to match the length of the plaintext, converting it into binary form.
- Performs a bitwise XOR operation between the binary plaintext and the binary key.
- Transforms the resulting binary sequence back into characters, forming the encrypted message.

### Decryption
- Splits the binary encrypted message into 8-bit segments.
- Conducts a bitwise XOR operation between each segment and the corresponding segment of the binary key.
- Converts the resulting binary numbers back to characters to reveal the original plaintext.

## Note
This cipher is intended for educational purposes and demonstrates the basic concept of symmetric key encryption. It is not recommended for securing sensitive data.
