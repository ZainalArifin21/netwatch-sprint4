import sqlite3

def login():
    username =input("Username: ")
    password =input("Password: ")

    koneksi = sqlite3.connect("database.db")
    cursor = koneksi.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?",
        (username, password)
    )

    data = cursor.fetchone()

    if data:
        print("Login berhasil!")
        koneksi.close()
        return True
    else:
        print("Username atau password salah!")
        koneksi.close()
        return False 


def registrasi():
    username = input("Buat username: ")
    password = input("Buat password: ")

    koneksi = sqlite3.connect("database.db")
    cursor = koneksi.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password)
        )

        koneksi.commit()
        print("Registrasi berhasil!")

    except sqlite3.IntegrityError:
        print("Username sudah digunakan!")

    koneksi.close()
