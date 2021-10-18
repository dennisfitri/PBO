import BangunRuang as b
import math

class Balok(b.bangunRuang):
	def __init__ (self):
		super(b.bangunRuang, self).__init__()
		self.panjang = float(input("Panjang (dalam cm)  	:"))
		self.lebar = float(input("Lebar (dalam cm) 	:"))
		self.tinggi = float(input("Tinggi (dalam cm	:"))

	def volume (self) :
		self.luasAlas = self.panjang * self.lebar
		self.volume = self.luasAlas*self.tinggi
		return self.volume
		
	def dispBalok (self):
		print ("Volume Balok  		:", self.volume, "cm^3")
		print()