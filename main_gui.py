# ================================================================
# PROYEK: SMKN1 Net-Watch (Sprint4) - GUI
# Deskripsi: Program Modular Python dengan Tkinter
# ================================================================

import tkinter as tk
from tkinter import messagebox
import sqlite3

from ganjil_genap import cek_ganjil_genap
from persegi_panjang import hitung_luas


# ================================================================
# DATABASE
# ================================================================

def login_gui():
    username = entry_username.get()
    password = entry_password.get()

    if username == "" or password == "":
        messagebox.showwarning("Peringatan", "Username dan password harus diisi!")
        return

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?",
        (username, password)
    )

    user = cursor.fetchone()

    conn.close()

    if user:
        messagebox.showinfo("Login Berhasil", "Login berhasil!")
        window_login.destroy()
        buka_menu_utama()
    else:
        messagebox.showerror("Login Gagal", "Username atau password salah!")


def registrasi_gui():
    username = entry_username.get()
    password = entry_password.get()

    if username == "" or password == "":
        messagebox.showwarning("Peringatan", "Username dan password harus diisi!")
        return

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password)
        )

        conn.commit()
        messagebox.showinfo("Registrasi Berhasil", "Akun berhasil dibuat!")

        entry_username.delete(0, tk.END)
        entry_password.delete(0, tk.END)

    except sqlite3.IntegrityError:
        messagebox.showerror("Registrasi Gagal", "Username sudah digunakan!")

    conn.close()


# ================================================================
# PROGRAM GANJIL / GENAP
# ================================================================

def buka_ganjil_genap():

    window = tk.Toplevel()
    window.title("Cek Ganjil / Genap")
    window.geometry("450x300")

    tk.Label(
        window,
        text="PROGRAM MENENTUKAN GANJIL ATAU GENAP",
        font=("Arial", 14, "bold")
    ).pack(pady=20)

    tk.Label(
        window,
        text="Masukkan angka:"
    ).pack()

    entry_angka = tk.Entry(window)
    entry_angka.pack(pady=10)

    hasil = tk.Label(
        window,
        text="Hasil akan muncul di sini",
        font=("Arial", 12)
    )
    hasil.pack(pady=10)

    def cek_angka():

        try:
            angka = int(entry_angka.get())

            if angka % 2 == 0:
                hasil.config(text="Hasil: Angka tersebut adalah GENAP")
            else:
                hasil.config(text="Hasil: Angka tersebut adalah GANJIL")

        except ValueError:
            messagebox.showerror(
                "Error",
                "Masukkan angka yang valid!"
            )

    tk.Button(
        window,
        text="Cek Angka",
        command=cek_angka
    ).pack(pady=10)

    tk.Button(
        window,
        text="Tutup",
        command=window.destroy
    ).pack()


# ================================================================
# PROGRAM LUAS PERSEGI PANJANG
# ================================================================

def buka_persegi_panjang():

    window = tk.Toplevel()
    window.title("Luas Persegi Panjang")
    window.geometry("450x350")

    tk.Label(
        window,
        text="MENGHITUNG LUAS PERSEGI PANJANG",
        font=("Arial", 14, "bold")
    ).pack(pady=20)

    tk.Label(
        window,
        text="Panjang:"
    ).pack()

    entry_panjang = tk.Entry(window)
    entry_panjang.pack(pady=5)

    tk.Label(
        window,
        text="Lebar:"
    ).pack()

    entry_lebar = tk.Entry(window)
    entry_lebar.pack(pady=5)

    hasil = tk.Label(
        window,
        text="Hasil akan muncul di sini",
        font=("Arial", 12)
    )
    hasil.pack(pady=15)

    def hitung():

        try:
            panjang = float(entry_panjang.get())
            lebar = float(entry_lebar.get())

            luas = panjang * lebar

            hasil.config(
                text=f"Luas = {luas}"
            )

        except ValueError:
            messagebox.showerror(
                "Error",
                "Panjang dan lebar harus berupa angka!"
            )

    tk.Button(
        window,
        text="Hitung Luas",
        command=hitung
    ).pack(pady=10)

    tk.Button(
        window,
        text="Tutup",
        command=window.destroy
    ).pack()


# ================================================================
# MENU UTAMA
# ================================================================

def buka_menu_utama():

    global window_menu

    window_menu = tk.Tk()
    window_menu.title("SMKN1 Net-Watch")
    window_menu.geometry("500x400")

    tk.Label(
        window_menu,
        text="PROGRAM MODULAR SMKN1 NET-WATCH",
        font=("Arial", 16, "bold")
    ).pack(pady=30)

    tk.Button(
        window_menu,
        text="1. Cek Ganjil / Genap",
        width=30,
        command=buka_ganjil_genap
    ).pack(pady=10)

    tk.Button(
        window_menu,
        text="2. Hitung Luas Persegi Panjang",
        width=30,
        command=buka_persegi_panjang
    ).pack(pady=10)

    tk.Button(
        window_menu,
        text="3. Keluar",
        width=30,
        command=window_menu.destroy
    ).pack(pady=10)

    window_menu.mainloop()


# ================================================================
# MENU LOGIN
# ================================================================

window_login = tk.Tk()

window_login.title("Login - SMKN1 Net-Watch")
window_login.geometry("450x350")

tk.Label(
    window_login,
    text="SMKN1 NET-WATCH",
    font=("Arial", 18, "bold")
).pack(pady=25)

tk.Label(
    window_login,
    text="Username"
).pack()

entry_username = tk.Entry(window_login, width=30)
entry_username.pack(pady=5)

tk.Label(
    window_login,
    text="Password"
).pack()

entry_password = tk.Entry(
    window_login,
    width=30,
    show="*"
)
entry_password.pack(pady=5)

tk.Button(
    window_login,
    text="Login",
    width=20,
    command=login_gui
).pack(pady=15)

tk.Button(
    window_login,
    text="Registrasi",
    width=20,
    command=registrasi_gui
).pack()

tk.Button(
    window_login,
    text="Keluar",
    width=20,
    command=window_login.destroy
).pack(pady=10)

window_login.mainloop()