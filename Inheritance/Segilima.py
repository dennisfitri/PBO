import Polygon as p

#menyatakan bahwa kelas Segilima merupakan kelas anak dari kelas Polygon
class Segilima(p.Polygon):
	def __init__(self):
		p.Polygon.__init__(self,5)
		print("Segilima")

	def hitungKeliling(self):
		a,b,c,d,e = self.sisi
		k = a+b+c+d+e 
		print("Keliling Segilima adalah", k, "cm")