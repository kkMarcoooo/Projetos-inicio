import random
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
            n1 = random.randint(1,3)
            jackpot.append(n1)
    print("\n=-=-=-=-=-=-=-=-=")
    for i in jackpot:
        if i == 1:
            emoji = "🎃"
        if i == 2:
            emoji = "❤"
        if i == 3:
            emoji = "🥸"
        print(f"| {emoji}", end=" ")
    print("|")
    print("=-=-=-=-=-=-=-=-=")
    if jackpot[0] == jackpot[1] == jackpot[2]:
        ganhar+=1
        premio = aposta*4
        saldo += premio
        print("\nWIN")
    continue