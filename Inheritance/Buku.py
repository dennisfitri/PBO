class Buku:
	def inputData(self):
		print("Masukkan data buku:")
		self.judul = str(input("Judul buku 	:"))
		self.tahun_terbit = str(input("Tahun terbit 	:"))
		self.nama_pengarang = str(input("Nama pengarang 	:"))
		self.penerbit = str(input("Penerbit 	:"))

	def dispData(self):
		print ("="*30)
		print("Judul 		:", self.judul)
		print("Tahun terbit 	:", self.tahun_terbit)
		print("Nama pengarang 	:", self.nama_pengarang)
		print("Penerbit 	:", self.penerbit)

