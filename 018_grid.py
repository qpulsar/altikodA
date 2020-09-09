from tkinter import *
from tkinter import ttk

from ttkthemes import ThemedTk


def sayiekle(dugme):
    if giris.get()=="Hatalı işlem!":
        giris.set("")

    giris.set(giris.get() + str(dugme))


def hesapla():
    try:
        sonuc = eval(giris.get())
        giris.set(sonuc)
    except:
        giris.set("Hatalı işlem!")

root = ThemedTk(theme="arc")
root.title("Gelişmiş Hesap Makinesi")
root.geometry("+1200+50")
root["bg"] = "#ababab"

giris = StringVar()

ttk.Entry(root, textvariable=giris).grid(row=0, column=0, columnspan=6, sticky=W + E)

for i in range(0, 9):
    ttk.Button(root, text=i + 1, command=lambda p=i+1: sayiekle(p)).grid(row=1 + i // 3, column=i % 3)

ttk.Button(root, text="0", command=lambda: sayiekle(0)).grid(row=4, column=0, columnspan=3, sticky=W + E)

ttk.Button(root, text="x", command=lambda: sayiekle("*")).grid(row=1, column=4, rowspan=2, sticky=N + S)
ttk.Button(root, text="+", command=lambda: sayiekle("+")).grid(row=3, column=4, rowspan=2, sticky=N + S)
ttk.Button(root, text="/", command=lambda: sayiekle("/")).grid(row=1, column=5, rowspan=2, sticky=N + S)
ttk.Button(root, text="-", command=lambda: sayiekle("-")).grid(row=3, column=5, rowspan=2, sticky=N + S)

ttk.Button(root, text="=", command=hesapla).grid(row=5, column=0, columnspan=6, sticky=E + W)

root.mainloop()
