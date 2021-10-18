import BangunRuang as b
import math

class Tabung(b.bangunRuang):
	def __init__ (self):
		super(b.bangunRuang, self).__init__()
		self.r = 14 #float(input("Jari - jari (dalam cm)  :"))
		self.tinggi = 35 #float(input("Tinggi (dalam cm) 	:"))

	def volume (self):
		self.luasAlas =  math.pi*self.r**2
		self.volume = self.luasAlas*self.tinggi
		return self.volume
		
	def dispTabung (self):
		print ("Volume Tabung 		:", self.volume, "cm^3")
		print()