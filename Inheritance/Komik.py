import Buku as b

class Komik(b.Buku):
	def inputDataKomik(self):
		print("Komik")
		b.Buku.inputData(self)
		self.genre = input("Genre 		:")
		self.episode = input("Episode 	:")
		self.ilustrator = input("Ilustrator 	:")
		self.jmlHalaman = int(input("Jumlah halaman	:"))

	def dispKomik(self):
		print ("-"*50)
		print("Judul 		:", self.judul)
		print("Tahun terbit 	:", self.tahun_terbit)
		print("Nama pengarang 	:", self.nama_pengarang)
		print("Penerbit 	:", self.penerbit)
		print("Genre 		:", self.genre)
		print("Episode		:", self.episode)
		print("Ilustrator 	:", self.ilustrator)
		print("Jumlah halaman 	:", self.jmlHalaman, "halaman")
		print()
	