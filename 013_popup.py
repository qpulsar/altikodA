from tkinter import *

pencere = Tk()
pencere.title("Diyalog penceresi")
pencere.geometry("300x100+1200+50")
pencere.resizable(width=False, height=False)
mesaj = Label(pencere, text="Programdan çıkmak istediğinize emin misiniz?")
mesaj.pack(side=TOP)
evet = Button(pencere, text="Evet", command=pencere.quit, bg="tomato")
evet["bg"] = "tomato"
evet.pack(side=LEFT, fill=X, expand=1)
hayir = Button(pencere, text="Hayır")
hayir.pack(side=LEFT, fill=X, expand=1)

pencere.mainloop()

# parse
