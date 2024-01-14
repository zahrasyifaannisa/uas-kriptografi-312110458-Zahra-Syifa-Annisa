import numpy as np

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def mod_inverse(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

def hill_cipher(text, key):
    key = np.array(key)
    if key.shape[0] != key.shape[1]:
        raise Exception('Key matrix must be square')
    
    n = key.shape[0]
    text = text.replace(" ", "").upper()
    
    while len(text) % n != 0:
        text += 'X'
    
    ciphertext = ''
    for i in range(0, len(text), n):
        block = text[i:i+n]
        block_indices = [ord(char) - ord('A') for char in block]
        block_vector = np.array(block_indices)
        result_vector = np.dot(key, block_vector) % 26
        result_block = ''.join([chr(result + ord('A')) for result in result_vector])
        ciphertext += result_block

    return ciphertext

def decrypt_hill_cipher(ciphertext, key):
    key = np.array(key)
    if key.shape[0] != key.shape[1]:
        raise Exception('Key matrix must be square')
    
    key_inverse = np.array([[mod_inverse(key[i][j], 26) for j in range(key.shape[1])] for i in range(key.shape[0])])

    n = key.shape[0]
    text = ''
    for i in range(0, len(ciphertext), n):
        block = ciphertext[i:i+n]
        block_indices = [ord(char) - ord('A') for char in block]
        block_vector = np.array(block_indices)
        result_vector = np.dot(key_inverse, block_vector) % 26
        result_block = ''.join([chr(result + ord('A')) for result in result_vector])
        text += result_block

    return text

# Contoh penggunaan
key = [[6, 24, 1], [13, 16, 10], [20, 17, 15]]
plaintext = "HELLOHILL"
encrypted_text = hill_cipher(plaintext, key)
print("Teks Terenkripsi:", encrypted_text)

decrypted_text = decrypt_hill_cipher(encrypted_text, key)
print("Teks Terdekripsi:", decrypted_text)
