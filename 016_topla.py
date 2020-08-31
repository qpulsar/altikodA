# İki sayıyı topla
from tkinter import *


def topla():
    try:
        s1 = int(sayi1.get())
        s2 = int(sayi2.get())
        sonuc["text"] = s1+s2
    except:
        print("sayı dönüşümünde hata.")

root = Tk()
root.title("İki sayıyı topla")
root.geometry("300x300-1200+50")

sayi1 = Entry(root)
sayi1.pack()
sayi2 = Entry(root)
sayi2.pack()

but = Button(text="+", command=topla)
but.pack()

sonuc = Label(text="")
sonuc.pack()

root.mainloop()
