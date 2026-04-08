import random
import time
cavalos = []
saldo = 100.00
maior = 0
posicao = 0
while True:
    for i in range(5):
        cavalos.append(random.randint(7,20))
    for k in cavalos:
        if k == 0 or k > maior:
            maior = k
            posicao += 1
    print(f"Saldo: R$ {saldo}")
    aposta = float(input("Valor da aposta: "))
    if aposta < saldo:
        print("| [1] Gordiço | [2] Felipe | [3] Omni-man | [4] Putrefação das trevas | [5] Bob |")
        qual_cavalo = int(input("Escolha o cavalo: "))
        if qual_cavalo in range(1,6):
            saldo -= aposta
            if qual_cavalo == posicao:
                print("\033[32m\nWIN!\n\033[m")
                time.sleep(0.5)
                premio = aposta * 3
                saldo += premio
            print(f"Velocidade dos cavalos: \n")
            for i in range(5):
                print(f" [{i + 1}] {cavalos[i]}km/h")
            print("\n")
        else:
            print("\033[31mAPOSTA CANCELADA! SELECIONE UM CAVALO VÁLIDO!\033[m")
    else:
        print("\033[31mAPOSTA!SALDO INSUFICIENTE!\033[m")
    continue