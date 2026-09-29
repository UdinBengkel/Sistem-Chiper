"""Aplikasi 2 - Vigenere Cipher (GUI Tkinter). Jalankan: python 2_vigenere_cipher.py"""
import tkinter as tk
from tkinter import ttk, messagebox


def vigenere(text, key, decrypt=False):
    k = [ord(c) - 65 for c in key.upper() if c.isascii() and c.isalpha()]
    if not k:
        raise ValueError("Kunci harus berisi minimal satu huruf (A-Z).")
    out, i = [], 0
    for ch in text:
        if ch.isascii() and ch.isalpha():
            s = -k[i % len(k)] if decrypt else k[i % len(k)]
            i += 1
            base = ord('A') if ch.isupper() else ord('a')
            out.append(chr((ord(ch) - base + s) % 26 + base))
        else:
            out.append(ch)
    return ''.join(out)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Vigenere Cipher")
        self.geometry("520x460")
        pad = {"padx": 10, "pady": 4}

        ttk.Label(self, text="Teks input:").pack(anchor="w", **pad)
        self.inp = tk.Text(self, height=7)
        self.inp.pack(fill="x", **pad)

        row = ttk.Frame(self)
        row.pack(fill="x", **pad)
        ttk.Label(row, text="Kunci (huruf):").pack(side="left")
        self.key = ttk.Entry(row)
        self.key.pack(side="left", fill="x", expand=True, padx=8)

        btns = ttk.Frame(self)
        btns.pack(fill="x", **pad)
        ttk.Button(btns, text="Enkripsi", command=lambda: self.run(False)).pack(side="left", expand=True, fill="x", padx=2)
        ttk.Button(btns, text="Dekripsi", command=lambda: self.run(True)).pack(side="left", expand=True, fill="x", padx=2)
        ttk.Button(btns, text="Bersihkan", command=self.clear).pack(side="left", expand=True, fill="x", padx=2)

        ttk.Label(self, text="Hasil:").pack(anchor="w", **pad)
        self.out = tk.Text(self, height=7)
        self.out.pack(fill="x", **pad)

    def run(self, decrypt):
        try:
            res = vigenere(self.inp.get("1.0", "end-1c"), self.key.get(), decrypt)
        except ValueError as e:
            return messagebox.showerror("Error", str(e))
        self.out.delete("1.0", "end")
        self.out.insert("1.0", res)

    def clear(self):
        self.inp.delete("1.0", "end")
        self.out.delete("1.0", "end")
        self.key.delete(0, "end")


if __name__ == "__main__":
    App().mainloop()
