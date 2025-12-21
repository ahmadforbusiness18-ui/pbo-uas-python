class MataKuliah:
    def __init__(self, kode, nama):
        self.kode = kode
        self.nama = nama

    def __str__(self):
        return f"{self.kode} -  {self.nama}"

    def tampil(self):
        return f"Kode: {self.kode} | Nama: {self.nama}"