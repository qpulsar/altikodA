from tkinter import *

root = Tk()
root.title("Frame")
root.geometry("300x300+1200+50")

alan1 = Frame(root, borderwidth=4, bg="steelblue", relief=RAISED)
metin1 = Label(alan1, text="Merhaba- Ben alan1'deyim")
metin1.pack(side=LEFT)
alan1.pack(fill=BOTH, expand=True)

alan2 = Frame(root, borderwidth=4, bg="bisque",relief=SUNKEN)
metin2 = Label(alan2, text="Merhaba- Ben alan1'deyim")
metin2.pack()
alan2.pack(fill=BOTH, expand=True)

root.mainloop()
