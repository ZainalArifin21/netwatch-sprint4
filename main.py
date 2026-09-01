# ================================================================
# PROYEK: SMKN1 Net-Watch (Sprint4)
# Deskripsi: Program Input Data Identitas & Parameter Perangkat
# ================================================================

print("=========================================")
print("  FORM INPUT DATA UTAMA SMKN1 NET-WATCH  ")
print("=========================================")

# 1. Menangkap Input Teks (String)
nama_operator = input("Masukkan Nama Operator/Siswa : ")
nama_perangkat = input("Masukkan Nama Perangkat Jaringan : ")
ip_address = input("Masukkan Alamat IP (IP Address) : ")

# 2. Menangkap Input Angka & Konversi Tipa Data (Type Casting)
jumlah_port = int(input("Masukkan Jumlah Port Router  :  "))
kecepatan_link = float(input("Masukkan Kecepatan Bandwith(Mbps):  "))

# 3. Variabel Boolean Default
status_aktif = True

print("\n-------------------------------------------")
print("  HASIL INISIALISASI MONITORING JARINGAN  ")
print("---------------------------------------------")
print("Operator Sistem :", nama_operator)
print("Nama Perangkat  :", nama_perangkat)
print("IP Address      :", ip_address)
print("Total Port      :", jumlah_port, "Port")
print("Bandwith Rate   :", kecepatan_link, "Mbps")
print("Status Monitor  :", status_aktif)
print("==============================================")

# 4. Memeriksa Tipe Data di Memori
print("\n[ANALISIS MEMORI SISTEM]")
print("Tipe data nama_operator :", type(nama_operator))
print("Tipe data jumlah_port    :", type(jumlah_port))
print("Tipe data kecepatan_link :", type(kecepatan_link))
