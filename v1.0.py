import tkinter as tk
from tkinter import filedialog

class FileEncryptorDecryptor:
    def __init__(self, root):
        self.root = root
        self.root.title("File Encryptor/Decryptor")

        # File Selection Frame
        self.file_frame = tk.Frame(root)
        self.file_frame.pack(pady=10)

        self.file_label = tk.Label(self.file_frame, text="Select File:")
        self.file_label.grid(row=0, column=0)

        self.file_path = tk.StringVar()
        self.file_entry = tk.Entry(self.file_frame, textvariable=self.file_path, width=40)
        self.file_entry.grid(row=0, column=1)

        self.browse_button = tk.Button(self.file_frame, text="Browse", command=self.browse_file)
        self.browse_button.grid(row=0, column=2)

        # Algorithm Selection Frame
        self.algorithm_frame = tk.Frame(root)
        self.algorithm_frame.pack(pady=10)

        self.algorithm_label = tk.Label(self.algorithm_frame, text="Select Algorithm:")
        self.algorithm_label.grid(row=0, column=0)

        self.algorithms = ["Algorithm 1 (Caesar Cipher)", "Algorithm 2 (Substitution Cipher)",
                           "Algorithm 3 (ROT13 Cipher)", "Algorithm 4 (Rail Fence Cipher)",
                           "Algorithm 5 (Row Transposition Cipher)", "Algorithm 6 (Affine Cipher)",
                           "Algorithm 7 (Playfair Cipher)","Algorithm 8 (Vigenere Cipher)"]
        self.algorithm_var = tk.StringVar()
        self.algorithm_dropdown = tk.OptionMenu(self.algorithm_frame, self.algorithm_var, *self.algorithms)
        self.algorithm_dropdown.grid(row=0, column=1)
        # Key Input Frame
        self.key_frame = tk.Frame(root)
        self.key_frame.pack(pady=10)

        self.key_label = tk.Label(self.key_frame, text="Enter Key:")
        self.key_label.grid(row=0, column=0)

        self.key_var = tk.StringVar()
        self.key_entry = tk.Entry(self.key_frame, textvariable=self.key_var, width=40)
        self.key_entry.grid(row=0, column=1)
        # Encrypt/Decrypt Buttons
        self.process_frame = tk.Frame(root)
        self.process_frame.pack(pady=10)

        self.encrypt_button = tk.Button(self.process_frame, text="Encrypt", command=self.encrypt_file)
        self.encrypt_button.grid(row=0, column=0, padx=10)

        self.decrypt_button = tk.Button(self.process_frame, text="Decrypt", command=self.decrypt_file)
        self.decrypt_button.grid(row=0, column=1, padx=10)

    def browse_file(self):
        file_path = filedialog.askopenfilename()
        self.file_path.set(file_path)

    def caesar_cipher(self, text, shift):
        result = ""

        # traverse text
        for char in text:
            if char.isalpha():  # Exclude spaces from encryption/decryption
                # Encrypt uppercase characters
                if char.isupper():
                    result += chr((ord(char) + shift - 65) % 26 + 65)
                # Encrypt lowercase characters
                else:
                    result += chr((ord(char) + shift - 97) % 26 + 97)
            else:
                result += char  # Preserve non-alphabetic characters
        return result

    def substitution_encrypt(self, plaintext, key):
        # Define the alphabet that we are using
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
        # Convert the plaintext to uppercase
        plaintext = plaintext.upper()
    
        # Create a dictionary to map each letter in the alphabet to the corresponding letter in the key
        substitution_dict = {alphabet[i]: key[i] for i in range(len(alphabet))}
    
        # Encrypt the plaintext
        ciphertext = ""
        for char in plaintext:
            if char in alphabet:
                ciphertext += substitution_dict[char]
            else:
                ciphertext += char
    
        return ciphertext

    def substitution_decrypt(self, ciphertext, key):
        # Define the alphabet that we are using
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        # Create a dictionary to map each letter in the key to the corresponding letter in the alphabet
        substitution_dict = {key[i]: alphabet[i] for i in range(len(alphabet))}

        # Decrypt the ciphertext
        plaintext = ""
        for char in ciphertext:
            if char in key:
                plaintext += substitution_dict[char]
            else:
                plaintext += char

        return plaintext

    def rail_fence_encrypt(self, plain_text, rails):
        # Creating an empty matrix to hold the rails
        rail_matrix = [['' for col in range(len(plain_text))] for row in range(rails)]

        # Variables to track the direction and position in the matrix
        row, col = 0, 0
        down = False

        for char in plain_text:
            # Check if we have reached the top or bottom rail
            if row == 0 or row == rails - 1:
                down = not down

            # Fill the matrix with characters
            rail_matrix[row][col] = char
            col += 1

            # Move to the next row based on direction
            if down:
                row += 1
            else:
                row -= 1

        # Combine the characters from each rail to form the cipher text
        cipher_text = ''.join([char for rail in rail_matrix for char in rail if char != ''])
        return cipher_text

    def rail_fence_decrypt(self, ciphertext, rails):
        # Initialize variables
        rail_lengths = [0] * rails
        current_rail = 0
        direction = 1

        # Calculate the lengths of each rail
        for i in range(len(ciphertext)):
            rail_lengths[current_rail] += 1
            current_rail += direction
            if current_rail == rails or current_rail == -1:
                direction *= -1
                current_rail += 2 * direction

        # Reconstruct the rails
        rails_text = [''] * rails
        current_index = 0
        for rail_index in range(rails):
            for _ in range(rail_lengths[rail_index]):
                rails_text[rail_index] += ciphertext[current_index]
                current_index += 1

        # Reconstruct the plaintext
        plaintext = ''
        current_rail = 0
        direction = 1
        for _ in range(len(ciphertext)):
            plaintext += rails_text[current_rail][0]
            rails_text[current_rail] = rails_text[current_rail][1:]
            current_rail += direction
            if current_rail == rails or current_rail == -1:
                direction *= -1
                current_rail += 2 * direction

        return plaintext
    def row_transposition_encrypt(self, message, key):
        # Remove spaces from the message
        message = message.replace(" ", "")
        
        # Calculate the number of rows needed
        rows = len(message) // len(key)
        if len(message) % len(key) != 0:
            rows += 1
        
        # Pad the message if necessary
        message += (len(key) - len(message) % len(key)) * "X"
        
        # Create the matrix for encryption
        matrix = []
        for i in range(rows):
            matrix.append(list(message[i * len(key):(i + 1) * len(key)]))
        
        # Rearrange the matrix according to the key
        sorted_key = sorted(key)
        ciphertext = ""
        for k in sorted_key:
            col_index = key.index(k)
            for row in matrix:
                ciphertext += row[col_index]
            ciphertext += " "  # Add space between characters
        
        return ciphertext.strip()  
    def row_transposition_decrypt(self, ciphertext, key):
        # Remove any spaces from the ciphertext
        ciphertext = ciphertext.replace(" ", "")
        
        # Calculate the number of rows
        num_of_rows = len(ciphertext) // len(key)
        
        # Create an empty grid
        arr = [[''] * len(key) for _ in range(num_of_rows)]
        
        # Fill the grid with the ciphertext
        idx = 0
        for k in sorted(range(len(key)), key=lambda x: key[x]):
            for i in range(num_of_rows):
                arr[i][k] = ciphertext[idx]
                idx += 1
        
        # Read off the plaintext
        plaintext = ''
        for i in range(num_of_rows):
            for j in range(len(key)):
                plaintext += arr[i][j]
            plaintext += ' '  # Add a space after each word
        
        return plaintext.strip()

    def ExtendedEuclidean(self, a, b):
        if a == 0:
            return b, 0, 1
        else:
            g, y, x = self.ExtendedEuclidean(b % a, a)
            return g, x - (b // a) * y, y

    def ModularInverse(self, a, m):
        g, x, y = self.ExtendedEuclidean(a, m)
        if g != 1:
            raise Exception('Modular inverse does not exist')
        return x % m

    def affine_encrypt(self, text, key):
        return ''.join([chr(((key[0] * (ord(t) - ord('A')) + key[1]) % 26) + ord('A')) if t.isalpha() else t for t in
                        text.upper()])

    def affine_decrypt(self, cipher, key):
        return ''.join([chr(((self.ModularInverse(key[0], 26) * (ord(c) - ord('A') - key[1])) % 26) + ord(
            'A')) if c.isalpha() else c for c in cipher])

    def generate_matrix(self, key):
        key = key.lower().replace("j", "i")
        key += "x"  # Ensure 'x' is included in the key
        key = "".join(dict.fromkeys(key))  # Remove duplicates
        alphabet = "abcdefghiklmnopqrstuvwxyz"
        key += alphabet
        matrix = []
        for char in key:
            if char not in matrix:
                matrix.append(char)
        matrix = [matrix[i:i + 5] for i in range(0, 25, 5)]
        return matrix

    def find_char_position(self, matrix, char):
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == char:
                    return (i, j)
        raise ValueError(f"Character {char} not found in matrix")

    def playfair_encrypt(self, plain_text, key):
        matrix = self.generate_matrix(key)
        plain_text = plain_text.lower().replace("j", "i")
        cipher_text = ""
        i = 0
        while i < len(plain_text):
            if plain_text[i] == " ":
                cipher_text += " "
                i += 1
            else:
                char1 = plain_text[i]
                char2 = plain_text[i + 1] if i + 1 < len(plain_text) and plain_text[i + 1] != " " else 'x'
                try:
                    pos1 = self.find_char_position(matrix, char1)
                    pos2 = self.find_char_position(matrix, char2)
                except ValueError as e:
                    print(e)
                    i += 1
                    continue
                if pos1[0] == pos2[0]:
                    cipher_text += matrix[pos1[0]][(pos1[1] + 1) % 5] + matrix[pos2[0]][(pos2[1] + 1) % 5]
                elif pos1[1] == pos2[1]:
                    cipher_text += matrix[(pos1[0] + 1) % 5][pos1[1]] + matrix[(pos2[0] + 1) % 5][pos2[1]]
                else:
                    cipher_text += matrix[pos1[0]][pos2[1]] + matrix[pos2[0]][pos1[1]]
                i += 2
        return cipher_text

    def playfair_decrypt(self, cipher_text, key):
        matrix = self.generate_matrix(key)
        plain_text = ""
        i = 0
        while i < len(cipher_text):
            if cipher_text[i] == " ":
                plain_text += " "
                i += 1
            else:
                char1 = cipher_text[i]
                char2 = cipher_text[i + 1]
                pos1 = self.find_char_position(matrix, char1)
                pos2 = self.find_char_position(matrix, char2)
                if pos1[0] == pos2[0]:
                    plain_text += matrix[pos1[0]][(pos1[1] - 1) % 5] + matrix[pos2[0]][(pos2[1] - 1) % 5]
                elif pos1[1] == pos2[1]:
                    plain_text += matrix[(pos1[0] - 1) % 5][pos1[1]] + matrix[(pos2[0] - 1) % 5][pos2[1]]
                else:
                    plain_text += matrix[pos1[0]][pos2[1]] + matrix[pos2[0]][pos1[1]]
                i += 2
        return plain_text
    def vigenere_encrypt(self, plain_text, key):
        plain_text = plain_text.upper()
        key = key.upper()
        encrypted_text = ""
        for i in range(len(plain_text)):
            char = plain_text[i]
            key_char = key[i % len(key)]
            if char.isalpha():
                encrypted_char = chr(((ord(char) - 65 + ord(key_char) - 65) % 26) + 65)
            else:
                encrypted_char = char
            encrypted_text += encrypted_char
        return encrypted_text
    def vigenere_decrypt(self, ciphertext, key):
        decrypted_text = ''
        key_length = len(key)
        key_as_int = [ord(char) - ord('A') for char in key.upper()]
        for i, char in enumerate(ciphertext):
            if char.isalpha():
                shift = key_as_int[i % key_length]
                if char.isupper():
                    decrypted_text += chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
                else:
                    decrypted_text += chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
            else:
                decrypted_text += char
        return decrypted_text


    def encrypt_file(self):
        file_path = self.file_path.get()
        algorithm = self.algorithm_var.get()
        key = self.key_var.get()

        if algorithm == "Algorithm 1 (Caesar Cipher)":
            shift = int(key)  # Define the shift value for Caesar cipher
            with open(file_path, 'r+') as file:
                text = file.read()
                encrypted_text = self.caesar_cipher(text, shift)
                file.seek(0)
                file.write(encrypted_text)
                file.truncate()
            print("Encrypting file:", file_path, "using algorithm:", algorithm)

        elif algorithm == "Algorithm 2 (Substitution Cipher)":
            with open(file_path, 'r+') as file:
                text = file.read()
                encrypted_text = self.substitution_encrypt(text,key)
                file.seek(0)
                file.write(encrypted_text)
                file.truncate()
            print("Encrypting file:", file_path, "using algorithm:", algorithm)

        elif algorithm == "Algorithm 3 (ROT13 Cipher)":
            with open(file_path, 'r+') as file:
                text = file.read()
                encrypted_text = self.rot13_cipher(text)
                file.seek(0)
                file.write(encrypted_text)
                file.truncate()
            print("Encrypting file:", file_path, "using algorithm:", algorithm)

        elif algorithm == "Algorithm 4 (Rail Fence Cipher)":
            rails = int(key)  # Define the number of rails for Rail Fence Cipher
            with open(file_path, 'r+') as file:
                text = file.read()
                encrypted_text = self.rail_fence_encrypt(text, rails)
                file.seek(0)
                file.write(encrypted_text)
                file.truncate()
            print("Encrypting file:", file_path, "using algorithm:", algorithm)
        elif algorithm == "Algorithm 5 (Row Transposition Cipher)":

            with open(file_path, 'r+') as file:
                text = file.read()
                encrypted_text = self.row_transposition_encrypt(text, key)
                file.seek(0)
                file.write(encrypted_text)
                file.truncate()
            print("Encrypting file:", file_path, "using algorithm:", algorithm)
        elif algorithm == "Algorithm 6 (Affine Cipher)":
            a, b = map(int, key.split(','))  # Assume the key is two numbers separated by a comma
            with open(file_path, 'r+') as file:
                text = file.read()
                encrypted_text = self.affine_encrypt(text, (a, b))
                file.seek(0)
                file.write(encrypted_text)
                file.truncate()
            print("Encrypting file:", file_path, "using algorithm:", algorithm)
        elif algorithm == "Algorithm 7 (Playfair Cipher)":
            with open(file_path, 'r+') as file:
                text = file.read()
                encrypted_text = self.playfair_encrypt(text, key)
                file.seek(0)
                file.write(encrypted_text)
                file.truncate()
            print("Encrypting file:", file_path, "using algorithm:", algorithm)
        elif algorithm == "Algorithm 8 (Vigenere Cipher)":
            with open(file_path, 'r+') as file:
                text = file.read()
                encrypted_text = self.vigenere_encrypt(text, key)
                file.seek(0)
                file.write(encrypted_text)
            print("Encrypting file:", file_path, "using algorithm:", algorithm)

    def decrypt_file(self):
        file_path = self.file_path.get()
        algorithm = self.algorithm_var.get()
        key = self.key_var.get()
        
        if algorithm == "Algorithm 1 (Caesar Cipher)":
            shift = int(key)  # Define the shift value for Caesar cipher
            with open(file_path, 'r+') as file:
                text = file.read()
                decrypted_text = self.caesar_cipher(text, -shift)  # Applying negative shift for decryption
                file.seek(0)
                file.write(decrypted_text)
                file.truncate()
            print("Decrypting file:", file_path, "using algorithm:", algorithm)

        elif algorithm == "Algorithm 2 (Substitution Cipher)":
            with open(file_path, 'r+') as file:
                text = file.read()
                decrypted_text = self.substitution_decrypt(text,key)
                file.seek(0)
                file.write(decrypted_text)
                file.truncate()
            print("Decrypting file:", file_path, "using algorithm:", algorithm)

        elif algorithm == "Algorithm 3 (ROT13 Cipher)":
            with open(file_path, 'r+') as file:
                text = file.read()
                decrypted_text = self.rot13_cipher(text)  # ROT13 is its own inverse
                file.seek(0)
                file.write(decrypted_text)
                file.truncate()
            print("Decrypting file:", file_path, "using algorithm:", algorithm)

        elif algorithm == "Algorithm 4 (Rail Fence Cipher)":
            rails = int(key)  # Define the number of rails for Rail Fence Cipher
            with open(file_path, 'r+') as file:
                text = file.read()
                decrypted_text = self.rail_fence_decrypt(text, rails)
                file.seek(0)
                file.write(decrypted_text)
                file.truncate()
            print("Decrypting file:", file_path, "using algorithm:", algorithm)
        elif algorithm == "Algorithm 5 (Row Transposition Cipher)":

            with open(file_path, 'r+') as file:
                text = file.read()
                decrypted_text = self.row_transposition_decrypt(text, key)
                file.seek(0)
                file.write(decrypted_text)
                file.truncate()
            print("Decrypting file:", file_path, "using algorithm:", algorithm)
        elif algorithm == "Algorithm 6 (Affine Cipher)":
            a, b = map(int, key.split(','))  # Assume the key is two numbers separated by a comma
            with open(file_path, 'r+') as file:
                text = file.read()
                decrypted_text = self.affine_decrypt(text, (a, b))
                file.seek(0)
                file.write(decrypted_text)
                file.truncate()
            print("Decrypting file:", file_path, "using algorithm:", algorithm)
        elif algorithm == "Algorithm 7 (Playfair Cipher)":
            with open(file_path, 'r+') as file:
                text = file.read()
                decrypted_text = self.playfair_decrypt(text, key)
                file.seek(0)
                file.write(decrypted_text)
                file.truncate()
            print("Decrypting file:", file_path, "using algorithm:", algorithm)
        elif algorithm == "Algorithm 8 (Vigenere Cipher)":
            with open(file_path, 'r+') as file:
                text = file.read()
                decrypted_text = self.vigenere_decrypt(text, key)
                file.seek(0)
                file.write(decrypted_text)
            print("Decrypting file:", file_path, "using algorithm:", algorithm)

if __name__ == "__main__":
    root = tk.Tk()
    app = FileEncryptorDecryptor(root)
    root.mainloop()