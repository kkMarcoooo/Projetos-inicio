from tkinter import *

root = Tk()

class Aplication():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        root.mainloop()
    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(background='#3F6492')
        self.root.geometry('700x500')
        self.root.resizable(True, True)
        self.root.maxsize(width=900,height=700)
        self.root.minsize(width=400,height=300)
    def frames_da_tela(self):
        self.frame1 = Frame(self.root, bd=4, bg= '#CDDAEA',
                            highlightbackground= '#D6A765', highlightthickness=3)
        self.frame1.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.45)
        self.frame2 = Frame(self.root, bd=4, bg= '#CDDAEA',
                            highlightbackground= '#D6A765', highlightthickness=3)
        self.frame2.place(relx=0.05, rely=0.5, relwidth=0.9, relheight=0.45)
Aplication()
