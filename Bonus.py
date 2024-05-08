import sys


def are_coprime(a, b):
    while b != 0:
        a, b = b, a % b
    return a == 1

# Function to find the modular multiplicative inverse
def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

# Function to encrypt plaintext
def encrypt(plaintext, a, b):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.islower():
                ciphertext += chr(((a * (ord(char) - ord('a')) + b) % 26) + ord('a'))
            elif char.isupper():
                ciphertext += chr(((a * (ord(char) - ord('A')) + b) % 26) + ord('A'))
        else:
            ciphertext += char
    return ciphertext

# Function to decrypt ciphertext
def decrypt(ciphertext, a, b):
    plaintext = ""
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        print("Error: Modular inverse of 'a' does not exist.")
        sys.exit(1)
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                plaintext += chr(((a_inv * (ord(char) - ord('a') - b)) % 26) + ord('a'))
            elif char.isupper():
                plaintext += chr(((a_inv * (ord(char) - ord('A') - b)) % 26) + ord('A'))
        else:
            plaintext += char
    return plaintext

def main():
    # Prompt user for choice: encryption or decryption
    choice = input("Enter 'e' for encryption or 'd' for decryption: ").lower()
    if choice not in ['e', 'd']:
        print("Invalid choice. Please enter 'e' or 'd'.")
        return

    # Prompt user for key values
    a = int(input("Enter the value of 'a' (must be coprime with 26): "))
    b = int(input("Enter the value of 'b' (0-25): "))
    if not are_coprime(a, 26):
        print("Error: 'a' is not coprime with 26.")
        return

    # Prompt user for plaintext or ciphertext
    if choice == 'e':
        plaintext = input("Enter the plaintext: ")
        ciphertext = encrypt(plaintext, a, b)
        print("Encrypted ciphertext:", ciphertext)
    else:
        ciphertext = input("Enter the ciphertext: ")
        plaintext = decrypt(ciphertext, a, b)
        print("Decrypted plaintext:", plaintext)

if __name__ == "__main__":
    main()
