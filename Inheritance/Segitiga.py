import Polygon as p

#menyatakan bahwa kelas Segitiga merupakan kelas anak dari kelas Polygon
class Segitiga(p.Polygon):
	def __init__(self):
		p.Polygon.__init__(self,3)
		print("Segitiga")

	def hitungLuas(self):
		a,b,c = self.sisi
		if a>c and a>b :
			l = 0.5*b*c
			print("Luas Segitiga adalah", l, "cm^2")
		elif b>a and b>c :
			l = 0.5*a*c
			print("Luas Segitiga adalah", l, "cm^2")
		elif c>a and c>b :
			l = 0.5*a*b
			print("Luas Segitiga adalah", l, "cm^2")
		else :
			print("Bukan Segitiga siku - siku" )	