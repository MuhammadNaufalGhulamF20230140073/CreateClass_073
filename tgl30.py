class PersegiPanjang:
    def __init__(self, panjang, lebar): #Konstruktor untuk menginisialisasi panjang dan lebar.
        self.panjang = panjang
        self.lebar = lebar

    def hitung_keliling(self): #Fungsi untuk menghitung keliling persegi panjang.
        return 2 * (self.panjang + self.lebar)

    def hitung_luas(self): #Fungsi untuk menghitung luas persegi panjang.
        return self.panjang * self.lebar

    def __str__(self): #Fungsi untuk menampilkan string objek.
        return f"Persegi panjang, panjang {self.panjang} cm, dan lebar nya {self.lebar} cm."


def main():
    try:
        Panjang=float(input("Masukkan Panjangnya ="))
        Lebar=float(input("Masukkan Lebarnya ="))
        if Panjang <=0 or Lebar <=0:
            print("")
            return
        PP=PersegiPanjang(Panjang,Lebar)
        print(PP)
        print("Keliling: ", PP.hitung_keliling())
        print("Luas: ", PP.hitung_luas())
    except ValueError:
        print("Nilai Harus Sesuai")
main()