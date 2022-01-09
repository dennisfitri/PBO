class Polygon:
	def __init__(self, banyak_sisi):
		self.n = banyak_sisi
		self.sisi = [0 for i in range(banyak_sisi)]

	def inputSisi(self):
		print("Masukkan panjang sisi (dalam cm):")
		self.sisi = [float(input("Sisi"+str(i+1)+":")) for i in range (self.n)]
		print()

	def dispSisi(self):
		for i in range (self.n):
			print("Panjang sisi",i+1, "adalah", self.sisi[i], "cm")

class segiEmpat(Polygon):
	sisi1 = Polygon()
	sisi1.inputSisi()
	def __init__(self):
		Polygon.__init__(self,4)
		print("Segiempat")

	def hitungKeliling(self):
		a,b,c,d = self.sisi
		k = a+b+c+d 
		print("Keliling Segiempat adalah",k,"cm.")

	keliling = segiEmpat()
	keliling.hitungKeliling()