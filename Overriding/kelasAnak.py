import BangunRuang as b
import math

class Tabung(b.bangunRuang):
	def __init__ (self):
		super(b.bangunRuang, self).__init__()
		self.r = int(input("Jari - jari (dalam cm)  :"))
		self.tinggi = int(input("Tinggi (dalam cm) 	:"))

	def volume (self):
		self.luasAlas =  math.pi*self.r**2
		self.volume = self.luasAlas*self.tinggi
		return self.volume
		
	def dispTabung (self):
		print ("Volume Tabung 		:", self.volume, "cm^3")
		print()

class Balok(b.bangunRuang):
	def __init__ (self):
		super(b.bangunRuang, self).__init__()
		self.panjang = int(input("Panjang (dalam cm)  	:"))
		self.lebar = int(input("Lebar (dalam cm) 	:"))
		self.tinggi = int(input("Tinggi (dalam cm	:"))

	def volume (self) :
		self.luasAlas = self.panjang * self.lebar
		self.volume = self.luasAlas*self.tinggi
		return self.volume
		
	def dispBalok (self):
		print ("Volume Balok  		:", self.volume, "cm^3")
		print()
		
class Bola(b.bangunRuang):
	def __init__ (self):
		super(b.bangunRuang, self).__init__()
		self.r = int(input("Jari - jari (dalam cm)  :"))
		self.tinggi = int(input("Tinggi (dalam cm) 	:"))

	def volume(self):
		luasAlas = math.pi * self.r**2
		if self.r == self.tinggi:
			self.volume = 4/3 * luasAlas * self.tinggi
		else :
			print("Bangun ruang tersebut bukan Bola")

	def dispBola (self):
		print ("Volume Bola   		:", self.volume, "cm^3")
		print()

