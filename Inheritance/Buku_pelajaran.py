import Buku as b

class BukuPelajaran(b.Buku):
	def inputDataPelajaran (self) :
		print("Buku pelajaran")
		b.Buku.inputData(self)
		self.kelas = input ("Kelas 		:")
		self.kurikulum = input("Kurikulum 	:")
		self.harga = (input("Harga		:"))
		self.jmlHalaman = (input("Jumlah halaman	:"))

	def dispDataPelajaran (self) :
		b.Buku.dispData(self)
		print("Kelas 		:", self.kelas)
		print("Kurikulum 	:", self.kurikulum)
		print("Harga 		:", self.harga)
		print("Jumlah halaman 	:", self.jmlHalaman, "halaman")
		print()
		