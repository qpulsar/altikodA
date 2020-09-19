from tkinter import *

uname = "e"
upass = "a"


def ekle(event):
    global madde_degiskeni, liste
    liste.insert(0, madde_degiskeni.get())
    madde_degiskeni.set("")


def kontrol():
    global madde_degiskeni, liste
    madde_degiskeni = StringVar()
    if uname == isim_degiskeni.get() and upass == pass_degiskeni.get():
        yeni_pencere = Toplevel(root)
        yeni_pencere.title("Asıl program")
        yeni_pencere.geometry("300x300+1300+100")
        root.withdraw()
        madde = Entry(yeni_pencere, textvariable=madde_degiskeni)
        madde.bind('<Return>', ekle)
        madde.pack()
        liste = Listbox(yeni_pencere)
        liste.pack()
    else:
        print("Sen kimsin!")


root = Tk()
root.title("Login Page")
root.geometry("300x250+1200+50")

isim_degiskeni = StringVar()
pass_degiskeni = StringVar()
Label(root, text="İsminizi giriniz").pack()
isim = Entry(root, textvariable=isim_degiskeni)
isim.pack()
Label(root, text="Parolanızı giriniz").pack()
parola = Entry(root, textvariable=pass_degiskeni, show="*")
parola.pack()

buton = Button(root, text="Login", command=kontrol)
buton.pack()

root.mainloop()
