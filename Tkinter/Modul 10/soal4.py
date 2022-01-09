from tkinter import*
import math

class segitiga :
	def inputsisiSegitiga(self):
		self.Alas = Label(root, text='Sisi Alas   :').place(x=10,y=10,height=37)
		self.alas = IntVar()
		self.alas2 = Entry( root , text = self.alas ).place(x=100,y=15,height=25)

		self.Tinggi = Label(root, text='Sisi Tinggi :').place(x=10,y=50,height=37)
		self.tinggi = IntVar()
		self.tinggi2 = Entry( root , text = self.tinggi ).place(x=100,y=55,height=25)

		self.hitung_button = Button( root , text = ' Luas Segitiga ' , command = self.hitungLuasSegitiga ).place(x=120,y=90,height= 37)

	def hitungLuasSegitiga(self):
		print('Luas Segitiga = ',0.5*self.alas.get()*self.tinggi.get(),'cm^2')

class persegi :
	def inputsisiPersegi(self):
		self.Sisi = Label(root, text='Panjang Sisi   :').place(x=10,y=140,height=37)
		self.sisi = IntVar()
		self.sisi2 = Entry( root , text = self.sisi ).place(x=100,y=145,height=25)

		self.hitung_button = Button( root , text = ' Luas Persegi ' , command = self.hitungLuasPersegi ).place(x=120,y=180,height= 37)

	def hitungLuasPersegi(self):
		print('Luas Persegi = ',self.sisi.get()**2,'cm^2')

class lingkaran :
	def inputsisiLingkaran(self):
		self.Jari = Label(root, text='Jari - jari   :').place(x=10,y=230,height=37)
		self.jari = IntVar()
		self.jari2 = Entry( root , text = self.jari ).place(x=100,y=235,height=25)

		self.hitung_button = Button( root , text = ' Luas Lingkaran ' , command = self.hitungLuasLingkaran ).place(x=120,y=270,height= 37)

	def hitungLuasLingkaran(self):
		print('Luas Lingkaran = ',math.pi*self.jari.get()**2,'cm^2')

class luas (segitiga, persegi, lingkaran):
	def __init__ (self, root):
		self.root = root
		root.title("Menghitung Luas Bangun Datar")
		self.label=Label(root, text="Pilih Jenis Bangun Datar")
		self.label.pack()
		self.segitiga_button = Button(root, text="Segitiga",command=self.inputsisiSegitiga)
		self.segitiga_button.pack()
		self.persegi_button = Button(root, text="Persegi",command=self.inputsisiPersegi)
		self.persegi_button.pack()
		self.lingkaran_button = Button(root, text="Lingkaran",command=self.inputsisiLingkaran)
		self.lingkaran_button.pack()
		self.keluar_button = Button(root, text="Keluar", command=root.quit)
		self.keluar_button.pack()

root = Tk()
my_gui = luas(root)
root.mainloop()