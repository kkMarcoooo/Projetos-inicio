import random
import time
saldo = 100.00
while True:
    jackpot = []
    ganhar = 0
    aposta = float(input(f"Saldo = R$ {saldo:.2f}\nValor da aposta: "))
    if aposta > saldo:
        print("!SALDO INSUFICIENTE!")
        continue
    else:
        saldo -= aposta
        for i in range(3):
            n1 = random.randint(1,4)
            jackpot.append(n1)
    print("\n=-=-=-=-=-=-=-=-=-=-=")
    emojis = ["🎃", "❤", "🥸", "👾"]
    for k in range(12):
        e1 = random.choice(emojis)
        e2 = random.choice(emojis)
        e3 = random.choice(emojis)
        print(f"\r | {e1} | {e2} | {e3} |", end=" ", flush=True)
        time.sleep(0.2)
        print(f"\r ", end=" ",flush=True)
    for i in jackpot:
        if i == 1:
            emoji = "🎃"
        elif i == 2:
            emoji = "❤"
        elif i == 3:
            emoji = "🥸"
        else:
            emoji = "👾"
        print(f"| {emoji}", end=" ", flush= True)
    print("|")
    print("=-=-=-=-=-=-=-=-=-=-=")
    if jackpot[0] == jackpot[1] == jackpot[2]:
        ganhar+=1
        premio = aposta*4
        saldo += premio
        print("\nWIN")
    continue