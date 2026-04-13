import random
import time
dificuldade = 1
saldo = 300.00
v1 = 7
v2 = 20
valor_aposta = 3
def processar_aposta(saldo, aposta, qual_cavalo, posicao, cavalos_nomes, cavalos):
    saldo -= aposta
    if qual_cavalo == posicao:
        print("\033[32m\nWIN!\n\033[m")
        time.sleep(0.5)
        premio = aposta * 3
        saldo += premio

    print(f"Velocidade dos cavalos: \n")
    for i in range(len(cavalos_nomes)):
        if i + 1 == posicao:
            print(f"\033[31m [{i + 1}] {cavalos_nomes[i]}  - {cavalos[i]}km/h\033[m")
        else:
            print(f" [{i + 1}] {cavalos_nomes[i]}  - {cavalos[i]}km/h")
    print("\n")
    return saldo
while True:
    if dificuldade == 1:
        cavalos_nomes = ["Gordiço", "Felipe", "Omni-man"]
    elif dificuldade == 2:
        cavalos_nomes = ["Gordiço", "Felipe", "Omni-man", "Putrefação das trevas", "Bob",]
    else:
        cavalos_nomes = ["Gordiço", "Felipe", "Omni-man", "Putrefação das trevas", "Bob", "Cabra do Wordskill", "Calabreso", "Vivi cardoso"]
    cavalos = []
    maior = 0
    posicao = 0
    for i in range(len(cavalos_nomes)):
        velocidade = random.randint(v1,v2)
        cavalos.append(velocidade)
        if velocidade > maior:
            maior = velocidade
            posicao = i + 1
    #print(posicao)
    print(f"Saldo: R$ {saldo}")
    aposta = float(input("Valor da aposta: "))
    if aposta == 67.6701:
        dificuldade = int(input("|[1] Fácil | [2] Médio | [3] Difícil|\nDificuldade: "))
        if dificuldade == 1:
            v1 = 7
            v2 = 20
            valor_aposta = 3
        if dificuldade == 2:
            v1 = 10
            v2 = 30
            valor_aposta = 4
        if dificuldade == 3:
            v1 = 30
            v2 = 70
            valor_aposta = 7
    elif aposta <= saldo:
        if dificuldade == 1:
            print("| [1] Gordiço | [2] Felipe | [3] Omni-man |")
        if dificuldade == 2:
            print("| [1] Gordiço |  [2] Felipe | [3] Omni-man | [4] Putrefação das trevas | [5] Bob |")
        if dificuldade == 3:
            print("| [1] Gordiço |  [2] Felipe | [3] Omni-man | [4] Putrefação das trevas | [5] Bob | [6] | Cabra do Wordskill | [7] Calabreso | [8] Vivi cardoso")
        qual_cavalo = int(input("Escolha o cavalo: "))
        if dificuldade == 1:
            if qual_cavalo in range(1, 4):
                saldo = processar_aposta(saldo, aposta, qual_cavalo, posicao, cavalos_nomes, cavalos)
            else:
                print("\033[31mAPOSTA CANCELADA! SELECIONE UM CAVALO VÁLIDO!\033[m")
        if dificuldade == 2:
            if qual_cavalo in range(1, 6):
                saldo = processar_aposta(saldo, aposta, qual_cavalo, posicao, cavalos_nomes, cavalos)
            else:
                print("\033[31mAPOSTA CANCELADA! SELECIONE UM CAVALO VÁLIDO!\033[m")
        if dificuldade == 3:
            if qual_cavalo in range(1, 9):
                saldo = processar_aposta(saldo, aposta, qual_cavalo, posicao, cavalos_nomes, cavalos)
            else:
                print("\033[31mAPOSTA CANCELADA! SELECIONE UM CAVALO VÁLIDO!\033[m")

    else:
        print("\033[31mAPOSTA!SALDO INSUFICIENTE!\033[m")
    continue
