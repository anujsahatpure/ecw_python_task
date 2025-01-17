import string

def caesar_cipher(text, shift, encrypt=True):
    result = ""
    shift = shift if encrypt else -shift
    for char in text:
        if char in string.ascii_letters:
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def main():
    while True:
        print("\nSimple Encryption-Decryption App")
        print("1. Encrypt Text")
        print("2. Decrypt Text")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            text = input("Enter text to encrypt: ")
            shift = int(input("Enter shift value (1-25): "))
            print("Encrypted Text:", caesar_cipher(text, shift, encrypt=True))
        
        elif choice == '2':
            text = input("Enter text to decrypt: ")
            shift = int(input("Enter shift value (1-25): "))
            print("Decrypted Text:", caesar_cipher(text, shift, encrypt=False))
        
        elif choice == '3':
            print("Exiting... Goodbye!")
            break
        
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
