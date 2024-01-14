# Fungsi untuk menemukan invers modular
def modInverse(a, m):
    m0 = m
    y = 0
    x = 1

    if m == 1:
        return 0

    while a > 1:
        q = a // m
        t = m

        m = a % m
        a = t
        t = y

        y = x - q * y
        x = t

    if x < 0:
        x = x + m0

    return x

# Fungsi untuk mengenkripsi pesan
def encrypt(text, key):
    result = ""

    # Mengambil nilai a dan b dari kunci
    a = key[0]
    b = key[1]

    for char in text:
        if char.isalpha():
            # Mengenkripsi hanya huruf alfabet
            if char.islower():
                result += chr(((a * (ord(char) - ord('a')) + b) % 26) + ord('a'))
            else:
                result += chr(((a * (ord(char) - ord('A')) + b) % 26) + ord('A'))
        else:
            result += char

    return result

# Fungsi untuk mendekripsi pesan
def decrypt(text, key):
    result = ""
    
    a = key[0]
    b = key[1]
    a_inv = modInverse(a, 26) # Menghitung invers modular dari a

    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr(((a_inv * (ord(char) - ord('a') - b)) % 26) + ord('a'))
            else:
                result += chr(((a_inv * (ord(char) - ord('A') - b)) % 26) + ord('A'))
        else:
            result += char

    return result

# Contoh penggunaan
pesan = "Ini adalah pesan rahasia"
kunci = (5, 7)  # Nilai a dan b

pesan_terenkripsi = encrypt(pesan, kunci)
pesan_terdekripsi = decrypt(pesan_terenkripsi, kunci)

print("Pesan Asli:", pesan)
print("Pesan Terenkripsi:", pesan_terenkripsi)
print("Pesan Terdekripsi:", pesan_terdekripsi)
