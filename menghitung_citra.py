# -*- coding: utf-8 -*-
"""312110458-Zahra Syifa Annisa-Menghitung Citra

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OaL4NGCcumpuHIgY9cwgfaCjocMUcKKe
"""

from google.colab import files
from PIL import Image
import cv2
import numpy as np
import io
import matplotlib.pyplot as plt

# Meminta pengguna untuk mengunggah file
uploaded = files.upload()

# Ambil nama file gambar dari dictionary 'uploaded'
# Gantilah 'nama_gambar.jpg' dengan nama file yang sesuai
nama_file_gambar = list(uploaded.keys())[0]

# Baca gambar dari objek byte
gambar_byte = uploaded['panda.jpg']

# Konversi objek byte menjadi objek gambar menggunakan PIL
gambar = Image.open(io.BytesIO(gambar_byte))

# Konversi gambar PIL menjadi array NumPy
gambar_array = np.array(gambar)

# Menampilkan informasi dan nilai piksel dari gambar
print(f"Informasi Gambar {'panda.jpg'}:")
print(f"Ukuran Gambar: {gambar.size}")
print(f"Mode Gambar: {gambar.mode}")
print(f"Nilai Piksel Gambar (beberapa contoh):")
print(gambar_array[:5, :5, :])  # Menampilkan beberapa piksel pertama sebagai contoh

# Membuat subplot dengan 1 baris dan 2 kolom untuk menampilkan gambar secara horizontal
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

# Menampilkan gambar asli di subplot pertama
axs[0].imshow(gambar_array)
axs[0].axis('off')
axs[0].set_title('Gambar Asli')

# Contoh pengolahan citra sederhana: Merubah ke citra keabuan (grayscale)
gambar_keabuan = cv2.cvtColor(gambar_array, cv2.COLOR_BGR2GRAY)

# Menampilkan gambar keabuan di subplot kedua
axs[1].imshow(gambar_keabuan, cmap='gray')
axs[1].axis('off')
axs[1].set_title('Gambar Keabuan')

# Menyusun subplot secara horizontal
plt.show()