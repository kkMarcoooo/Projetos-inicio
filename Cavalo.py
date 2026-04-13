import random
import time
cavalos_nomes = ["Gordiço",  "Felipe", "Omni-man",   "Putrefação das trevas",   "Bob"]
saldo = 100.00
while True:
    cavalos = []
    maior = 0
    posicao = 0
    for i in range(5):
        velocidade = random.randint(7,20)
        cavalos.append(velocidade)
        if velocidade > maior:
            maior = velocidade
            posicao = i + 1
    #print(posicao)
    print(f"Saldo: R$ {saldo}")
    aposta = float(input("Valor da aposta: "))
    if aposta <= saldo:
        print("| [1] Gordiço | [2] Felipe | [3] Omni-man | [4] Putrefação das trevas | [5] Bob |")
        qual_cavalo = int(input("Escolha o cavalo: "))
        if qual_cavalo in range(1,6):
            saldo -= aposta
            if qual_cavalo == posicao:
                print("\033[32m\nWIN!\n\033[m")
                time.sleep(0.5)
                premio = aposta * 4
                saldo += premio
            print(f"Velocidade dos cavalos: \n")
            for i in range(5):
                if i+1 == posicao:
                    print(f"\033[31m [{i + 1}] {cavalos_nomes[i]}  - {cavalos[i]}km/h\033[m")
                else:
                    print(f" [{i + 1}] {cavalos_nomes[i]}  - {cavalos[i]}km/h")
            print("\n")
        else:
            print("\033[31mAPOSTA CANCELADA! SELECIONE UM CAVALO VÁLIDO!\033[m")
    else:
        print("\033[31mAPOSTA!SALDO INSUFICIENTE!\033[m")
    continue
