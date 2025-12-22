from matakuliah import MataKuliah
from nilai import Nilai

class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama

    def tampil(self):
        return f"NIM: {self.nim} | Nama: {self.nama}"

# data
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
            print("⚠️ Data mahasiswa atau mata kuliah belum tersedia, silahkan input terlebih dahulu")
            continue

        print("\nDaftar Mahasiswa:")
        for i, mhs in enumerate(daftar_mahasiswa):
            print(f"{i}. {mhs.tampil()}")

        idx_mhs = int(input("Pilih nomor mahasiswa: "))

        print("\nDaftar Mata Kuliah:")
        for i, mk in enumerate(daftar_matakuliah):
            print(f"{i}. {mk.tampil()}")

        idx_mk = int(input("Pilih nomor mata kuliah: "))
        presence = int(input("Masukkan Niai Kehadiran (0-100): "))
        n_tugas = int(input("Masukkan Nilai Tugas (0-100): "))
        n_uts = int(input("Masukkan Nilai UTS (0-100): "))
        n_uas = int(input("Masukkan Nilai UAS (0-100): "))
        print("Jumlah Nilai: ", (presence + n_tugas + n_uts + n_uas)/4)
        nilai_total = int((presence + n_tugas + n_uts + n_uas)/4)

        daftar_nilai.append(
            Nilai(daftar_mahasiswa[idx_mhs], daftar_matakuliah[idx_mk], nilai_total)
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
        print("❌ Pilihan tidak valid, pilih ulang")
