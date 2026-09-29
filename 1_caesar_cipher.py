"""Aplikasi 1 - Caesar Cipher (GUI Tkinter). Jalankan: python 1_caesar_cipher.py"""
import tkinter as tk
from tkinter import ttk, messagebox


def caesar(text, shift, decrypt=False):
    if decrypt:
        shift = -shift
    out = []
    for ch in text:
        if ch.isascii() and ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            out.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            out.append(ch)
    return ''.join(out)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Caesar Cipher")
        self.geometry("520x460")
        pad = {"padx": 10, "pady": 4}

        ttk.Label(self, text="Teks input:").pack(anchor="w", **pad)
        self.inp = tk.Text(self, height=7)
        self.inp.pack(fill="x", **pad)

        row = ttk.Frame(self)
        row.pack(fill="x", **pad)
        ttk.Label(row, text="Kunci (geser 0-25):").pack(side="left")
        self.shift = tk.IntVar(value=3)
        ttk.Spinbox(row, from_=0, to=25, textvariable=self.shift, width=5).pack(side="left", padx=8)

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
            s = int(self.shift.get())
        except (tk.TclError, ValueError):
            return messagebox.showerror("Error", "Kunci harus berupa angka.")
        text = self.inp.get("1.0", "end-1c")
        self.out.delete("1.0", "end")
        self.out.insert("1.0", caesar(text, s, decrypt))

    def clear(self):
        self.inp.delete("1.0", "end")
        self.out.delete("1.0", "end")


if __name__ == "__main__":
    App().mainloop()
