# Caesar Cipher Encryption/Decryption App

## Interview Assignment for ECW

This is my interview assignment for ECW, where I was asked to implement a simple python application.

---

## Overview

This is a simple command-line application that implements the Caesar Cipher encryption and decryption technique. The application allows users to encrypt and decrypt text messages using a shift value of their choice. The app works with both uppercase and lowercase letters, and it retains spaces and punctuation marks as they are.

### Key Features:
- **Encrypt Text**: Allows the user to input text and a shift value, then outputs the encrypted text.
- **Decrypt Text**: Allows the user to input encrypted text and the shift value used for encryption, then outputs the original, decrypted text.
- **Shift Value**: Users can specify a shift value between 1 and 25 to control the level of encryption.
- **Command-Line Interface**: The app is menu-driven, making it easy to use via the terminal.

---

## How It Works

The Caesar Cipher works by shifting the letters of the alphabet by a fixed number (the shift value). For example, with a shift of 3, the letter `A` becomes `D`, `B` becomes `E`, and so on. If the shift exceeds `Z`, it wraps around back to `A`.

This app provides two functionalities:
1. **Encrypting a Message**: Using a shift value, each letter in the message is shifted by the specified value.
2. **Decrypting a Message**: This reverses the encryption process by shifting the letters back by the same shift value.

---

## How to Use the Application

### Step 1: Clone the Repository (or Copy the Code)

If you're running this on your local machine, you can copy the Python script, or clone the repository if provided.

### Step 2: Run the Script

1. Open a terminal window.
2. Navigate to the directory where the script is located.
3. Run the Python script by typing:

```bash
python caesar_cipher.py
