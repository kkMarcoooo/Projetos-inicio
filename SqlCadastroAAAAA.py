import sqlite3
conexao = sqlite3.connect("Banco_dados_legal.db")
funcio = conexao.cursor()
funcio.execute("""
    CREATE TABLE IF NOT EXISTS login(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL,
        senha TEXT NOT NULL
)    
""")
def cadastro():
    while True:
        print("--== CADASTRO ==--")
        e = email()
        s = senha()
        funcio.execute("INSERT INTO login(email,senha) VALUES (?,?)", (e,s))
        conexao.commit()
        print("Usuário Cadastrado!")
        continuar = str(input("Continuar? [S/N]: ").upper())
        if continuar == "S":
            continue
        else:
            break
def login():
    while True:
        print("--== LOGIN ==--")
        confirmar_email = confi_email()
        if confirmar_email:
            email_encontrado = confirmar_email[0]
            login_certo = confi_senha(email_encontrado)
            if login_certo:
                print("Bem VIndo ao Sistema!")
        else:
            print("Email não encontrado no sistema.")
def email():
    while True:
        email = str(input("Email: "))
        if email.endswith(("@gmail.com", "@yahoo.com", "@outlook.com", "@hotmail.com")):
            return email
        print("Insira email válido!")
def senha():
    while True:
        senha = str(input("Senha: "))
        senhanums = len(senha)
        if senhanums >= 6 and senhanums <= 20:
            senhaconf = str(input("Confirme a senha: "))
            if senhaconf == senha:
                return senha
            print("Senhas não coincidem!")
        else:
            print("Digite uma senha de 6 á 20 carateres!")
def confi_email():
    emailLogin = str(input("Email: "))
    funcio.execute("SELECT email FROM login WHERE email = ?",(emailLogin,))
    return funcio.fetchone()
def confi_senha(emailLogin):
    tentativa = 3
    funcio.execute("SELECT senha FROM login WHERE email = ?", (emailLogin,))
    usuario = funcio.fetchone()
    if usuario is None:
        print("Usuário não encontrado.")
        return False
    senha = usuario[0]
    while tentativa > 0:
        senhalogin = str(input("Senha: "))
        if senhalogin == senha:
            print("LOGIN CONCEDIDO!")
            return True
        if tentativa > 0:
            tentativa-=1
            print(f"SENHA INCORRETA! Você tem {tentativa} tentativas restantes!")
        else:
            print("Aceso bloqueado!")
while True:
    print("\n--- SISTEMA DE ACESSO ---")
    print("1. Cadastrar Novo Usuário")
    print("2. Fazer Login")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        cadastro()
    elif opcao == "2":
        login()
    elif opcao == "3":
        print("Saindo...")
        conexao.close()
        break
    else:
        print("Opção inválida!")
