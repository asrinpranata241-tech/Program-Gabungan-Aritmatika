# Program Evaluasi Mahasiswa

# 1. Input
tugas = float(input("Masukkan nilai tugas      : "))
uts = float(input("Masukkan nilai UTS        : "))
uas = float(input("Masukkan nilai UAS        : "))
kehadiran = float(input("Masukkan kehadiran (%)    : "))

# 2. Hitung nilai akhir (operator aritmatika)
nilai_akhir = (0.20 * tugas) + (0.30 * uts) + (0.50 * uas)

# 3. Evaluasi syarat (operator perbandingan, logika, dan modulus)
lulus = nilai_akhir >= 75 and kehadiran >= 80
genap = round(nilai_akhir) % 2 == 0
predikat = nilai_akhir >= 85 and kehadiran >= 90 and genap

# 4. Tentukan status (if, elif, else)
if predikat:
    status = "LULUS DENGAN PREDIKAT"
elif lulus:
    status = "LULUS"
else:
    status = "BELUM LULUS"

# 5. Tampilkan hasil
print(f"\nNilai Akhir : {nilai_akhir:.2f}")
print(f"Status      : {status}")
