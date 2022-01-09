import Buku as b

class Majalah(b.Buku):
	def inputDataMajalah (self) :
		print("Majalah")
		b.Buku.inputData(self)
		self.edisi = input ("Edisi		:")
		self.genre = input("Genre 		:")
		self.harga = input("Harga		:")
		self.jmlHalaman = input("Jumlah halaman	:")

	def dispDataMajalah (self) :
		b.Buku.dispData(self)
		print("Edisi 		:", self.edisi)
		print("Genre 		:", self.genre)
		print("Harga 		:", self.harga)
		print("Jumlah halaman 	:", self.jmlHalaman, "halaman")
		print()