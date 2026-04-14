import time
def email():
    while True:
        email = str(input("Email: "))
        if email.endswith(("@gmail.com", "@outlook.com", "@hotmail.com")):
            return email
        print("Insira um email válido!")
def senha():
    while True:
        senha = str(input("Senha: "))
        if len(senha) >= 6 and len(senha) <= 20:
            senha_conf = str(input("Confirmar senha: "))
            if senha_conf == senha:
                return senha
            print("Senhas não coincidem!")
        else:
            print("Insira uma senha de 6 a 20 caracteres!")
def confirmar_email(email):
    while True:
        confirmar_email = str(input("Email: "))
        if confirmar_email == email:
            return True
        print("Usuário não encontrado!")
def confirmar_senha(senha):
    tentativas = 3
    while tentativas > 0:
        confirmar_senha= str(input("Senha: "))
        if confirmar_senha == senha:
            print("LOGIN CONCEDIDO!")
            return True
        tentativas -= 1
        if tentativas > 0:
            print(f"Senha Incorreta! Você tem {tentativas} tentativas")
        else:
            print("MÁXIMO DE TENTATIVAS USADAS! TENTE NOVAMENTE EM 2 HORAS...")
            return False
email_register = email()
password_register = senha()
direcionar = str(input("Continuar para o sistema de login? (Sim ou Não): ").upper().strip())
if direcionar == "SIM":
    print("carregando...")
    time.sleep(2)
    print("\n---===LOGIN===---\n")
    login_email = confirmar_email(email_register)
    login_senha = confirmar_senha(password_register)
else:
    print("PROGRAMA ENCERRADO!")
