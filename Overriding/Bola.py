import BangunRuang as b
import math

class Bola(b.bangunRuang):
	def __init__ (self):
		super(b.bangunRuang, self).__init__()
		self.r = 21 #float(input("Jari - jari (dalam cm)  :"))
		self.tinggi = 21 #float(input("Tinggi (dalam cm) 	:"))

	def volume(self):
		luasAlas = math.pi * self.r**2
		if self.r == self.tinggi:
			self.volume = 4/3 * luasAlas * self.tinggi
			print ("Volume Bola   		:", self.volume, "cm^3")
		else :
			print("Bangun ruang tersebut bukan Bola")


