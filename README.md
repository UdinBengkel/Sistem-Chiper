# Aplikasi Cipher Klasik (Python + Tkinter)

Tugas: membuat 3 aplikasi sistem cipher klasik dengan antarmuka GUI.

## Identitas

| | |
|---|---|
| Nama | Syafarudiansya (Yansa) |
| Kelas | I241A |
| NIM | 312410381 |
| Kampus | Universitas Pelita Bangsa |
| Mata Kuliah | _(isi nama mata kuliah)_ |

## Daftar Aplikasi

| No | File | Cipher | Jenis | Kunci |
|----|------|--------|-------|-------|
| 1 | `1_caesar_cipher.py` | Caesar Cipher | Substitusi (abjad-tunggal) | Angka geser 0-25 |
| 2 | `2_vigenere_cipher.py` | Vigenère Cipher | Substitusi (abjad-majemuk) | Kata (huruf A-Z) |
| 3 | `3_columnar_transposition.py` | Columnar Transposition | Transposisi | Kata (huruf A-Z) |

## Cara Menjalankan

Kebutuhan: **Python 3.8+**. Tkinter sudah termasuk di instalasi Python standar, tidak perlu `pip install`.

```bash
python 1_caesar_cipher.py
python 2_vigenere_cipher.py
python 3_columnar_transposition.py
```

> Linux (Ubuntu/Debian): jika muncul `No module named 'tkinter'`, jalankan `sudo apt install python3-tk`.

## Cara Menggunakan

1. Ketik pesan di kotak **Teks input**.
2. Isi **Kunci**.
3. Klik **Enkripsi** atau **Dekripsi**, hasil muncul di kotak **Hasil**.
4. Klik **Bersihkan** untuk mengosongkan semua isian.

## Cara Cek Aplikasi Berjalan Benar

Coba contoh berikut. Jika hasilnya sama, aplikasi berfungsi.

| Aplikasi | Input | Kunci | Hasil Enkripsi |
|----------|-------|-------|----------------|
| Caesar | `awasi asterix dan temannya obelix` | `3` | `dzdvl dvwhula gdq whpdqqbd rehola` |
| Caesar | `ADA RENCANA PENYELUNDUPAN NARKOBA DI BANDARA` | `5` | `FIF WJSHFSF UJSDJQZSIZUFS SFWPTGF IN GFSIFWF` |
| Vigenère | `kriptografiklasikdengancipheralfabetmajemuk` | `LAMPION` | `vruebctcarxszndiwsmbtlnoxxvrcaxuipremmymahv` |
| Vigenère | `she sells sea shells by the seashore` | `KEY` | `clc cijvw qoe qrijvw zi xfo wckwfyvc` |
| Columnar | `sistem dan teknologi informasi` | `TOMBAK` | `EEGRXTTOOXMKIMXSNLFIIAONSSDNIA` |

Untuk **dekripsi**, tempel hasil enkripsi ke kotak input dengan kunci yang sama. Pesan asli harus kembali.

## Penjelasan Singkat

### 1. Caesar Cipher
Setiap huruf digeser sejauh `k` posisi di alfabet.

- Enkripsi: `c = (p + k) mod 26`
- Dekripsi: `p = (c - k) mod 26`

Huruf besar/kecil dipertahankan, spasi dan simbol tidak diubah.

### 2. Vigenère Cipher
Cipher abjad-majemuk: setiap huruf digeser sesuai huruf kunci yang berulang.

- Enkripsi: `c = (p + k_i) mod 26`
- Dekripsi: `p = (c - k_i) mod 26`

Kunci hanya maju pada huruf, sedangkan spasi dan simbol dilewati.

### 3. Columnar Transposition Cipher
Cipher transposisi: plainteks ditulis per baris sebanyak panjang kunci, lalu dibaca per kolom sesuai urutan alfabet huruf kunci (contoh `TOMBAK` dibaca urutan 6 5 4 2 1 3 sesuai posisi alfabetnya).

- Spasi dan simbol dibuang, hanya huruf yang diproses.
- Jika baris terakhir kurang, ditambah huruf dummy `X`, sehingga hasil dekripsi bisa berakhiran `x`.
- Panjang cipherteks harus kelipatan panjang kunci saat dekripsi.

## Struktur Repositori

```
.
├── 1_caesar_cipher.py
├── 2_vigenere_cipher.py
├── 3_columnar_transposition.py
└── README.md
```

## Referensi

- Materi kuliah *Ragam Cipher Klasik (Bagian 1)*, IF4020 Kriptografi, Dr. Ir. Rinaldi Munir, M.T., Informatika ITB.
