import math
class bangunRuang :
	def __init__(self):
		super(bangunRuang, self).__init__()
		self.nama = "Bangun Ruang"
		self.luasAlas = None
		self.tinggi = None

	def volume(self, luasAlas, tinggi):
		self.volume = luasAlas*tinggi
		return self.volume

#class Tabung(bangunRuang):
#	def __init__ (self):
#		super(bangunRuang, self).__init__()
#		self.jari = 7 #int(input("Jari - jari (cm)  :"))
#		self.tinggi = 8 #int(input("Tinggi (cm) 	:"))

#	def volume (self):
#		self.luasAlas =  math.pi*self.jari**2
#		self.volume = self.luasAlas*self.tinggi
#		return self.volume
		
#	def tampilTabung (self):
#		print ("Volume Tabung 		:", self.volume, "cm^3")
#		print()

#class Balok(bangunRuang):
#	def __init__ (self):
#		super(bangunRuang, self).__init__()
#		self.panjang = 10 #int(input("Panjang (cm)  	:"))
#		self.lebar = 15 #int(input("Lebar (cm) 	:"))
#		self.tinggi = 20 #int(input("Tinggi (cm	:"))

#	def volume (self) :
#		self.luasAlas = self.panjang * self.lebar
#		self.volume = self.luasAlas*self.tinggi
#		return self.volume
		
#	def tampilBalok (self):
#		print ("Volume Balok  		:", self.volume, "cm^3")
#		print()
		
#class Bola(bangunRuang):
#	def __init__ (self):
#		super(bangunRuang, self).__init__()
#		self.jari = 14 #int(input("Jari - jari (dalam cm)  :"))
#		self.tinggi = 14 #int(input("Tinggi (dalam cm) 	:"))

#	def volume(self):
#		if self.jari == self.tinggi:
#			self.volume = 4/3 * self.jari**2
#			print ("Volume Bola   		:", self.volume, "cm^3")
#		else :
#			print("Bangun ruang tersebut bukan Bola")
#
#if __name__ == '__main__':
#	print("TABUNG")
#	tabung1 = Tabung()
#	tabung1.volume()
#	tabung1.tampilTabung()

#	print("BALOK")
#	balok1 = Balok()
#	balok1.volume()
#	balok1.tampilBalok()

#	print("BOLA")
#	bola1 = Bola()
#	bola1.volume()


