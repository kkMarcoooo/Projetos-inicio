import random
import time
num = random.randint(1,3)
print("=" * 5 + "\n⚫\n⚫\n⚫\n" + "=" * 5)
num = random.randint(1, 3)
time.sleep(2)
saldo = 5
while True:
    aposta = 0
    num = random.randint(1, 3)
    print(f"Saldo: {saldo}")
    aposta = float(input("Digite o valor da aposta: "))
    if saldo < aposta:
        print("saldo insuficiente!")
        continue
    else:
        saldo -= aposta
        cor = int(input("Qual cor vai cair?\n[1] Verde | [2] Amarelo | [3]  Vermelho\nChute: "))
        if num == 1:
            print("\n🟢\n⚫\n⚫\n")
        if num == 2:
            print("\n⚫\n🟡\n⚫\n")
        if num == 3:
            print("\n⚫\n⚫\n🔴\n")
    if cor == num:
        aposta += aposta * 2
        saldo += aposta