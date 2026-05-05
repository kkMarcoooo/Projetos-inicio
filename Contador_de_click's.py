import tkinter as tk

janela = tk.Tk()
contador = 0
texto_67 = None
def click():
    global contador, texto_67
    contador += 1
    texto.config(text=f"{contador} cliques")
    if contador == 67:
        texto_67 = tk.Label(janela, text="SEIS SETE SEIS SETE SEIS SETE")
        texto_67.place(relx=0.5,rely=0.8, anchor="center")
    if contador >67:
        if texto_67:
            texto_67.place_forget()
janela.config(background="#daff75")
janela.geometry('900x700')
janela.maxsize(width=1800, height=1800)
janela.minsize(width=400, height=300)

botao = tk.Button(
    janela,
    text = "Botão",
    command=click,
    bg="#bd1e1e",
    activebackground= "#e00000",
    font=("Arial", 20)
)
botao.place(relx=0.5, rely= 0.5, anchor="center")

titulo = tk.Label(janela,text= "Contador de cliques", bg="#daff75")
titulo.config(font=("Times New Roman", 20, "bold"))
titulo.place(relx=0.5, rely=0.15, anchor="center")

texto = tk.Label(janela, text = f"{0} cliques", bg="#fffbf0")
texto.config(font=("Arial", 20))
texto.place(relx=0.5, rely= 0.7, anchor="center")


janela.mainloop()
