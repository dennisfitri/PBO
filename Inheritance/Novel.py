import Buku as b

class Novel(b.Buku):
	def inputDataNovel (self) :
		print("Novel")
		b.Buku.inputData(self)
		self.tema = input ("Tema 		:")
		self.genre = input("Genre 		:")
		self.harga = input("Harga		:")
		self.jmlHalaman = input("Jumlah halaman	:")

	def dispDataNovel (self) :
		b.Buku.dispData(self)
		print("Tema 		:", self.tema)
		print("Genre 		:", self.genre)
		print("Harga 		:", self.harga)
		print("Jumlah halaman 	:", self.jmlHalaman, "halaman")
		print()
	