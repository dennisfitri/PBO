from tkinter import *
from tkinter import messagebox

class single_room:

	def single_booking(self):
		master = Tk()
		master.config(bg = 'dark gray')
		master.title("Four Seaoson Resort Hotel")
		Label(master, text="Tipe Single Room", bg="dark gray", fg="olive", font="Forte 15").grid(row=0, columnspan=2, pady=5)
		Label(master, text="Fasilitas", bg="dark gray", fg="olive", font="Sylfaen 10 bold italic").grid(row=1, column=0, pady=5)
		Label(master, text="1. Satu single bed", bg = 'dark gray', fg="white", font="Sylfaen 10").grid(row=2, column=0)
		Label(master, text="2. Include breakfast (1 orang)", bg = 'dark gray', fg="white", font="Sylfaen 10").grid(row=3, column=0)
		Label(master, text="3. Kamar mandi", bg = 'dark gray', fg="white", font="Sylfaen 10").grid(row=4, column=0)
		Label(master, text="Isi data berikut", bg="dark gray", fg="olive", font="Sylfaen 10 bold italic").grid(row=5, columnspan=2, pady=5)
		Label(master, text="Nama", bg = 'dark gray', fg="white", font="Sylfaen 10").grid(row=6, pady=5)
		Label(master, text="Check In", bg = 'dark gray', fg="white", font="Sylfaen 10").grid(row=7, pady=5)
		Label(master, text="Check Out", bg = 'dark gray', fg="white", font="Sylfaen 10").grid(row=8, pady=5)
		Label(master, text="Berapa Hari", bg = 'dark gray', fg="white", font="Sylfaen 10").grid(row=9, pady=5)
		Label(master, text="Berapa Kamar", bg = 'dark gray', fg="white", font="Sylfaen 10").grid(row=10, pady=5)
		Label(master, text="Berapa Orang", bg = 'dark gray', fg="white", font="Sylfaen 10").grid(row=11, pady=5)
		Label(master, text="Harga", bg = 'dark gray', fg="white", font="Sylfaen 10").grid(row=13, pady=5)
		Label(master, text="Harap lakukan cek data terlebih dahulu sebelum melakukan konfirmasi.", bg = "dark gray", fg="red", font="Sylfaen 10").grid(row=14, columnspan=2, pady=5)
		
		self.nama = Entry(master)
		self.check_in = Entry(master)
		self.check_out = Entry(master)
		self.hari = Spinbox(master, from_=0, to=100)
		self.kamar = Spinbox(master, from_=0, to=100)	
		self.orang = Spinbox(master, from_=0, to=100)	
		self.harga = Entry(master)	

		self.nama.grid(row=6, column=1, pady=5)
		self.check_in.grid(row=7, column=1, pady=5)
		self.check_out.grid(row=8, column=1, pady=5)
		self.hari.grid(row=9, column=1, pady=5)
		self.kamar.grid(row=10, column=1, pady=5)
		self.orang.grid(row=11, column=1, pady=5)
		self.harga.grid(row=13, column=1, pady=5)
		
		self.nama.bind("<KeyRelease>", self.cekKarakter)
		self.hari.bind("<KeyRelease>", self.cekKarakter)
		self.kamar.bind("<KeyRelease>", self.cekKarakter)
		self.orang.bind("<KeyRelease>", self.cekKarakter)
		self.harga.bind("<KeyRelease>", self.cekKarakter)

		self.cek = Button( master , text = ' Cek Harga ' , command = self.cekHarga, bg="olive", fg="white", font="Sylfaen 10").grid(row=12, column=1, pady=5)
		self.cekDataTombol = Button( master , text = ' Cek Data ', command = self.cekData , bg="olive", fg="white", font="Sylfaen 10").grid(row=12, column=0, pady=5)
		self.konfirmasi = Button( master , text = 'Konfirmasi' , command = self.Konfirmasi, bg="olive", fg="white", font="Sylfaen 10").grid(row=15, column=0, pady=5)
		self.selesai = Button(master, text="Selesai", command=self.Selesai, bg="olive", fg="white", font="Sylfaen 10").grid(row=15, column=1, pady=5)

	def cekKarakter(self, event):
		if event.keycode>48 and event.keycode<57:
			self.nama.delete(0, END)

		if event.keycode>65 and event.keycode<90:
			self.hari.delete(0,END)

		if event.keycode>65 and event.keycode<90:
			self.kamar.delete(0,END)

		if event.keycode>65 and event.keycode<90: 
			self.orang.delete(0,END)

		if event.keycode>65 and event.keycode<90:  
			self.harga.delete(0,END)

	def cekData (self):
		if self.nama.get() == "":
			messagebox.showwarning(message="Nama tidak boleh kosong!")
			return False

		if self.check_in.get() == "":
			messagebox.showwarning(message="Harap isi tanggal check in!")
			return False

		if self.check_out.get() == "":
			messagebox.showwarning(message="Harap isi tanggal check out!")
			return False

		if self.hari.get() == "0":
			messagebox.showwarning(message="Harap isi kolom berapa hari anda akan memesan!")
			return False

		if self.kamar.get() == "0":
			messagebox.showwarning(message="Harap isi kolom berapa kamar yang akan anda pesan!")
			return False

		if self.orang.get() == "0":
			messagebox.showwarning(message="Harap isi berapa orang yang akan menginap!")
			return False

		if self.harga.get() == "":
			messagebox.showwarning(message="Harap lakukan cek harga terlebih dahulu!")
			return False

		messagebox.showinfo(message="Data anda telah lengkap, harap lakukan konfirmasi pesanan anda!")

	def cekHarga (self):
		totalHari = int(self.hari.get())
		totalKamar = int(self.kamar.get())
		totalHarga = 450000*totalHari*totalKamar

		self.harga.insert(END, int(totalHarga))

	def Konfirmasi (self):
		print("========PESANAN MASUK========")
		print("Nama 		: %s" % (self.nama.get()))
		print("Tipe kamar 	: Single Room")
		print("Check In  	: %s" % (self.check_in.get()))
		print("Check Out 	: %s" % (self.check_out.get()))
		print("Jumlah Hari 	: %s" % (self.hari.get()))
		print("Jumlah Kamar 	: %s" % (self.kamar.get()))
		print("Jumlah Orang 	: %s" % (self.orang.get()))
		print("Harga 		: %s" % (self.harga.get()))

		self.nama.delete(0, END)
		self.check_in.delete(0, END)
		self.check_out.delete(0, END)
		self.hari.delete(0, END)
		self.kamar.delete(0, END)
		self.orang.delete(0, END)
		self.harga.delete(0, END)

	def Selesai (self):
		master = Tk()
		master.title("Four Seaoson Resort Hotel")
		master.config(bg = 'dark gray')
		Label(master, text="Terima Kasih",bg="dark gray", fg="olive", font="Forte 15").grid(row=0, columnspan=2)
		Label(master, text="Pesanan anda akan diproses jika sudah melakukan konfimasi",bg="dark gray", fg="white", font="Sylfaen 12").grid(row=1, columnspan=2)
		Label(master, text="Silahkan lakukan pembayaran di represionis sebelum pukul 10.00",bg="dark gray", fg="white", font="Sylfaen 12").grid(row=2, columnspan=2)
		self.keluar_button = Button(master, text="Keluar", command=master.quit, bg="olive", fg="white", font="Sylfaen 10 bold").grid(row=3, columnspan=2, pady=5)

class double_room:

	def double_booking(self):
		master = Tk()
		master.config(bg = 'dark gray')
		master.title("Four Seaoson Resort Hotel")
		Label(master, text="Tipe Double Room", bg="dark gray", fg="olive", font="Forte 15").grid(row=0, columnspan=2, pady=5)
		Label(master, text="Fasilitas", bg="dark gray", fg="olive", font="Sylfaen 10 bold italic").grid(row=1, column=0, pady=5)
		Label(master, text="1. Dua single bed", bg = 'dark gray', fg="white", font="Sylfaen 10").grid(row=2, column=0)
		Label(master, text="2. Include breakfast (2 orang)", bg = 'dark gray', fg="white", font="Sylfaen 10").grid(row=3, column=0)
		Label(master, text="3. Kamar mandi", bg = 'dark gray', fg="white", font="Sylfaen 10").grid(row=4, column=0)
		Label(master, text="Isi data berikut", bg="dark gray", fg="olive", font="Sylfaen 10 bold italic").grid(row=5, columnspan=2, pady=5)
		Label(master, text="Nama", bg = 'dark gray', fg="white", font="Sylfaen 10").grid(row=6, pady=5)
		Label(master, text="Check In", bg = 'dark gray', fg="white", font="Sylfaen 10").grid(row=7, pady=5)
		Label(master, text="Check Out", bg = 'dark gray', fg="white", font="Sylfaen 10").grid(row=8, pady=5)
		Label(master, text="Berapa Hari", bg = 'dark gray', fg="white", font="Sylfaen 10").grid(row=9, pady=5)
		Label(master, text="Berapa Kamar", bg = 'dark gray', fg="white", font="Sylfaen 10").grid(row=10, pady=5)
		Label(master, text="Berapa Orang", bg = 'dark gray', fg="white", font="Sylfaen 10").grid(row=11, pady=5)
		Label(master, text="Harga", bg = 'dark gray', fg="white", font="Sylfaen 10").grid(row=13, pady=5)
		Label(master, text="Harap lakukan cek data terlebih dahulu sebelum melakukan konfirmasi.",bg="dark gray", fg="red", font="Sylfaen 10").grid(row=14, columnspan=2, pady=5)
		
		self.nama = Entry(master)
		self.check_in = Entry(master)
		self.check_out = Entry(master)
		self.hari= Spinbox(master, from_=0, to=100)
		self.kamar = Spinbox(master, from_=0, to=100)	
		self.orang = Spinbox(master, from_=0, to=100)	
		self.harga = Entry(master)	

		self.nama.grid(row=6, column=1, pady=5)
		self.check_in.grid(row=7, column=1, pady=5)
		self.check_out.grid(row=8, column=1, pady=5)
		self.hari.grid(row=9, column=1, pady=5)
		self.kamar.grid(row=10, column=1, pady=5)
		self.orang.grid(row=11, column=1, pady=5)
		self.harga.grid(row=13, column=1, pady=5)

		self.nama.bind("<KeyRelease>", self.cekKarakter2)
		self.hari.bind("<KeyRelease>", self.cekKarakter2)
		self.kamar.bind("<KeyRelease>", self.cekKarakter2)
		self.orang.bind("<KeyRelease>", self.cekKarakter2)
		self.harga.bind("<KeyRelease>", self.cekKarakter2)
		
		self.cek = Button( master , text = ' Cek Harga ' , command = self.cekHarga2, bg="olive", fg="white", font="Sylfaen 10").grid(row=12, column=1, pady=5)
		self.cekDataTombol = Button( master , text = ' Cek Data ', command = self.cekData2 , bg="olive", fg="white", font="Sylfaen 10").grid(row=12, column=0, pady=5)
		self.konfimasi = Button( master , text = 'Konfirmasi' , command = self.Konfirmasi2, bg="olive", fg="white", font="Sylfaen 10").grid(row=15, column=0, pady=5)
		self.selesai = Button(master, text="Selesai", command=self.Selesai2, bg="olive", fg="white", font="Sylfaen 10").grid(row=15, column=1, pady=5)
	
	def cekKarakter2(self, event):
		if event.keycode>48 and event.keycode<57:
			self.nama.delete(0, END)

		if event.keycode>65 and event.keycode<90:
			self.hari.delete(0,END)

		if event.keycode>65 and event.keycode<90:
			self.kamar.delete(0,END)

		if event.keycode>65 and event.keycode<90: 
			self.orang.delete(0,END)

		if event.keycode>65 and event.keycode<90:  
			self.harga.delete(0,END)


	def cekData2 (self):
		if self.nama.get() == "":
			messagebox.showwarning(message="Nama tidak boleh kosong!")
			return False

		if self.check_in.get() == "":
			messagebox.showwarning(message="Harap isi tanggal check in!")
			return False

		if self.check_out.get() == "":
			messagebox.showwarning(message="Harap isi tanggal check out!")
			return False

		if self.hari.get() == "0":
			messagebox.showwarning(message="Harap isi kolom berapa hari anda akan memesan!")
			return False

		if self.kamar.get() == "0":
			messagebox.showwarning(message="Harap isi kolom berapa kamar yang akan anda pesan!")
			return False

		if self.orang.get() == "0":
			messagebox.showwarning(message="Harap isi berapa orang yang akan menginap!")
			return False

		if self.harga.get() == "":
			messagebox.showwarning(message="Harap lakukan cek harga terlebih dahulu!")
			return False

		messagebox.showinfo(message="Data anda telah lengkap, harap lakukan konfirmasi pesanan anda!")

	def cekHarga2 (self, event=None):
		totalHari = int(self.hari.get())
		totalKamar = int(self.kamar.get())
		totalHarga = 600000*totalHari*totalKamar

		self.harga.insert(END, str(totalHarga))

	def Konfirmasi2 (self):
		print("========PESANAN MASUK========")
		print("Nama 		: %s" % (self.nama.get()))
		print("Tipe kamar 	: Double Room")
		print("Check In  	: %s" % (self.check_in.get()))
		print("Check Out 	: %s" % (self.check_out.get()))
		print("Jumlah Hari 	: %s" % (self.hari.get()))
		print("Jumlah Kamar 	: %s" % (self.kamar.get()))
		print("Jumlah Orang 	: %s" % (self.orang.get()))
		print("Harga 		: %s" % (self.harga.get()))

		self.nama.delete(0, END)
		self.check_in.delete(0, END)
		self.check_out.delete(0, END)
		self.hari.delete(0, END)
		self.kamar.delete(0, END)
		self.orang.delete(0, END)
		self.harga.delete(0, END)

	def Selesai2 (self, event=None):
		master = Tk()
		master.title("Four Seaoson Resort Hotel")
		master.config(bg = 'dark gray')
		Label(master, text="Terima Kasih",bg="dark gray", fg="olive", font="Forte 15").grid(row=0, columnspan=2)
		Label(master, text="Pesanan anda akan diproses jika sudah melakukan konfimasi",bg="dark gray", fg="white", font="Sylfaen 12").grid(row=1, columnspan=2)
		Label(master, text="Silahkan lakukan pembayaran di represionis sebelum pukul 10.00",bg="dark gray", fg="white", font="Sylfaen 12").grid(row=2, columnspan=2)
		self.keluar_button = Button(master, text="Keluar", command=master.quit, bg="olive", fg="white", font="Sylfaen 10 bold").grid(row=3, columnspan=2, pady=5)

class deluxe_room:

	def deluxe_booking(self):
		master = Tk()
		master.config(bg = 'dark gray')
		master.title("Four Seaoson Resort Hotel")
		Label(master, text="Tipe Deluxe Room", bg="dark gray", fg="olive", font="Forte 15").grid(row=0, columnspan=2, pady=5)
		Label(master, text="Fasilitas", bg="dark gray", fg="olive", font="Sylfaen 10 bold italic").grid(row=1, column=0, pady=5)
		Label(master, text="1. Satu master bed", bg = 'dark gray', fg="white", font="Sylfaen 10").grid(row=2, column=0)
		Label(master, text="2. Include breakfast (2 orang)", bg = 'dark gray', fg="white", font="Sylfaen 10").grid(row=3, column=0)
		Label(master, text="3. Kamar mandi", bg = 'dark gray', fg="white", font="Sylfaen 10").grid(row=4, column=0)
		Label(master, text="4. Living room", bg = 'dark gray', fg="white", font="Sylfaen 10").grid(row=5, column=0)
		Label(master, text="5. Kitchen", bg = 'dark gray', fg="white", font="Sylfaen 10").grid(row=6, column=0)
		Label(master, text="Isi data berikut", bg="dark gray", fg="olive", font="Sylfaen 10 bold italic").grid(row=7, columnspan=2, pady=5)
		Label(master, text="Nama", bg = 'dark gray', fg="white", font="Sylfaen 10").grid(row=8, pady=5)
		Label(master, text="Check In", bg = 'dark gray', fg="white", font="Sylfaen 10").grid(row=9, pady=5)
		Label(master, text="Check Out", bg = 'dark gray', fg="white", font="Sylfaen 10").grid(row=10, pady=5)
		Label(master, text="Berapa Hari", bg = 'dark gray', fg="white", font="Sylfaen 10").grid(row=11, pady=5)
		Label(master, text="Berapa Kamar", bg = 'dark gray', fg="white", font="Sylfaen 10").grid(row=12, pady=5)
		Label(master, text="Berapa Orang", bg = 'dark gray', fg="white", font="Sylfaen 10").grid(row=13, pady=5)
		Label(master, text="Harga", bg = 'dark gray', fg="white", font="Sylfaen 10").grid(row=15, pady=5)
		Label(master, text="Harap lakukan cek data terlebih dahulu sebelum melakukan konfirmasi.",bg="dark gray", fg="red", font="Sylfaen 10").grid(row=16, columnspan=2, pady=5)
		
		self.nama = Entry(master)
		self.check_in = Entry(master)
		self.check_out = Entry(master)
		self.hari= Spinbox(master, from_=0, to=100)
		self.kamar = Spinbox(master, from_=0, to=100)	
		self.orang = Spinbox(master, from_=0, to=100)	
		self.harga = Entry(master)	

		self.nama.grid(row=8, column=1)
		self.check_in.grid(row=9, column=1)
		self.check_out.grid(row=10, column=1)
		self.hari.grid(row=11, column=1)
		self.kamar.grid(row=12, column=1)
		self.orang.grid(row=13, column=1)
		self.harga.grid(row=15, column=1)

		self.nama.bind("<KeyRelease>", self.cekKarakter3)
		self.hari.bind("<KeyRelease>", self.cekKarakter3)
		self.kamar.bind("<KeyRelease>", self.cekKarakter3)
		self.orang.bind("<KeyRelease>", self.cekKarakter3)
		self.harga.bind("<KeyRelease>", self.cekKarakter3)
		
		self.cek = Button( master , text = ' Cek Harga ' , command = self.cekHarga3, bg="olive", fg="white", font="Sylfaen 10").grid(row=14, column=1, pady=5)
		self.cekDataTombol = Button( master , text = ' Cek Data ', command = self.cekData3 , bg="olive", fg="white", font="Sylfaen 10").grid(row=14, column=0, pady=5)
		self.konfimasi = Button( master , text = 'Konfirmasi' , command = self.Konfirmasi3, bg="olive", fg="white", font="Sylfaen 10").grid(row=17, column=0, pady=5)
		self.selesai = Button(master, text="Selesai", command=self.Selesai3, bg="olive", fg="white", font="Sylfaen 10").grid(row=17, column=1, pady=5)
		
	def cekKarakter3(self, event):
		if event.keycode>48 and event.keycode<57:
			self.nama.delete(0, END)

		if event.keycode>65 and event.keycode<90:
			self.hari.delete(0,END)

		if event.keycode>65 and event.keycode<90:
			self.kamar.delete(0,END)

		if event.keycode>65 and event.keycode<90: 
			self.orang.delete(0,END)

		if event.keycode>65 and event.keycode<90:  
			self.harga.delete(0,END)

	def cekData3 (self):
		if self.nama.get() == "":
			messagebox.showwarning(message="Nama tidak boleh kosong!")
			return False

		if self.check_in.get() == "":
			messagebox.showwarning(message="Harap isi tanggal check in!")
			return False

		if self.check_out.get() == "":
			messagebox.showwarning(message="Harap isi tanggal check out!")
			return False

		if self.hari.get() == "0":
			messagebox.showwarning(message="Harap isi kolom berapa hari anda akan memesan!")
			return False

		if self.kamar.get() == "0":
			messagebox.showwarning(message="Harap isi kolom berapa kamar yang akan anda pesan!")
			return False

		if self.orang.get() == "0":
			messagebox.showwarning(message="Harap isi berapa orang yang akan menginap!")
			return False

		if self.harga.get() == "":
			messagebox.showwarning(message="Harap lakukan cek harga terlebih dahulu!")
			return False

		messagebox.showinfo(message="Data anda telah lengkap, harap lakukan konfirmasi pesanan anda!")

	def cekHarga3 (self, event=None):
		totalHari = int(self.hari.get())
		totalKamar = int(self.kamar.get())
		totalHarga = 1000000*totalHari*totalKamar

		self.harga.insert(END, int(totalHarga))

	def Konfirmasi3 (self):
		print("========PESANAN MASUK========")
		print("Nama 		: %s" % (self.nama.get()))
		print("Tipe kamar 	: Deluxe Room")
		print("Check In  	: %s" % (self.check_in.get()))
		print("Check Out 	: %s" % (self.check_out.get()))
		print("Jumlah Hari 	: %s" % (self.hari.get()))
		print("Jumlah Kamar 	: %s" % (self.kamar.get()))
		print("Jumlah Orang 	: %s" % (self.orang.get()))
		print("Harga 		: %s" % (self.harga.get()))

		self.nama.delete(0, END)
		self.check_in.delete(0, END)
		self.check_out.delete(0, END)
		self.hari.delete(0, END)
		self.kamar.delete(0, END)
		self.orang.delete(0, END)
		self.harga.delete(0, END)

	def Selesai3 (self, event=None):
		master = Tk()
		master.title("Four Seaoson Resort Hotel")
		master.config(bg = 'dark gray')
		Label(master, text="Terima Kasih",bg="dark gray", fg="olive", font="Forte 15").grid(row=0, columnspan=2)
		Label(master, text="Pesanan anda akan diproses jika sudah melakukan konfimasi",bg="dark gray", fg="white", font="Sylfaen 12").grid(row=1, columnspan=2)
		Label(master, text="Silahkan lakukan pembayaran di represionis sebelum pukul 10.00",bg="dark gray", fg="white", font="Sylfaen 12").grid(row=2, columnspan=2)
		self.keluar_button = Button(master, text="Keluar", command=master.quit, bg="olive", fg="white", font="Sylfaen 10 bold").grid(row=3, columnspan=2, pady=5)

class Pemesanan (single_room, double_room, deluxe_room):
	def __init__ (self, master):
		master.title("Four Seaoson Resort Hotel")
		self.label=Label(master, text="Booking Hotel", bg="dark gray", fg="olive", font="Forte 12").grid(row=0, columnspan=2)
		self.label=Label(master, text="Four Seaoson Resort Hotel", bg="dark gray", fg="olive", font="Sylfaen 10 bold italic").grid(row=1, columnspan=2)
		self.label1=Label(master, text="Silahkan Pilih Tipe Kamar", bg="dark gray", fg="white", font="Sylfaen 10").grid(row=2, columnspan=2, pady=5)
		self.single = Button(master, text="Single Room",command=self.single_booking, bg="olive", fg="white", font="Sylfaen 10")
		self.single.grid(row=3, column=0, pady=5)
		self.double = Button(master, text="Double Room",command=self.double_booking, bg="olive", fg="white", font="Sylfaen 10")
		self.double.grid(row=3, column=1, pady=5, padx=5)
		self.deluxe = Button(master, text="Deluxe Room",command=self.deluxe_booking, bg="olive", fg="white", font="Sylfaen 10")
		self.deluxe.grid(row=4, columnspan=2, pady=5)
		self.keluar_button = Button(master, text="Keluar", command=master.quit, bg="olive", fg="white", font="Sylfaen 10")
		self.keluar_button.grid(row=5, columnspan=2, pady=5)
	
root = Tk()
my_gui = Pemesanan(root) 
root.config(bg = 'dark gray')
root.mainloop()