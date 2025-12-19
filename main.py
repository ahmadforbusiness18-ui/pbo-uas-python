from matakuliah import MataKuliah
from nilai import Nilai


class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama

    def tampil(self):
        return f"NIM: {self.nim} | Nama: {self.nama}"

daftar_mahasiswa = []
daftar_matakuliah = []
daftar_nilai = []

def menu():
    print("\n===== Sistem Informasi Akademik =====")
    print("1. Tambah Mahasiswa")
    print("2. Tambah Mata Kuliah")
    print("3. Input Nilai")
    print("4. Tampilkan Data")
    print("5. Keluar")

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama Mahasiswa: ")
        daftar_mahasiswa.append(Mahasiswa(nim, nama))
        print("✅ Mahasiswa berhasil ditambahkan")

    elif pilihan == "2":
        kode = input("Masukkan Kode Mata Kuliah: ")
        nama = input("Masukkan Nama Mata Kuliah: ")
        daftar_matakuliah.append(MataKuliah(kode, nama))
        print("✅ Mata kuliah berhasil ditambahkan")

    elif pilihan == "3":
        if not daftar_mahasiswa or not daftar_matakuliah:
            print("⚠️ Data mahasiswa atau mata kuliah belum tersedia")
            continue

        print("\nDaftar Mahasiswa:")
        for i, mhs in enumerate(daftar_mahasiswa):
            print(f"{i}. {mhs.tampil()}")

        idx_mhs = int(input("Pilih nomor mahasiswa: "))

        print("\nDaftar Mata Kuliah:")
        for i, mk in enumerate(daftar_matakuliah):
            print(f"{i}. {mk.tampil()}")

        idx_mk = int(input("Pilih nomor mata kuliah: "))
        nilai = input("Masukkan Nilai: ")

        daftar_nilai.append(
            Nilai(daftar_mahasiswa[idx_mhs], daftar_matakuliah[idx_mk], nilai)
        )

        print("✅ Nilai berhasil disimpan")

    elif pilihan == "4":
        print("\n=== Data Nilai Mahasiswa ===")
        if not daftar_nilai:
            print("Belum ada data nilai")
        else:
            for n in daftar_nilai:
                print(n.tampil())

    elif pilihan == "5":
        print("👋 Terima kasih, program selesai")
        break

    else:
        print("❌ Pilihan tidak valid")
