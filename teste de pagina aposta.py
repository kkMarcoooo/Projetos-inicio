import random
import tkinter as tk
from pydoc import text

botao_option = 0
janela = tk.Tk()
cont = 0
saldo = 999.99
aposta = 0
n1 = None

def apostar():
    blank = []
    global cont
    global saldo, avisos
    cont = 0
    if botao_option != 0:
        if saldo > 0:
            status.config(text="Perdeu!", bg="#fff3c2")
            aposta = botao_option
            saldo -= aposta
            for i in range(3):
                n1 = random.randint(1,3)
                blank.append(n1)
            for i in blank:
                cont+=1
                if i == 1:
                    if cont == 1:
                        texto1.config(text="😎", bg="#ffeca1")
                    if cont == 2:
                        texto2.config(text="😎", bg="#ffeca1")
                    if cont == 3:
                        texto3.config(text="😎", bg="#ffeca1")
                if i == 2:
                    if cont == 1:
                        texto1.config(text="🎶", bg="#ffeca1")
                    if cont == 2:
                        texto2.config(text="🎶", bg="#ffeca1")
                    if cont == 3:
                        texto3.config(text="🎶", bg="#ffeca1")
                if i == 3:
                    if cont == 1:
                        texto1.config(text="💖", bg="#ffeca1")
                    if cont == 2:
                        texto2.config(text="💖", bg="#ffeca1")
                    if cont == 3:
                        texto3.config(text="💖", bg="#ffeca1")
            if blank[0] == blank[1] == blank[2]:
                saldo = saldo + aposta * 4
                status.config(text=f"JACKPOT!!!\n+ R$ {aposta*4:.2f}", bg="#64c94b")
            saldo_texto.config(text=f"Saldo: R$ {saldo:.2f}")

def opcao1():
    global botao_option
    botao_option = 2
    avisos.config(text="Selecionado: R$ 2,00")
    avisos.config(font=("Arial", 15))
def opcao2():
    global botao_option
    avisos.config(text="Selecionado: R$ 4,00")
    botao_option = 4
    avisos.config(font=("Arial", 15))
def opcao3():
    global botao_option
    botao_option = 8
    avisos.config(text="Selecionado: R$ 8,00")
    avisos.config(font=("Arial", 15))
def opcao4():
    global botao_option
    botao_option = 16
    avisos.config(text="Selecionado: R$ 16,00")
    avisos.config(font=("Arial", 15))

tk.Frame(janela,bd=4, bg="#c41b1b", highlightbackground= '#fac355', highlightthickness=3).place(relx=0.9, rely=0.4, relwidth=0.15, relheight=0.5, anchor="center")

frame_titulo = tk.Frame(janela, bd=4, bg="black", highlightbackground= 'gold', highlightthickness=3).place(relx=0.5, rely=0.02, relwidth=1.1, relheight=0.15, anchor="center")
frame_rodape = tk.Frame(janela, bd=4, bg="black", highlightbackground= 'gold', highlightthickness=3).place(relx=0.5, rely=1, relwidth=1.1, relheight=0.15, anchor="center")


titulo = tk.Label(janela,text="~ Pequeno Tigre 🐯🎲 ~", bg="black", fg="#fac355")
titulo.place(relx=0.5, rely=0.05, anchor="center")
titulo.config(font=("Comic Sans MS", 25))

opcao_1 =tk.Button(janela, text="R$ 2,00", command=opcao1, fg="white",bg="#a3a0a0", activeforeground="yellow", activebackground="#525252")
opcao_1.config(font=("Arial", 12))

opcao_2 = tk.Button(janela, text="R$ 4,00", command=opcao2, fg="white",bg="#a3a0a0", activeforeground="yellow", activebackground="#525252")
opcao_2.config(font=("Arial", 12))

opcao_3 = tk.Button(janela, text="R$ 8,00", command=opcao3, fg="white",bg="#a3a0a0", activeforeground="yellow", activebackground="#525252")
opcao_3.config(font=("Arial", 12))

opcao_4 = tk.Button(janela, text="R$ 16,00", command=opcao4, fg="white",bg="#a3a0a0", activeforeground="yellow", activebackground="#525252")
opcao_4.config(font=("Arial", 12))

opcao_1.place(relx=0.9, rely= 0.25, relwidth=0.1, relheight=0.07, anchor="center")
opcao_2.place(relx=0.9, rely= 0.35, relwidth=0.1, relheight=0.07, anchor="center")
opcao_3.place(relx=0.9, rely= 0.45, relwidth=0.1, relheight=0.07, anchor="center")
opcao_4.place(relx=0.9, rely= 0.55, relwidth=0.1, relheight=0.07, anchor="center")

tk.Frame(janela,bd=4, bg="#ffeca1", highlightbackground= '#D6A765', highlightthickness=3).place(relx=0.30, rely=0.35, relwidth=0.4, relheight=0.1)

texto1 = tk.Label(janela, text="⬛", bg="#ffeca1")
texto1.config(font=("Arial",20))
texto1.place(relx=0.35, rely= 0.4,   anchor="center")

texto2 = tk.Label(janela, text="⬛", bg="#ffeca1")
texto2.config(font=("Arial",20))
texto2.place(relx=0.5, rely= 0.4, anchor="center")

texto3 = tk.Label(janela, text="⬛", bg="#ffeca1")
texto3.config(font=("Arial",20))
texto3.place(relx=0.65, rely= 0.4, anchor="center")

avisos = tk.Label(janela, text="Selecione Valor Para Aposta!", fg="#fac355", bg="#000000")
avisos.place(relx=0.5,rely=0.2, anchor="center")
avisos.config(font=("Arial", 15))

status = tk.Label(janela, text="-  -  -  -  -  -")
status.place(relx=0.5,rely=0.5, anchor="center")
status.config(font=("Arial", 14))

sobre = tk.Label(janela, text="1° Cassino Honesto 100% Honesto\nSELO DE HONESTIDADE DA O.N.U: ✅✅✅", fg="white", bg="black")
sobre.place(relx=0.5,rely=0.965, anchor="center")
sobre.config(font=("Courier New", 7))

tk.Button(janela, text="Apostar", command=apostar, fg="white",bg="#ff2b2b", activeforeground="yellow", activebackground="#c22121").place(relx=0.5, rely= 0.6,relwidth=0.08, relheight=0.08, anchor="center")
saldo_texto = tk.Label(janela, text=f"Saldo: R$ {saldo:.2f}")
saldo_texto.place(relx=0.04, rely=0.12)
saldo_texto.config(font=("Times New Roman", 12))

janela.config(background="#262626")
janela.minsize(width=900, height=700)
janela.mainloop()
