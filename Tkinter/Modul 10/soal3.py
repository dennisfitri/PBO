from tkinter import *

def hitungLuasSegitiga():
	if  tinggi > 0 and alas > 0 :
		self.hasil = 0.5*tinggi*alas
	elif tinggi <= 0 and alas <= 0 :
		print ("Error")
	else: # reset
		print("Masukkan angka terlebih dahulu")
	
	Label(master, text='Hasil :').grid(column=0, row=6)
	Label(master, text=self.hasil.get()).grid(column=1, row=6)

master = Tk()
Label(master, text="Segitiga").grid(row=0, columnspan=2)
tinggi = Label(master, text="Tinggi").grid(row=1)
alas = Label(master, text="Alas").grid(row=2)

tinggi = Entry(master)
tinggi.grid(row=1, column=1)
alas = Entry(master)
alas.grid(row=2, column=1)

Button(master, text='Hitung', command=hitungLuasSegitiga).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Keluar', command=master.quit).grid(row=3, column=1, sticky=W, pady=4)

mainloop()