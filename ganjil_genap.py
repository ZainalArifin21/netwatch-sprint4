print("==================================================================")
print("  PROGRAM MENENTUKAN NILAI ANGKA ADALAH GANJIL ATAU GENAP  ")
print("==================================================================")

while True:
    input_angka = input("Masukkan angka (ketik `exit` untuk keluar): )")

    if input_angka.lower() == "exit":
        print("Program selesai.")
        break

    angka = int(input_angka)

    if angka % 2 == 0:
            print("angka tersebut adalah Genap")
    else:
            print("angka tersebut adalah Ganjil")
