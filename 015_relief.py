from tkinter import *

desenler = [GROOVE, SOLID, RAISED, FLAT, SUNKEN, RIDGE]
root = Tk()
root.title("Frame Relief")
root.geometry("800x300+1200+20")

for satir in range(0, 5):
    dis_frame = Frame(root, borderwidth=3, relief=GROOVE)
    lbl = Label(dis_frame, text="Kalınlık:{}".format(satir))
    lbl.pack(side=LEFT)
    for r in desenler:
        ic_frame = Frame(dis_frame, borderwidth=satir, relief=r)
        Button(ic_frame, text=r).pack(side=LEFT)
        ic_frame.pack(side=LEFT, expand=True, fill=X)

    dis_frame.pack(expand=True, fill=X)
root.mainloop()
