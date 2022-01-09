from tkinter import *
import math

class Segitiga:
	def inputSisiSegitiga(self):
		Label(root, text='Menghitung Luas Segitiga',fg='green').pack(pady=50)
		Label(root, text='Sisi Alas   :').pack(pady=5)
		self.alas = IntVar()
		self.alas2 = Entry( root , text = self.alas ).pack(pady=5)

		Label(root, text='Sisi Tinggi :').pack(pady=5)
		self.tinggi = IntVar()
		self.tinggi2 = Entry( root , text = self.tinggi ).pack(pady=5)

		self.hitung_button = Button( root , text = ' Luas Segitiga ' , command = self.luasSegitiga ).pack(pady=5)
	def luasSegitiga(self):
		print('Luas Segitiga = ',0.5*self.alas.get()*self.tinggi.get(),'cm2')
class Persegi:
	def inputSisiPersegi(self):
		Label(root, text='Menghitung Luas Persegi',fg='blue').pack(pady=50)
		Label(root, text='Panjang Sisi   :').pack(pady=5)
		self.sisi = IntVar()
		self.inputSisi = Entry( root , text = self.sisi ).pack(pady=5)

		self.hitung_button = Button( root , text = ' Luas Persegi ' , command = self.luasPersegi ).pack(pady=5)
	def luasPersegi(self):
		print('Luas Persegi = ',self.sisi.get()**2,'cm2')
class Lingkaran:
	def inputSisiLingkaran(self):
		Label(root, text="Menghitung Luas Lingkaran",fg='yellow').pack(pady=50)
		Label(root, text='Jari - jari   :').pack(pady=5)
		self.jari = IntVar()
		self.inputJari = Entry( root , text = self.jari ).pack(pady=5)

		self.hitung_button = Button( root , text = ' Luas Lingkaran ' , command = self.luasLingkaran ).pack(pady=5)
	def luasLingkaran(self):
		print('Luas Lingkaran = ',math.pi*self.jari.get()**2,'cm2')

class BangunDatar(Segitiga, Lingkaran, Persegi):
	def __init__(self,root):
		self.root = root
		self.v = IntVar()
		Label(root, text = 'Bangun Datar').pack(pady=5)
		Radiobutton(root, text='Luas Segitiga', variable=self.v, value = 1, command=self.inputSisiSegitiga).pack(anchor=W, pady=5, padx=5)
		Radiobutton(root, text='Luas Persegi', variable=self.v, value  = 2, command=self.inputSisiPersegi).pack(anchor=W, pady=5, padx=5)
		Radiobutton(root, text='Luas Lingkaran', variable=self.v, value = 3, command=self.inputSisiLingkaran).pack(anchor=W, pady=5, padx=5)
		Button(root, text="Keluar", command=root.quit).pack(anchor=S, pady=5, padx=5)

root = Tk()
root.title('By Mohamad Burhanudin')
root.config(bg = 'Light Steel Blue')
bangun = BangunDatar(root)
root.mainloop()