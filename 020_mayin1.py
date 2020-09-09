from tkinter import *
import random

root = Tk()
root.geometry("400x440+1200+50")
root.title("Mayın tarlası 1")


ust = Frame(root, bg="lightskyblue2")
lbl_kalan = Label(ust, text="Kalan", width=5, height=2)
lbl_kalan.pack(side=LEFT,  anchor="center")

lbl_gulen = Label(ust, text=":)", width=1, height=2)
lbl_gulen.pack(side=LEFT, anchor="center")

lbl_sure = Label(ust, text="0", width=5, height=2)
lbl_sure.pack(side=RIGHT, anchor="center")

ust.pack(side=TOP, fill=X)

alt = Frame(root, bg="red")
alt.pack(side=TOP, fill=BOTH)

res_bos = PhotoImage(file="./img/bos.png")
for satir in range(0,10):
    for sutun in range(0,10):
        label = Label(alt, image=res_bos, relief=SUNKEN)
        label.grid(row=satir, column=sutun)

root.mainloop()

