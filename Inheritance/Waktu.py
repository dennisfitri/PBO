class Waktu:
# def _init_(self, jam=0, menit=0, detik=0):
	def __init__(self, jam=0, menit=0, detik=0):
		self.jam = jam
		self.menit = menit
		self.detik = detik

	def ubahWaktu(self, jam, menit, detik=0):
		self.jam = jam
		self.menit = menit
		self.detik = detik

	