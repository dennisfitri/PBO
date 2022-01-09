from tkinter import *

master = Tk()
Label(master, text="Biodata").grid(row=0, columnspan=2)
Label(master, text="Nama Lengkap").grid(row=1)
Label(master, text="NIM").grid(row=2)
Label(master, text="Program Studi").grid(row=3)

nama = Entry(master)
nama.grid(row=1, column=1)
nim = Entry(master)
nim.grid(row=2, column=1)
prodi = Entry(master)
prodi.grid(row=3, column=1)

def show_entry_fields():
	print("Nama : %s" % (nama.get()))
	print("NIM  : %s" % (nim.get()))
	print("Program Studi : %s" % (prodi.get()))

Button(master, text='Kirim', command=show_entry_fields).grid(row=4, column=0, sticky=W, pady=4)
Button(master, text='Keluar', command=master.quit).grid(row=4, column=1, sticky=W, pady=4)

mainloop()