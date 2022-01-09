from tkinter import *

root = Tk()
root.title("Segitiga")
Label(root, text="Segitiga").grid(row=0, columnspan=2)
Label(root, text='Sisi Alas   :').grid(row=1, column=0)
input_alas = IntVar()
alas = Entry( root , text = input_alas ).grid(row=1, column=1)

Label(root, text='Sisi Tinggi :').grid(row=2, column=0)
input_tinggi = IntVar()
tinggi = Entry( root , text = input_tinggi ).grid(row=2, column=1)

def hitungLuas():
    print('Luas Segitiga = ',0.5*input_alas.get()*input_tinggi.get(),'cm^2')

Button( root , text = ' Luas Segitiga ' , command = hitungLuas ).grid(row=3, column=1, sticky=W, pady=4)

root.mainloop()