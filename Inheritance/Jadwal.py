import Waktu as w
import Tempat as t
import Kalender as k

class Jadwal(w.Waktu, t.Tempat, k.Kalender):
	def __init__(self):
		self.namaKegiatan = input("Nama Kegiatan :")
		self.jenisKegiatan = input("Jenis Kegiatan :")
		self.hari = input("Hari :")
		self.tanggal = int(input("Tanggal :"))
		self.bulan = int(input("Bulan :"))
		self.tahun = int(input("Tahun :"))
		self.jam = int(input("Jam :"))
		self.menit = int(input("Menit :"))
		self.namaTempat = input("Nama Tempat :")

	def tampilJadwal(self):
		print("JADWAL")
		print("="*30)
		print("Nama Kegiatan :", self.namaKegiatan)
		print("Jenis Kegiatan :", self.jenisKegiatan)
		print("Hari/Tanggal :", self.hari, ",", self.tanggal, "/", self.bulan, "/", self.tahun)
		print("Waktu :", self.jam, ":", self.menit, "WIB")
		print("Tempat :", self.namaKegiatan)

	def ubahJadwal(self):
		namaKegiatan = input("Nama Kegiatan :")
		if(namaKegiatan == ""):
			namaKegiatan = self.namaKegiatan
		else :
			self.namaKegiatan = namaKegiatan
		