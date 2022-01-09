import Polygon as p

#menyatakan bahwa kelas Segiempat merupakan kelas anak dari kelas Polygon
class Segiempat(p.Polygon):
	def __init__(self):
		p.Polygon.__init__(self,4)
		print("Segiempat")

	def hitungKeliling(self):
		a,b,c,d = self.sisi
		k = a+b+c+d 
		print("Keliling Segiempat adalah", k, "cm")

	def inputSisi(self):
		print("Hello world")