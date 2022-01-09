from tkinter import *

class single_room:
	def single_booking(self):
		master = Tk()
		master.title("nama hotel")
		Label(master, text="Tipe Single Room").grid(row=0, columnspan=2)
		Label(master, text="Fasilitas").grid(row=1, column=0)
		Label(master, text="1. Satu single bed").grid(row=2, column=0)
		Label(master, text="2. Include breakfast (1 orang)").grid(row=3, column=0)
		Label(master, text="3. Kamar mandi").grid(row=4, column=0)
		Label(master, text="Isi data berikut").grid(row=5, columnspan=2)
		Label(master, text="Nama").grid(row=6)
		Label(master, text="Check In").grid(row=7)
		Label(master, text="Check Out").grid(row=8)

		self.hari = 0
		self.label_text = IntVar()
		self.label_text.set(self.hari)
		self.label_hari = Label(master, text="Berapa Hari").grid(row=9)
		vcmd = master.register(self.validate)
		self.input_hari = Entry(master, validate="key", validatecommand=(vcmd, '%P')).grid(row=9, column=1)


		Label(master, text="Berapa Kamar").grid(row=10)
		self.kamar= IntVar()
		self.input_kamar = Entry (master , text = self.kamar ).grid(row=10, column=1)

		Label(master, text="Berapa Orang").grid(row=11)
		self.orang = IntVar()
		self.input_orang = Entry(master , text = self.orang ).grid(row=11, column=1)
		
		self.nama = Entry(master)
		self.check_in = Entry(master)
		self.check_out = Entry(master)

		self.nama.grid(row=6, column=1)
		self.check_in.grid(row=7, column=1)
		self.check_out.grid(row=8, column=1)
		
		self.selesai = Button( master , text = ' Selesai ' , command = self.cetak ).grid(row=13, column=1)

	#def cekHarga (self):
		#print("Harga :",self.hari.get()*self.kamar.get()*450000)
		
	def cetak (self):
		master = Tk()
		master.title("nama hotel")
		Label(master, text="Konfirmasi Pesanan").grid(row=0, columnspan=2)
		Label(master, text='Nama :').grid(column=0, row=1)
		Label(master, text="Tipe Kamar :").grid(column=0, row=2)
		Label(master, text='Check In :').grid(column=0, row=3)
		Label(master, text='Check Out :').grid(column=0, row=4)

	def validate(self, new_text) :
		if not new_text:
			self.hari = 0
			return True

		try:
			self.hari = int(new_text)
			return True

		except ValueError:
			return False


		Label(master, text='Jumlah Hari :').grid(column=0, row=5)
		#Label(master, text='Jumlah Kamar :').grid(column=0, row=6)
		#Label(master, text='Jumlah Orang :').grid(column=0, row=7)
		#Label(master, text='Harga :').grid(column=0, row=8)
		
		Label(master, text=self.nama.get()).grid(column=1, row=1)
		Label(master, text="Single Room").grid(column=1, row=2)
		Label(master, text=self.check_in.get()).grid(column=1, row=3)
		Label(master, text=self.check_out.get()).grid(column=1, row=4)
		Label(master, text=self.hari.get()).grid(column=1, row=5)
		#Label(master, text=self.kamar.get()).grid(column=1, row=6)
		#self.harga = self.hari.get()*self.kamar.get()*450000
		#Label(master, text=self.orang.get()).grid(column=1, row=7)
		#Label(master, text=self.harga).grid(column=1, row=8)

		self.konfirm = Button( master , text = 'Konfirmasi' , command = self.konfimasi ).grid(row=9, column=1)
		self.keluar_button = Button(master, text="Keluar", command=master.quit).grid(row=10, column=1)

	def konfirmasi (self):
		master = Tk()
		master.title("nama hotel")
		Label(master, text="Terima Kasih atas Pesanan Anda").grid(row=0, columnspan=2)
		Label(master, text="Silahkan lakukan pembayaran di represionis").grid(row=1, columnspan=2)
		Label(master, text="Sebelum pukul 10.00").grid(row=2, columnspan=2)
		self.keluar_button = Button(master, text="Keluar", command=master.quit).grid(row=3, column=1)
		
class double_room:
	def cetak (self):
		master = Tk()
		master.title("nama hotel")
		Label(master, text="Konfirmasi Pesanan").grid(row=0, columnspan=2)
		Label(master, text='Nama :').grid(column=0, row=1)
		Label(master, text="Tipe Kamar :").grid(column=0, row=2)
		Label(master, text='Check In :').grid(column=0, row=3)
		Label(master, text='Check Out :').grid(column=0, row=4)
		Label(master, text='Jumlah Hari :').grid(column=0, row=5)
		Label(master, text='Jumlah Kamar :').grid(column=0, row=6)
		Label(master, text='Jumlah Orang :').grid(column=0, row=7)
		Label(master, text='Harga :').grid(column=0, row=8)
		Label(master, text=self.nama.get()).grid(column=1, row=1)
		Label(master, text="Single Room").grid(column=1, row=2)
		Label(master, text=self.check_in.get()).grid(column=1, row=3)
		Label(master, text=self.check_out.get()).grid(column=1, row=4)
		Label(master, text=self.hari.get()).grid(column=1, row=5)
		Label(master, text=self.kamar.get()).grid(column=1, row=6)
		Label(master, text=self.orang.get()).grid(column=1, row=7)
		Label(master, text=self.hari.get()*self.kamar.get()*600000).grid(column=1, row=8)
		self.selesai = Button( master , text = 'Konfirmasi' , command = self.konfimasi ).grid(row=9, column=1)
		self.keluar_button = Button(master, text="Keluar", command=master.quit).grid(row=10, column=1)

	def konfirmasi (self):
		master = Tk()
		master.title("nama hotel")
		Label(master, text="Terima Kasih atas Pesanan Anda").grid(row=0, columnspan=2)
		Label(master, text="Silahkan lakukan pembayaran di represionis").grid(row=1, columnspan=2)
		Label(master, text="Sebelum pukul 10.00").grid(row=2, columnspan=2)
		self.keluar_button = Button(master, text="Keluar", command=master.quit).grid(row=3, column=1)


	def double_booking(self):
		master = Tk()
		master.title("nama hotel")
		Label(master, text="Tipe Single Room").grid(row=0, columnspan=2)
		Label(master, text="Fasilitas").grid(row=1, column=0)
		Label(master, text="1. Master bed").grid(row=2, column=0)
		Label(master, text="2. Include breakfast (2 orang)").grid(row=3, column=0)
		Label(master, text="3. Kamar mandi").grid(row=4, column=0)
		Label(master, text="Isi data berikut").grid(row=5, columnspan=2)
		Label(master, text="Nama").grid(row=6)
		Label(master, text="Check In").grid(row=7)
		Label(master, text="Check Out").grid(row=8)
		Label(master, text="Berapa Hari").grid(row=9)
		Label(master, text="Berapa Kamar").grid(row=10)
		Label(master, text="Berapa Orang").grid(row=11)
		
		self.nama = Entry(master)
		self.check_in = Entry(master)
		self.check_out = Entry(master)
		self.hari= IntVar()
		self.kamar= IntVar()
		self.orang = IntVar()

		self.nama.grid(row=6, column=1)
		self.check_in.grid(row=7, column=1)
		self.check_out.grid(row=8, column=1)
		self.input_hari(master , text = self.hari ).grid(row=9, column=1)
		self.input_kamar(master , text = self.kamar ).grid(row=10, column=1)
		self.input_orang(master , text = self.orang ).grid(row=11, column=1)
		
		self.selesai = Button( master , text = ' Selesai ' , command = self.cetak ).grid(row=13, column=1)

class Pemesanan (single_room, double_room):
	def __init__ (self, master):
		master.title("Booking Hotel Online")
		self.label=Label(master, text="Silahkan Pilih Tipe Kamar")
		self.label.pack()
		self.single = Button(master, text="Single Room",command=self.single_booking)
		self.single.pack()
		self.double = Button(master, text="Double Room",command=self.double_booking)
		self.double.pack()
		#self.deluxe = Button(master, text="Deluxe Room",command=self.daftarPindahan)
		#self.deluxe.pack()
		self.keluar_button = Button(master, text="Keluar", command=master.quit)
		self.keluar_button.pack()
		#single_room.konfimasi(self,parent)


root = Tk()
my_gui = Pemesanan(root)
root.mainloop()


