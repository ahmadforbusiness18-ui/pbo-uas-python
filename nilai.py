class Nilai:
    def __init__(self, mahasiswa, matakuliah, nilai):
        self.mahasiswa = mahasiswa
        self.matakuliah = matakuliah
        self.nilai = nilai

    def tampil(self):
        return f"Mahasiswa: {self.mahasiswa.nama} | Mata Kuliah: {self.matakuliah.nama} | Nilai: {self.nilai}"
