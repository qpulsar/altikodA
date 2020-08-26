from tkinter import *
import tkinter.font

pencere = Tk()
pencere.title("işte fontlar")
pencere.geometry("300x500")
pencere["bg"] = "#ffaa33"

fontlar = list(tkinter.font.families())
fontlar.sort()

liste = Listbox(pencere, font="Broadway 20")
liste.pack()

for f in fontlar:
    liste.insert(END, f)

pencere.mainloop()
