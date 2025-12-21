class Nilai:
    def __init__(self, mahasiswa, matakuliah, nilai_total):
        self.mahasiswa = mahasiswa
        self.matakuliah = matakuliah
        self.nilai_total = nilai_total

    def tampil(self):
        return f"Mahasiswa: {self.mahasiswa.nama} | Mata Kuliah: {self.matakuliah.nama} | Nilai: {self.nilai_total}"
