from tkinter import *

root = Tk()
root.title("Login Page")
root.geometry("300x250+1200+50")

isim_degiskeni = StringVar()
pass_degiskeni = StringVar()
Label(root, text="İsminizi giriniz").pack()
isim = Entry(root, textvariable=isim_degiskeni)
isim.pack()
Label(root, text="Parolanızı giriniz").pack()
parola = Entry(root, textvariable=pass_degiskeni)
parola.pack()

buton = Button(root, text="Login")
buton.pack()


root.mainloop()
