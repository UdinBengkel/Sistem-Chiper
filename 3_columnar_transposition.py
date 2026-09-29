"""Aplikasi 3 - Columnar Transposition Cipher (GUI Tkinter).
Jalankan: python 3_columnar_transposition.py

Aturan (sesuai materi kuliah):
- Spasi dan simbol dibuang, hanya huruf yang diproses.
- Plainteks ditulis per baris sebanyak panjang kunci, lalu dibaca per kolom
  sesuai urutan alfabet huruf kunci (contoh: TOMBAK -> 6 5 4 2 1 3).
- Jika baris terakhir kurang, ditambah huruf dummy X.
"""
import tkinter as tk
from tkinter import ttk, messagebox


def clean(text):
    return ''.join(c for c in text.upper() if c.isascii() and c.isalpha())


def col_order(key):
    """Urutan indeks kolom yang dibaca (huruf kembar: kiri dulu)."""
    return sorted(range(len(key)), key=lambda i: (key[i], i))


def encrypt(text, key):
    key = clean(key)
    if not key:
        raise ValueError("Kunci harus berisi minimal satu huruf.")
    t = clean(text)
    n = len(key)
    t += 'X' * (-len(t) % n)
    return ''.join(t[c::n] for c in col_order(key))


def decrypt(text, key):
    key = clean(key)
    if not key:
        raise ValueError("Kunci harus berisi minimal satu huruf.")
    c = clean(text)
    n = len(key)
    if len(c) % n:
        raise ValueError(f"Panjang cipherteks ({len(c)}) harus kelipatan panjang kunci ({n}).")
    rows = len(c) // n
    cols = {}
    for j, idx in enumerate(col_order(key)):
        cols[idx] = c[j * rows:(j + 1) * rows]
    return ''.join(cols[i][r] for r in range(rows) for i in range(n)).lower()


def grid(text, key):
    """Tabel penulisan plainteks per baris (untuk ditampilkan)."""
    key = clean(key)
    if not key:
        return ""
    t = clean(text)
    n = len(key)
    t += 'X' * (-len(t) % n)
    order = col_order(key)
    rank = {idx: k + 1 for k, idx in enumerate(order)}
    lines = [' '.join(str(rank[i]) for i in range(n)), ' '.join(key)]
    lines += [' '.join(t[r:r + n]) for r in range(0, len(t), n)]
    return '\n'.join(lines)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Columnar Transposition Cipher")
        self.geometry("520x620")
        pad = {"padx": 10, "pady": 4}

        ttk.Label(self, text="Teks input:").pack(anchor="w", **pad)
        self.inp = tk.Text(self, height=6)
        self.inp.pack(fill="x", **pad)

        row = ttk.Frame(self)
        row.pack(fill="x", **pad)
        ttk.Label(row, text="Kunci (kata):").pack(side="left")
        self.key = ttk.Entry(row)
        self.key.pack(side="left", fill="x", expand=True, padx=8)

        btns = ttk.Frame(self)
        btns.pack(fill="x", **pad)
        ttk.Button(btns, text="Enkripsi", command=lambda: self.run(False)).pack(side="left", expand=True, fill="x", padx=2)
        ttk.Button(btns, text="Dekripsi", command=lambda: self.run(True)).pack(side="left", expand=True, fill="x", padx=2)
        ttk.Button(btns, text="Bersihkan", command=self.clear).pack(side="left", expand=True, fill="x", padx=2)

        ttk.Label(self, text="Tabel transposisi (saat enkripsi):").pack(anchor="w", **pad)
        self.grid_lbl = ttk.Label(self, text="", font=("Courier", 12), justify="left")
        self.grid_lbl.pack(anchor="w", **pad)

        ttk.Label(self, text="Hasil:").pack(anchor="w", **pad)
        self.out = tk.Text(self, height=6)
        self.out.pack(fill="x", **pad)

    def run(self, dec):
        text, key = self.inp.get("1.0", "end-1c"), self.key.get()
        try:
            res = decrypt(text, key) if dec else encrypt(text, key)
        except ValueError as e:
            return messagebox.showerror("Error", str(e))
        self.grid_lbl.config(text="" if dec else grid(text, key))
        self.out.delete("1.0", "end")
        self.out.insert("1.0", res)

    def clear(self):
        self.inp.delete("1.0", "end")
        self.out.delete("1.0", "end")
        self.key.delete(0, "end")
        self.grid_lbl.config(text="")


if __name__ == "__main__":
    App().mainloop()
