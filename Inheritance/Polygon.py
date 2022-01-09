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


