from tkinter import *

def show_entry_fields():
	print("Nama : %s!" % (e.get()))
	print("NIM  : %s!" % (e.get()))
	print("Program Studi : %s!" % (e.get()))
	e.delete(0,END)

master = Tk()
Label(master, text="Biodata").grid(row=0, columnspan=2)
Label(master, text="Nama Lengkap").grid(row=1)
Label(master, text="NIM").grid(row=1)
Label(master, text="Program Studi").grid(row=1)

e = Entry(master)
e.grid(row=1, column=1)

Button(master, text='Kirim', command=show_entry_fields).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Keluar', command=master.quit).grid(row=3, column=1, sticky=W, pady=4)

mainloop()