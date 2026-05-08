import  tkinter as tk
janela = tk.Tk()
janela.minsize(width=900, height=700)
janela.title("Cadastro Com Retorno")
def dados():
    global requer
    dado = entrada.get().strip()
    if dado == "":
        requer=tk.Label(janela, text="*PREENCHA TODOS OS CAMPOS*", fg="red")
        requer.place(relx=0.5, rely=0.7, anchor="center")
    else:
        dado = tuple(dado.split(","))
        print(f"Tupla: {dado}")
        try:
            requer.place_forget()
        except:
            pass
entrada = tk.Entry(janela)
entrada.place(relx=0.5, rely=0.5, anchor="center")

botao_salvar = tk.Button(janela, text="Enviar",command=dados)
botao_salvar.place(relx=0.6,rely=0.5, anchor="center")

janela.mainloop()
