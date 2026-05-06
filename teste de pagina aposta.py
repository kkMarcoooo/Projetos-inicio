import random
import tkinter as tk
botao_option = 0
janela = tk.Tk()
cont = 0
saldo = 999.99
aposta = 0
n1 = None

def apostar():
    blank = []
    global cont
    global saldo
    cont = 0
    if botao_option != 0:
        if saldo > 0:
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
            saldo_texto.config(text=f"Saldo: R$ {saldo:.2f}")
def opcao1():
    global botao_option
    botao_option = 2
def opcao2():
    global botao_option
    botao_option = 4
def opcao3():
    global botao_option
    botao_option = 8
def opcao4():
    global botao_option
    botao_option = 16

opcao_1 =tk.Button(janela, text="R$ 2,00", command=opcao1)
opcao_2 = tk.Button(janela, text="R$ 4,00", command=opcao2)
opcao_3 = tk.Button(janela, text="R$ 8,00", command=opcao3)
opcao_4 = tk.Button(janela, text="R$ 16,00", command=opcao4)
opcao_1.place(relx=0.9, rely= 0.35, anchor="center")
opcao_2.place(relx=0.9, rely= 0.40, anchor="center")
opcao_3.place(relx=0.9, rely= 0.45, anchor="center")
opcao_4.place(relx=0.9, rely= 0.50, anchor="center")

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

avisos = tk.Label(janela, text="Selecione Valor Para Aposta!")
avisos.place(relx=0.5,rely=0.2, anchor="center")
avisos.config(font=("Arial", 12))

tk.Button(janela, text="Apostar", command=apostar).place(relx=0.5, rely= 0.6, anchor="center")

saldo_texto = tk.Label(janela, text=f"Saldo: R$ {saldo:.2f}")
saldo_texto.place(relx=0.05, rely=0.01)
saldo_texto.config(font=("Times New Roman", 12))

janela.config(background="#262626")
janela.minsize(width=900, height=700)
janela.mainloop()
