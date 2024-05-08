# def ExtendedEuclidean(a, b):
#     if a == 0:
#         return (b, 0, 1)
#     else:
#         g, y, x = ExtendedEuclidean(b % a, a)
#         return (g, x - (b // a) * y, y)

# def ModularInverse(a, m):
#     g, x, y = ExtendedEuclidean(a, m)
#     if g != 1:
#         raise Exception('Modular inverse does not exist')
#     else:
#         return x % m

# def affine_encrypt(text, key):
#     '''
#     C = (a*P + b) % 26
#     '''
#     return ''.join([chr(((key[0]*(ord(t) - ord('A')) + key[1]) % 26)
#                   + ord('A')) for t in text.upper().replace(' ', '')])

# def affine_decrypt(cipher, key):
#     '''
#     P = (a^-1 * (C - b)) % 26
#     '''
#     return ''.join([chr(((ModularInverse(key[0], 26)*(ord(c) - ord('A') - key[1]))
#                     % 26) + ord('A')) for c in cipher])

# # Get user input for text
# text = input("Enter the text to encrypt: ").upper()

# # Get user input for key values
# a = int(input("Enter the value of 'a' (must be coprime with 26): "))
# b = int(input("Enter the value of 'b': "))
# key = (a, b)

# encrypted_text = affine_encrypt(text, key)
# decrypted_text = affine_decrypt(encrypted_text, key)

# print("Original Text: " + text)
# print("Encrypted Text: " + encrypted_text)
# print("Decrypted Text: " + decrypted_text)

def ExtendedEuclidean(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = ExtendedEuclidean(b % a, a)
        return g, x - (b // a) * y, y


def ModularInverse(a, m):
    g, x, y = ExtendedEuclidean(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    return x % m


def affine_encrypt(text, key):
    return ''.join([chr(((key[0] * (ord(t) - ord('A')) + key[1]) % 26) + ord('A')) for t in text.upper().replace(' ', '')])


def affine_decrypt(cipher, key):
    return ''.join([chr(((ModularInverse(key[0], 26) * (ord(c) - ord('A') - key[1])) % 26) + ord('A')) for c in cipher])


def get_user_input():
    text = input("enter the text to encrypt: ").upper()
    a = int(input("enter the value of 'a' "))
    b = int(input("enter the value of 'b': "))
    key = a, b
    return text, key


def main():
    text, key = get_user_input()
    encrypted_text = affine_encrypt(text, key)
    decrypted_text = affine_decrypt(encrypted_text, key)

    print(f"Encrypted Text: {encrypted_text}")
    print(f"Decrypted Text: {decrypted_text}")


if __name__ == "__main__":
    main()