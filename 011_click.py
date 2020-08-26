from tkinter import *


def tikla():
    metin['text'] = "İlk fonksiyonunu yazdın. Tebrikler!!!"


def tiklama():
    metin['text'] = "Ben direk çalışırım"


pencere = Tk()
pencere.geometry("300x300+1200+100")

metin = Label(pencere, text="Düğmeyi tıkla")
metin.pack()

dugme = Button(pencere, text="Beni tıkla", command=tikla)
dugme.pack()

tiklama()
pencere.mainloop()

