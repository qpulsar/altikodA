from tkinter import *
import random


def uzerinde(olay):
    bizim_label = olay.widget
    if bizim_label["text"] != "b":
        bizim_label["image"] = res_qm


def disinda(kim):
    bizimki = kim.widget
    if bizimki["image"] != res_bom:
        return 
    if bizimki["text"] != "b":
        bizimki["image"] = res_bos

def tikla(w):
    lab = w.widget
    if lab["text"] == "b":
        return
    sa = int(lab["text"])
    if sa in mayinlar:
        lab["image"] = res_bom
        kalan_sayisi = -1
    else:
        lab["image"] = ""
        lab["text"] = "b"


root = Tk()
root.geometry("440x480+1200+50")
root.title("Mayın tarlası 1")

ust = Frame(root, bg="lightskyblue2")
lbl_kalan = Label(ust, text="Kalan", width=5, height=2)
lbl_kalan.pack(side=LEFT, anchor="center")

lbl_gulen = Label(ust, text=":)", width=1, height=2)
lbl_gulen.pack(side=LEFT, anchor="center")

lbl_sure = Label(ust, text="0", width=5, height=2)
lbl_sure.pack(side=RIGHT, anchor="center")

ust.pack(side=TOP, fill=X)

alt = Frame(root, bg="red")
alt.pack(side=TOP, fill=BOTH)

res_bos = PhotoImage(file="./img/bos.png")
res_bom = PhotoImage(file="./img/bom.png")
res_qm = PhotoImage(file="./img/qm.png")

# Mayın yerleştir
mayinlar = []
mayin_sayisi = 20
kalan_sayisi = mayin_sayisi

for i in range(0, mayin_sayisi):
    tmp = random.randrange(0, 100)
    while tmp in mayinlar:
        tmp = random.randrange(0, 100)
    mayinlar.append(tmp)

print(mayinlar)

sira = 0
for satir in range(0, 10):
    for sutun in range(0, 10):
        label = Label(alt, image=res_bos, relief=SUNKEN, text=sira)
        label.grid(row=satir, column=sutun)
        label.bind("<Enter>", uzerinde)
        label.bind("<Leave>", disinda)
        label.bind("<Button-1>", tikla)
        sira += 1

root.mainloop()
