import Segiempat as s
import Polygon as p

#menunjukkan bahwa file ini merupakan kelas Main.
if __name__ == "__main__":
	#s4 adalah objek dari kelas Segiempat
	s4 = s.Segiempat()

	#method inputSisi() dan dispSisi() dimiliki oleh Polygon (kelas induk)
	s4.inputSisi()
	s4.dispSisi()

	#method hitungKeliling() dimiliki oleh kelas Segiempat (kelas anak)
	s4.hitungKeliling()

	#poly adalah objek dari kelas polygon
	#poly = p.Polygon(4)

	#poly.inputSisi()
	#poly.dispSisi()

	#mehod hitungKeliling()