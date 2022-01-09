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

def cetak():
 	Label(master, text='Nama :').grid(column=0, row=5)
 	Label(master, text='NIM :').grid(column=0, row=6)
 	Label(master, text='Prodi :').grid(column=0, row=7)
 	Label(master, text=nama.get()).grid(column=1, row=5)
 	Label(master, text=nim.get()).grid(column=1, row=6)
 	Label(master, text=prodi.get()).grid(column=1, row=7)

Button(master, text='Kirim', command=cetak).grid(row=4, column=0, sticky=W, pady=4)
Button(master, text='Keluar', command=master.quit).grid(row=4, column=1, sticky=W, pady=4)

mainloop()