import tkinter
from tkinter import *
import math

root = Tk()
root.title("Menghitung Luas Bangun Datar")
self.label=Label(root, text="Pilih Jenis Bangun Datar")
self.label.pack()
self.segitiga_button = Button(root, text="Segitiga",command=self.segitiga)
self.segitiga_button.pack()
self.persegi_button = Button(root, text="Persegi",command=self.inputsisiPersegi)
self.persegi_button.pack()
self.lingkaran_button = Button(root, text="Lingkaran",command=self.inputsisiLingkaran)
self.lingkaran_button.pack()
self.keluar_button = Button(root, text="Keluar", command=root.quit)
self.keluar_button.pack()


def hitungLuasSegitiga(self):
	print('Luas Segitiga = ',0.5*a.get()*c.get(),'cm2')

def segitiga(self) :
	alas = Label(root, text='Sisi Alas   :').place(x=10,y=10,height=37)	
	a = IntVar()
	b = Entry( root , text = a ).place(x=180,y=10,height=37)

	tinggi = Label(root, text='Sisi Tinggi :').place(x=5,y=70,height=37)
	c = IntVar()
	d = Entry( root , text = c ).place(x=180,y=70,height=37)

	Button( root , text = ' Luas Segitiga ' , command = hitungLuasSegitiga ).place(x=150,y=120,height= 45)

class persegi :
	def hitungLuas():
		print('Luas Persegi = ',a.get()**2,'cm2')

	def inputsisiPersegi():
		sisi = Label(root, text='Panjang Sisi   :').place(x=10,y=10,height=37)
		a = IntVar()
		b = Entry( root , text = a ).place(x=180,y=10,height=37)

		e = Button( root , text = ' Luas Persegi ' , command = hitungLuas ).place(x=150,y=120,height= 45)

class lingkaran :
	def hitungLuas():
		print('Luas Lingkaran = ',math.pi*a.get()**2,'cm2')

	def inputsisiLingkaran():
		jari = Label(root, text='Jari - jari   :').place(x=10,y=10,height=37)
		a = IntVar()
		b = Entry( root , text = a ).place(x=180,y=10,height=37)

		e = Button( root , text = ' Luas Lingkaran ' , command = hitungLuas ).place(x=150,y=120,height= 45)

root.mainloop()