# ================================================================
# PROYEK: SMKN1 Net-Watch (Sprint4)
# Deskripsi: Program Modular Python
# ================================================================

from ganjil_genap import cek_ganjil_genap
from persegi_panjang import hitung_luas

def program_ganjil_genap():
    print("\n======================================")
    print("   PROGRAM MENENTUKAN GANJIL ATAU GENAP")
    print("=======================================")

    while True:
        input_angka = input("Masukkan angka (ketik `exit` untuk keluar): ")

        if input_angka.lower() == "exit":
            print("Program Selesai.")
            break 

        angka = int(input_angka)

        cek_ganjil_genap(angka)

    
def main():
    while True:
        print("\n======================================")
        print("   PROGRAM MODULAR SMKN1 NET-WATCH")
        print("========================================")
        print("1. Cek Ganjil / Genap")
        print("2. Hitung Luas Persegi Panjang")
        print("3. Keluar")
        print("========================================")

        pilihan = input("Pilih program (1/2/3): ")

        if pilihan == "1":
            program_ganjil_genap()

        elif pilihan == "2":
            hitung_luas()

        elif pilihan == "3":
            print("Program selesai.")
            break 


        else:
            print("Pilihan tidak tersedia.")



main()
