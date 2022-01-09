import Buku as b

class Komik(b.Buku):
	def inputDataKomik(self):
		print("Komik")
		b.Buku.inputData(self)
		self.genre = input("Genre :")
		self.episode = input("Episode :")
		self.ilustrator = input("Ilustrator :")
		self.harga = input("Harga :")

	def dispKomik(self):
		print ("="*30)
		print("Judul 		:", self.judul)
		print("Tahun terbit 	:", self.tahun_terbit)
		print("Nama pengarang 	:", self.nama_pengarang)
		print("Penerbit 	:", self.penerbit)
		print("Genre 		:", self.genre)
		print("Episode		:", self.episode)
		print("Ilustrator 	:", self.ilustrator)
		print("Harga 		:", self.harga)
		print()

class Buku_pelajaran(b.Buku):
	def __init__ (self) :
		b.Buku.inputData(self)
		print("Buku pelajaran")
	