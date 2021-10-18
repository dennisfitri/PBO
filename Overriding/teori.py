class Induk:
	def __init__(self):
		self.nilai = 5

	def get_nilai(self):
		return self.nilai

class Anak(Induk):
	def get_nilai(self):
		return self.nilai + 1

anak1 = Anak()
print(anak1.get_nilai())