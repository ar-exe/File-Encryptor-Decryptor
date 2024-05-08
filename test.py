def generate_matrix(key):
    key = key.replace("j", "i")
    key = "".join(dict.fromkeys(key))
    alphabet = "abcdefghiklmnopqrstuvwxyz"
    key += alphabet
    matrix = []
    for char in key:
        if char not in matrix:
            matrix.append(char)
    matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
    return matrix

def find_char_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return (i, j)

def encrypt(plain_text, key):
    matrix = generate_matrix(key)
    plain_text = plain_text.lower().replace("j", "i")
    plain_text = plain_text.replace(" ", "")
    cipher_text = ""
    for i in range(0, len(plain_text), 2):
        char1 = plain_text[i]
        char2 = plain_text[i+1] if i+1 < len(plain_text) else 'x'
        pos1 = find_char_position(matrix, char1)
        pos2 = find_char_position(matrix, char2)
        if pos1[0] == pos2[0]:
            cipher_text += matrix[pos1[0]][(pos1[1] + 1) % 5] + matrix[pos2[0]][(pos2[1] + 1) % 5]
        elif pos1[1] == pos2[1]:
            cipher_text += matrix[(pos1[0] + 1) % 5][pos1[1]] + matrix[(pos2[0] + 1) % 5][pos2[1]]
        else:
            cipher_text += matrix[pos1[0]][pos2[1]] + matrix[pos2[0]][pos1[1]]
    return cipher_text

def decrypt(cipher_text, key):
    matrix = generate_matrix(key)
    plain_text = ""
    for i in range(0, len(cipher_text), 2):
        char1 = cipher_text[i]
        char2 = cipher_text[i+1]
        pos1 = find_char_position(matrix, char1)
        pos2 = find_char_position(matrix, char2)
        if pos1[0] == pos2[0]:
            plain_text += matrix[pos1[0]][(pos1[1] - 1) % 5] + matrix[pos2[0]][(pos2[1] - 1) % 5]
        elif pos1[1] == pos2[1]:
            plain_text += matrix[(pos1[0] - 1) % 5][pos1[1]] + matrix[(pos2[0] - 1) % 5][pos2[1]]
        else:
            plain_text += matrix[pos1[0]][pos2[1]] + matrix[pos2[0]][pos1[1]]
    return plain_text

def main():
    choice = input("Enter 'E' for encryption or 'D' for decryption: ").upper()
    if choice == 'E':
        plain_text = input("Enter the plain text: ")
        key = input("Enter the key: ")
        cipher_text = encrypt(plain_text, key)
        print("Encrypted text:", cipher_text)
    elif choice == 'D':
        cipher_text = input("Enter the cipher text: ")
        key = input("Enter the key: ")
        decrypted_text = decrypt(cipher_text, key)
        print("Decrypted text:", decrypted_text)
    else:
        print("Invalid choice. Please enter 'E' or 'D'.")

if __name__ == "__main__":
    main()