from tkinter import *
from tkinter import ttk

from ttkthemes import ThemedTk

root = ThemedTk(theme="blue")
root.title("Gelişmiş Hesap Makinesi")
root.geometry("+1200+50")
root["bg"] = "#ababab"

giris = StringVar()

ttk.Entry(root, textvariable=giris).grid(row=0, column=0, columnspan=5, sticky=W + E)

for i in range(0, 9):
    ttk.Button(root, text=i+1).grid(row=1 + i // 3, column=i % 3)

ttk.Button(root, text="x").grid(row=1, column=4, rowspan=2)
root.mainloop()
