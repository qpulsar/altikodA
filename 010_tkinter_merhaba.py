from tkinter import *

pencere = Tk()
pencere.title("Altıkod")
pencere.geometry("500x500-50+0")
pencere.resizable(width=False, height=False)

metin = Label(text="Python Harika Bir Dil!")
metin['bg'] = "goldenrod1"
metin.pack(side=LEFT)

metin2 = Label(text="Python Harika Bir Dil!")
metin2['bg'] = "#5dc966"
metin2.pack(side=TOP)

dugme = Button(text="Ben düğmeyim", command=pencere.quit)
dugme.pack(side=BOTTOM)

pencere.mainloop()
