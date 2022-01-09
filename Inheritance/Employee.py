import Person as p

class Employee(p.Person) :
	def inputDataEmployee(self):
		p.Person.inputData(self)
		self.idEmployee = str(input("ID Employee :"))
		self.pekerjaan = str(input("Pekerjaan :"))
		self.gaji = int(input("Gaji :")) 
		self.tahunMasuk = int(input("Tahun masuk:"))
		self.status = str(input("Status :"))

	def tampilDataEmployee(self) :
		print ("-"*40)
		p.Person.tampilData(self)
		print ("ID Employee	:", self.idEmployee)
		print ("Pekerjaan	:", self.pekerjaan)
		print ("Gaji		:", self.gaji)
		print ("Tahun masuk	:", self.tahunMasuk)
		print ("Status		:", self.status)

	def hitungMasaKerja(self) :
		tahun = 2021 - self.tahunMasuk
		print ("Masa kerja 	:", tahun)
		print()