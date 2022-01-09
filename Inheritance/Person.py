class Person  :
	def inputData(self):
		self.nik = str(input("NIK :"))
		self.tinggiBadan = int(input("Tinggi badan (dalam cm) :"))
		self.nama = str(input("Nama :"))
		self.jenisKelamin = str(input("Jenis kelamin :"))
		self.tempatLahir = str(input("Tempat lahir :"))
		self.tanggalLahir = str(input("Tanggal lahir :"))
		self.golonganDarah = str(input("Golongan darah :"))
		self.beratBadan = int(input("Berat badan (dalam kg) :"))
		self.alamat	= str(input("Alamat :"))

	def tampilData(self) :
		print ("NIK		:", self.nik)
		print ("Tinggi badan	:", self.tinggiBadan)
		print ("Nama		:", self.nama)
		print ("Jenis kelamin	:", self.jenisKelamin)
		print ("Tempat lahir 	:", self.tempatLahir)
		print ("Tanggal lahir	:", self.tanggalLahir)
		print ("Golongan darah	:", self.golonganDarah)
		print ("Berat badan	:", self.beratBadan)
		print ("Alamat		:", self.alamat)

