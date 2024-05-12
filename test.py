# def generate_matrix(key):
#     key = key.replace("j", "i")
#     key = "".join(dict.fromkeys(key))
#     alphabet = "abcdefghiklmnopqrstuvwxyz"
#     key += alphabet
#     matrix = []
#     for char in key:
#         if char not in matrix:
#             matrix.append(char)
#     matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
#     return matrix
#
# def find_char_position(matrix, char):
#     for i in range(5):
#         for j in range(5):
#             if matrix[i][j] == char:
#                 return (i, j)
#
# def encrypt(plain_text, key):
#     matrix = generate_matrix(key)
#     plain_text = plain_text.lower().replace("j", "i")
#     plain_text = plain_text.replace(" ", "")
#     cipher_text = ""
#     for i in range(0, len(plain_text), 2):
#         char1 = plain_text[i]
#         char2 = plain_text[i+1] if i+1 < len(plain_text) else 'x'
#         pos1 = find_char_position(matrix, char1)
#         pos2 = find_char_position(matrix, char2)
#         if pos1[0] == pos2[0]:
#             cipher_text += matrix[pos1[0]][(pos1[1] + 1) % 5] + matrix[pos2[0]][(pos2[1] + 1) % 5]
#         elif pos1[1] == pos2[1]:
#             cipher_text += matrix[(pos1[0] + 1) % 5][pos1[1]] + matrix[(pos2[0] + 1) % 5][pos2[1]]
#         else:
#             cipher_text += matrix[pos1[0]][pos2[1]] + matrix[pos2[0]][pos1[1]]
#     return cipher_text
#
# def decrypt(cipher_text, key):
#     matrix = generate_matrix(key)
#     plain_text = ""
#     for i in range(0, len(cipher_text), 2):
#         char1 = cipher_text[i]
#         char2 = cipher_text[i+1]
#         pos1 = find_char_position(matrix, char1)
#         pos2 = find_char_position(matrix, char2)
#         if pos1[0] == pos2[0]:
#             plain_text += matrix[pos1[0]][(pos1[1] - 1) % 5] + matrix[pos2[0]][(pos2[1] - 1) % 5]
#         elif pos1[1] == pos2[1]:
#             plain_text += matrix[(pos1[0] - 1) % 5][pos1[1]] + matrix[(pos2[0] - 1) % 5][pos2[1]]
#         else:
#             plain_text += matrix[pos1[0]][pos2[1]] + matrix[pos2[0]][pos1[1]]
#     return plain_text
#
# def main():
#     choice = input("Enter 'E' for encryption or 'D' for decryption: ").upper()
#     if choice == 'E':
#         plain_text = input("Enter the plain text: ")
#         key = input("Enter the key: ")
#         cipher_text = encrypt(plain_text, key)
#         print("Encrypted text:", cipher_text)
#     elif choice == 'D':
#         cipher_text = input("Enter the cipher text: ")
#         key = input("Enter the key: ")
#         decrypted_text = decrypt(cipher_text, key)
#         print("Decrypted text:", decrypted_text)
#     else:
#         print("Invalid choice. Please enter 'E' or 'D'.")
#
# if __name__ == "__main__":
#     main()



# Affine Cipher
# def affine_encrypt(self, text, key):
#     return ''.join([chr(((key[0] * (ord(t) - ord('A')) + key[1]) % 26) + ord('A')) if t.isalpha() else t for t in text.upper()])
#
# def affine_decrypt(self, cipher, key):
#     return ''.join([chr(((self.ModularInverse(key[0], 26) * (ord(c) - ord('A') - key[1])) % 26) + ord('A')) if c.isalpha() else c for c in cipher])
#
# # Playfair Cipher
# def playfair_encrypt(self, plain_text, key):
#     matrix = self.generate_matrix(key)
#     cipher_text = ""
#     i = 0
#     while i < len(plain_text):
#         if plain_text[i].isalpha():
#             char1 = plain_text[i]
#             char2 = plain_text[i + 1] if i + 1 < len(plain_text) and plain_text[i + 1].isalpha() else 'x'
#             pos1 = self.find_char_position(matrix, char1)
#             pos2 = self.find_char_position(matrix, char2)
#             if pos1[0] == pos2[0]:
#                 cipher_text += matrix[pos1[0]][(pos1[1] + 1) % 5] + matrix[pos2[0]][(pos2[1] + 1) % 5]
#             elif pos1[1] == pos2[1]:
#                 cipher_text += matrix[(pos1[0] + 1) % 5][pos1[1]] + matrix[(pos2[0] + 1) % 5][pos2[1]]
#             else:
#                 cipher_text += matrix[pos1[0]][pos2[1]] + matrix[pos2[0]][pos1[1]]
#             i += 2
#         else:
#             cipher_text += plain_text[i]
#             i += 1
#     return cipher_text
#
# def playfair_decrypt(self, cipher_text, key):
#     matrix = self.generate_matrix(key)
#     plain_text = ""
#     i = 0
#     while i < len(cipher_text):
#         if cipher_text[i].isalpha():
#             char1 = cipher_text[i]
#             char2 = cipher_text[i + 1]
#             pos1 = self.find_char_position(matrix, char1)
#             pos2 = self.find_char_position(matrix, char2)
#             if pos1[0] == pos2[0]:
#                 plain_text += matrix[pos1[0]][(pos1[1] - 1) % 5] + matrix[pos2[0]][(pos2[1] - 1) % 5]
#             elif pos1[1] == pos2[1]:
#                 plain_text += matrix[(pos1[0] - 1) % 5][pos1[1]] + matrix[(pos2[0] - 1) % 5][pos2[1]]
#             else:
#                 plain_text += matrix[pos1[0]][pos2[1]] + matrix[pos2[0]][pos1[1]]
#             i += 2
#         else:
#             plain_text += cipher_text[i]
#             i += 1
#     return plain_text
#
# # Vigenere Cipher
# def vigenere_encrypt(self, plain_text, key):
#     plain_text = plain_text.upper()
#     key = key.upper()
#     encrypted_text = ""
#     j = 0
#     for i in range(len(plain_text)):
#         char = plain_text[i]
#         if char.isalpha():
#             key_char = key[j % len(key)]
#             encrypted_char = chr(((ord(char) - 65 + ord(key_char) - 65) % 26) + 65)
#             j += 1
#         else:
#             encrypted_char = char
#         encrypted_text += encrypted_char
#     return encrypted_text
#
# def vigenere_decrypt(self, ciphertext, key):
#     decrypted_text = ''
#     key_length = len(key)
#     key_as_int = [ord(char) - ord('A') for char in key.upper()]
#     j = 0
#     for i, char in enumerate(ciphertext):
#         if char.isalpha():
#             shift = key_as_int[j % key_length]
#             decrypted_char = chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
#             j += 1
#         else:
#             decrypted_char = char
#         decrypted_text += decrypted_char
#     return decrypted_text


#
# class FileEncryptorDecryptor:
#     def __init__(self, root):
#         # ... existing code ...
#
#         # Text Entry Frame
#         self.text_frame = tk.Frame(root)
#         self.text_frame.pack(pady=10)
#
#         self.text_label = tk.Label(self.text_frame, text="Enter Text:")
#         self.text_label.grid(row=0, column=0)
#
#         self.text_var = tk.StringVar()
#         self.text_entry = tk.Entry(self.text_frame, textvariable=self.text_var, width=40)
#         self.text_entry.grid(row=0, column=1)
#
#         # Encrypt/Decrypt Text Buttons
#         self.text_process_frame = tk.Frame(root)
#         self.text_process_frame.pack(pady=10)
#
#         self.text_encrypt_button = tk.Button(self.text_process_frame, text="Encrypt Text", command=self.encrypt_text)
#         self.text_encrypt_button.grid(row=0, column=0, padx=10)
#
#         self.text_decrypt_button = tk.Button(self.text_process_frame, text="Decrypt Text", command=self.decrypt_text)
#         self.text_decrypt_button.grid(row=0, column=1, padx=10)
#
#         # Result Display Frame
#         self.result_frame = tk.Frame(root)
#         self.result_frame.pack(pady=10)
#
#         self.result_label = tk.Label(self.result_frame, text="Result:")
#         self.result_label.grid(row=0, column=0)
#
#         self.result_var = tk.StringVar()
#         self.result_entry = tk.Entry(self.result_frame, textvariable=self.result_var, width=40)
#         self.result_entry.grid(row=0, column=1)
#
#     # ... existing code ...
#
#     def encrypt_text(self):
#         text = self.text_var.get()
#         algorithm = self.algorithm_var.get()
#         key = self.key_var.get()
#
#         # ... existing code ...
#
#         if algorithm == "Algorithm 1 (Caesar Cipher)":
#             shift = int(key)  # Define the shift value for Caesar cipher
#             encrypted_text = self.caesar_cipher(text, shift)
#             self.result_var.set(encrypted_text)
#
#         # ... similar code for other algorithms ...
#
#     def decrypt_text(self):
#         text = self.text_var.get()
#         algorithm = self.algorithm_var.get()
#         key = self.key_var.get()
#
#         # ... existing code ...
#
#         if algorithm == "Algorithm 1 (Caesar Cipher)":
#             shift = int(key)  # Define the shift value for Caesar cipher
#             decrypted_text = self.caesar_cipher(text, -shift)  # Applying negative shift for decryption
#             self.result_var.set(decrypted_text)
#
#         # ... similar code for other algorithms ...
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#         class FileEncryptorDecryptor:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("File Encryptor/Decryptor")
#
#         # File Selection Frame
#         self.file_frame = tk.Frame(root)
#         self.file_frame.pack(pady=10)
#
#         self.file_label = tk.Label(self.file_frame, text="Select File:")
#         self.file_label.grid(row=0, column=0)
#
#         self.file_path = tk.StringVar()
#         self.file_entry = tk.Entry(self.file_frame, textvariable=self.file_path, width=40)
#         self.file_entry.grid(row=0, column=1)
#
#         self.browse_button = tk.Button(self.file_frame, text="Browse", command=self.browse_file)
#         self.browse_button.grid(row=0, column=2)
#
#         # Algorithm Selection Frame
#         self.algorithm_frame = tk.Frame(root)
#         self.algorithm_frame.pack(pady=10)
#
#         self.algorithm_label = tk.Label(self.algorithm_frame, text="Select Algorithm:")
#         self.algorithm_label.grid(row=0, column=0)
#
#         self.algorithms = ["Algorithm 1 (Caesar Cipher)", "Algorithm 2 (Substitution Cipher)",
#                            "Algorithm 3 (ROT13 Cipher)", "Algorithm 4 (Rail Fence Cipher)",
#                            "Algorithm 5 (Row Transposition Cipher)", "Algorithm 6 (Affine Cipher)",
#                            "Algorithm 7 (Playfair Cipher)","Algorithm 8 (Vigenere Cipher)"]
#         self.algorithm_var = tk.StringVar()
#         self.algorithm_dropdown = tk.OptionMenu(self.algorithm_frame, self.algorithm_var, *self.algorithms)
#         self.algorithm_dropdown.grid(row=0, column=1)
#
#         # Key Input Frame
#         self.key_frame = tk.Frame(root)
#         self.key_frame.pack(pady=10)
#
#         self.key_label = tk.Label(self.key_frame, text="Enter Key:")
#         self.key_label.grid(row=0, column=0)
#
#         self.key_var = tk.StringVar()
#         self.key_entry = tk.Entry(self.key_frame, textvariable=self.key_var, width=40)
#         self.key_entry.grid(row=0, column=1)
#
#         # Text Entry Frame
#         self.text_frame = tk.Frame(root)
#         self.text_frame.pack(pady=10)
#
#         self.text_label = tk.Label(self.text_frame, text="Enter Text:")
#         self.text_label.grid(row=0, column=0)
#
#         self.text_var = tk.StringVar()
#         self.text_entry = tk.Entry(self.text_frame, textvariable=self.text_var, width=40)
#         self.text_entry.grid(row=0, column=1)
#
#         # Encrypt/Decrypt Text Buttons
#         self.text_process_frame = tk.Frame(root)
#         self.text_process_frame.pack(pady=10)
#
#         self.text_encrypt_button = tk.Button(self.text_process_frame, text="Encrypt Text", command=self.encrypt_text)
#         self.text_encrypt_button.grid(row=0, column=0, padx=10)
#
#         self.text_decrypt_button = tk.Button(self.text_process_frame, text="Decrypt Text", command=self.decrypt_text)
#         self.text_decrypt_button.grid(row=0, column=1, padx=10)
#
#         # Result Display Frame
#         self.result_frame = tk.Frame(root)
#         self.result_frame.pack(pady=10)
#
#         self.result_label = tk.Label(self.result_frame, text="Result:")
#         self.result_label.grid(row=0, column=0)
#
#         self.result_var = tk.StringVar()
#         self.result_entry = tk.Entry(self.result_frame, textvariable=self.result_var, width=40)
#         self.result_entry.grid(row=0, column=1)
#
#         # Encrypt/Decrypt Buttons
#         self.process_frame = tk.Frame(root)
#         self.process_frame.pack(pady=10)
#
#         self.encrypt_button = tk.Button(self.process_frame, text="Encrypt", command=self.encrypt_file)
#         self.encrypt_button.grid(row=0, column=0, padx=10)
#
#         self.decrypt_button = tk.Button(self.process_frame, text="Decrypt", command=self.decrypt_file)
#         self.decrypt_button.grid(row=0, column=1, padx=10)
#
#
#
#         def decrypt_text(self):
#     text = self.text_var.get()
#     algorithm = self.algorithm_var.get()
#     key = self.key_var.get()
#
#     if algorithm == "Algorithm 1 (Caesar Cipher)":
#         shift = int(key)  # Define the shift value for Caesar cipher
#         decrypted_text = self.caesar_cipher(text, -shift)  # Applying negative shift for decryption
#         self.result_var.set(decrypted_text)
#
#     elif algorithm == "Algorithm 2 (Substitution Cipher)":
#         decrypted_text = self.substitution_decrypt(text, key)
#         self.result_var.set(decrypted_text)
#
#     elif algorithm == "Algorithm 3 (ROT13 Cipher)":
#         decrypted_text = self.rot13_cipher(text)  # ROT13 is its own inverse
#         self.result_var.set(decrypted_text)
#
#     elif algorithm == "Algorithm 4 (Rail Fence Cipher)":
#         rails = int(key)  # Define the number of rails for Rail Fence Cipher
#         decrypted_text = self.rail_fence_decrypt(text, rails)
#         self.result_var.set(decrypted_text)
#
#     elif algorithm == "Algorithm 5 (Row Transposition Cipher)":
#         decrypted_text = self.row_transposition_decrypt(text, key)
#         self.result_var.set(decrypted_text)
#
#     elif algorithm == "Algorithm 6 (Affine Cipher)":
#         a, b = map(int, key.split(','))  # Assume the key is two numbers separated by a comma
#         decrypted_text = self.affine_decrypt(text, (a, b))
#         self.result_var.set(decrypted_text)
#
#     elif algorithm == "Algorithm 7 (Playfair Cipher)":
#         decrypted_text = self.playfair_decrypt(text, key)
#         self.result_var.set(decrypted_text)
#
#     elif algorithm == "Algorithm 8 (Vigenere Cipher)":
#         decrypted_text = self.vigenere_decrypt(text, key)
#         self.result_var.set(decrypted_text)
#
#
# # Encryption
# def encrypt(message, key):
#     # Remove spaces from the message
#     message = message.replace(" ", "")
#
#     # Calculate the number of rows needed
#     rows = len(message) // len(key)
#     if len(message) % len(key) != 0:
#         rows += 1
#
#     # Pad the message if necessary
#     message += (rows * len(key) - len(message)) * "X"
#
#     # Create the matrix for encryption
#     matrix = []
#     for i in range(rows):
#         matrix.append(list(message[i * len(key):(i + 1) * len(key)]))
#
#     # Rearrange the matrix according to the key
#     sorted_key = sorted(key)
#     ciphertext = ""
#     for k in sorted_key:
#         col_index = key.index(k)
#         for row in matrix:
#             ciphertext += row[col_index]
#         ciphertext += " "  # Add space between characters
#
#     return ciphertext.strip()
#
#
# def main():
#     message = input("Enter the message to encrypt: ")
#     key = input("Enter the key: ")
#
#     ciphertext = encrypt(message, key)
#     print("Encrypted Message:")
#     print(ciphertext)
#
#
# if _name_ == "_main_":
#     main()

# def generate_matrix(key):
#     key = key.replace("j", "i")
#     key = "".join(dict.fromkeys(key))
#     alphabet = "abcdefghiklmnopqrstuvwxyz"
#     key += alphabet
#     matrix = []
#     for char in key:
#         if char not in matrix:
#             matrix.append(char)
#     matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
#     return matrix
#
# def find_char_position(matrix, char):
#     for i in range(5):
#         for j in range(5):
#             if matrix[i][j] == char:
#                 return (i, j)
#
# def encrypt(plain_text, key):
#     matrix = generate_matrix(key)
#     plain_text = plain_text.lower().replace("j", "i")
#     plain_text = plain_text.replace(" ", "")
#     cipher_text = ""
#     for i in range(0, len(plain_text), 2):
#         char1 = plain_text[i]
#         char2 = plain_text[i+1] if i+1 < len(plain_text) else 'x'
#         pos1 = find_char_position(matrix, char1)
#         pos2 = find_char_position(matrix, char2)
#         if pos1[0] == pos2[0]:
#             cipher_text += matrix[pos1[0]][(pos1[1] + 1) % 5] + matrix[pos2[0]][(pos2[1] + 1) % 5]
#         elif pos1[1] == pos2[1]:
#             cipher_text += matrix[(pos1[0] + 1) % 5][pos1[1]] + matrix[(pos2[0] + 1) % 5][pos2[1]]
#         else:
#             cipher_text += matrix[pos1[0]][pos2[1]] + matrix[pos2[0]][pos1[1]]
#     return cipher_text

# def decrypt(cipher_text, key):
#     matrix = generate_matrix(key)
#     plain_text = ""
#     for i in range(0, len(cipher_text), 2):
#         char1 = cipher_text[i]
#         char2 = cipher_text[i+1]
#         pos1 = find_char_position(matrix, char1)
#         pos2 = find_char_position(matrix, char2)
#         if pos1[0] == pos2[0]:
#             plain_text += matrix[pos1[0]][(pos1[1] - 1) % 5] + matrix[pos2[0]][(pos2[1] - 1) % 5]
#         elif pos1[1] == pos2[1]:
#             plain_text += matrix[(pos1[0] - 1) % 5][pos1[1]] + matrix[(pos2[0] - 1) % 5][pos2[1]]
#         else:
#             plain_text += matrix[pos1[0]][pos2[1]] + matrix[pos2[0]][pos1[1]]
#     return plain_text

# def main():
#     choice = input("Enter 'E' for encryption or 'D' for decryption: ").upper()
#     if choice == 'E':
#         plain_text = input("Enter the plain text: ")
#         key = input("Enter the key: ")
#         cipher_text = encrypt(plain_text, key)
#         print("Encrypted text:", cipher_text)
#     elif choice == 'D':
#         cipher_text = input("Enter the cipher text: ")
#         key = input("Enter the key: ")
#         decrypted_text = decrypt(cipher_text, key)
#         print("Decrypted text:", decrypted_text)
#     else:
#         print("Invalid choice. Please enter 'E' or 'D'.")
#
# if __name__ == "__main__":
#     main()