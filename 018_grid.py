from tkinter import *
from tkinter import ttk

from ttkthemes import ThemedTk

root = ThemedTk(theme="blue")
root.title("Gelişmiş Hesap Makinesi")
root.geometry("+1200+50")
root["bg"]="#ababab"

giris = StringVar()

ttk.Entry(root, textvariable=giris).grid(row=0, column=0, columnspan=4, sticky=W+E)
ttk.Button(root, text="1").grid(row=1, column=0)
ttk.Button(root, text="2").grid(row=1, column=1)
ttk.Button(root, text="3").grid(row=1, column=2)
ttk.Button(root, text="4").grid(row=2, column=0)
ttk.Button(root, text="5").grid(row=2, column=1)
ttk.Button(root, text="6").grid(row=2, column=2)
ttk.Button(root, text="7").grid(row=3, column=0)
ttk.Button(root, text="8").grid(row=3, column=1)
ttk.Button(root, text="9").grid(row=3, column=2)


root.mainloop()

