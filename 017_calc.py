from tkinter import *


def topla():
    s3.set(str(int(s1.get()) + int(s2.get())))


def cikar():
    s3.set(str(int(s1.get()) - int(s2.get())))


def carp():
    s3.set(str(int(s1.get()) * int(s2.get())))


def bol():
    s3.set(str(int(s1.get()) / int(s2.get())))


root = Tk()
root.title("Hesap Makinesi")
root.geometry("300x300+1200+50")

s1 = StringVar()
s2 = StringVar()
s3 = StringVar()
Entry(textvariable=s1).pack()
Entry(textvariable=s2).pack()

f = Frame(root)
Button(f, text="+", command=topla).pack(side=LEFT, expand=True, fill=X)
Button(f, text="-", command=cikar).pack(side=LEFT, expand=True, fill=X)
Button(f, text="*", command=carp).pack(side=LEFT, expand=True, fill=X)
Button(f, text="/", command=bol).pack(side=LEFT, expand=True, fill=X)
f.pack(expand=True, fill=X)
Label(textvariable=s3).pack()
root.mainloop()
