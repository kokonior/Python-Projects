class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
        self.hitung_luas()
        self.hitung_keliling()
    def hitung_luas(self):
        self.luas = self.panjang * self.lebar
    def hitung_keliling(self):
        self.keliling = 2 * (self.panjang + self.lebar)
    def ubah_panjang(self, nilai):
        self.panjang = nilai
        self.hitung_luas()
        self.hitung_keliling()
    def ubah_lebar(self, nilai):
        self.lebar = nilai
        self.hitung_luas()
        self.hitung_keliling()

pp = PersegiPanjang(10, 7)
pp.ubah_panjang(9)
print(
    pp.panjang,
    pp.lebar,
    pp.luas,
    pp.keliling
)
