#Jogo dos 21 fósforos

import random

print("Bem vindo ao jogo dos fósforos! Existem 21 fósforos e, cada jogador pode tirar, na sua vez, entre 1 a 4 fósforos. Quem tirar o último fósforo perde!")

n = 21
print("Quem joga primeiro? (1=jogador, 2=computador)")
start = int(input("Quem joga primeiro? (1=jogador, 2=computador):"))
while n > 1:
    if start == 1:
        print("É o primeiro a retirar.")
        while n > 1:
            jogada = int(input("Quantos fósforos quer retirar, de 1 a 4?:"))
            if jogada>=1 and jogada<=4:
                n=n-jogada
                print(f"Tirou {jogada} fósforos. Sobram {n}.")
                computador = int(5-jogada)
                n=n-computador
                print(f"O computador retira {computador} fósforos e ficam {n} fósforos.")
            elif jogada<1 or jogada>4:
                print("Tenta de novo. Só vale de 1 a 4!")     
        print("Perdeu, sobrou um fósforo!")
    elif start == 2:
        print("O computador é primeiro a retirar.")
        computador = (random.randint(1,4))
        n=n-computador
        print(f"O computador retirou {computador} fósforos. Sobram {n}.")
        while n > 1:
            jogada = int(input("Quantos fósforos quer retirar, de 1 a 4?:"))
            if jogada>=1 and jogada<=4:
                n=n-jogada
                print(f"Tira {jogada} fósforos e ficam {n} fósforos.")
                if n > 5:
                    computador=jogada%5
                    if computador==0:
                        computador=(random.randint(1,4))
                    n=n-computador            
                    print(f"O computador retirou {computador} fósforos. Sobram {n}.")
                    if n==1:
                        print("Perdeu! O computador deu a volta.")
                elif 1<n<=5:
                    computador=n-1
                    n=n-computador
                    print(f"O computador retirou {computador} fósforos. Sobram {n}.")
                    print("Perdeu! O computador deu a volta.")
                elif n == 1:
                    print("Ganhou!")
            elif jogada<1 or jogada>4:
                print("Tenta de novo. Só vale de 1 a 4!")
    else:
        print("Resposta inválida")
        print("Quem joga primeiro? (1=jogador, 2=computador)")
        start = int(input("Quem joga primeiro? (1=jogador, 2=computador):"))
    