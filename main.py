#
# Nome(s): Nelson Dellosbel Junior
# Email(s) ou matrícula(s): 201072345
#
from time import sleep
import matplotlib.pyplot as plt
import matplotlib as mpl
import random
import math

# mpl.interactive(True)

print('-=' * 15)
print('\t\t  Tank Game')
print('-=' * 15)
print('Escolha seu nível de dificuldade:')
print('1 - Facíl')
print('2 - Médio')
print('3 - Difícil')
print('4 - HARDCORE')
print('-' * 30)
escolha = int(input('>> Sua escolha: '))

# INÍCIO da repetição externa (tentativas):

posx = abs(random.randint(100, 1000))

cont = 0

for c in range(1, 11):

    while abs(escolha) > 4 or escolha == 0:
        escolha = int(input('Escolha inválida! Digite novamente: '))

    if escolha == 4 and cont == 0:
        print('Ainda pode voltar atrás!')
        resp = input('Você tem certeza [S/N]? ').upper()
        if resp == 'N':
            print('É só pros fortes mesmo.')
            escolha = int(input('Escolha novamente: '))
        elif resp == 'S':
            print('Ok então, boa sorte!')
            sleep(1)
            print('\033[31mENTRANDO EM ZONA PERIGOSA...\033[m')
            sleep(3)

    listax = []
    listay = []

    g = 9.81

    if cont == 0:
        if escolha == 1:
            print('-' * 16)
            print(' \033[34m Nível Fácil\033[m')
            print('-' * 16)
            cont = 1
        elif escolha == 2:
            print('-' * 16)
            print(' \033[33m Nível Médio\033[m')
            print('-' * 16)
            cont = 1
        elif escolha == 3:
            print('-' * 16)
            print(' \033[35m Nível Difícil\033[m')
            print('-' * 16)
            cont = 1
        else:
            print('-' * 16)
            print(' \033[31mNÍVEL HARDCORE\033[m')
            print('-' * 16)
            cont = 1

    print(f'Tentativa {c}:')
    v0 = float(input('Velocidade inicial: '))
    angulo = float(input('Ângulo: '))
    ar = math.radians(angulo)
    y = 0
    t = 0
    p = t

    while y >= 0:
        x = v0 * math.cos(ar) * t
        y = v0 * math.sin(ar) * t - g * t ** 2 / 2
        listax.append(x)
        listay.append(y)
        t = t + 0.05

    plt.clf()

    plt.xlim(0, 1000)
    plt.ylim(0, 750)

    plt.ylabel("Altura")
    plt.xlabel("Distância")

    distancia = abs(posx - listax[-1])

    if escolha == 1 or escolha == 2:

        plt.plot(listax, listay)
        plt.plot(posx, 10, 'ro')
        plt.show()

        if escolha == 1:
            if distancia < 10:
                print('=' * 30)
                print('\t   >> VICTORY!! <<')
                print('=' * 30)
                print(f'Sua distância até o alvo foi de |{distancia:.2f}|')
                break

        elif escolha == 2:
            if distancia < 5:
                print('=' * 30)
                print('\t   >> VICTORY!! <<')
                print('=' * 30)
                print(f'Sua distância até o alvo foi de |{distancia:.2f}|')
                break

    elif escolha == 3:
        plt.plot(listax, listay)
        plt.show()

        if distancia < 100:
            print(f'Bahh!! Chegou perto! Sua distância é de {distancia:.2f} até o alvo.')
        elif distancia < 300:
            print(f'Ainda pode melhorar! Sua distância é de {distancia:.2f} até o alvo.')
        else:
            print(f'Ta muito frio ainda, mas tem chance! Sua distância é de {distancia:.2f} até o alvo.')

        if distancia < 2:
            plt.plot(posx, 10, 'ro')
            plt.show()
            print('=' * 30)
            print('\t   >> VICTORY!! <<')
            print('=' * 30)
            print('Uauu! Você conseguiu no modo difícil, parabéns!!')
            print(f'Sua distância até o alvo foi de |{distancia:.2f}|')
            break
    else:
        plt.plot(posx, 10, 'ro')
        plt.show()

        if distancia > 500:
            print('A sua distância até o alvo é maior que 500')
        elif distancia > 300:
            print('A sua distância até o alvo é maior que 300 e menor que 500')
        elif distancia > 100:
            print('A sua distância até o alvo é maior que 100 e menor que 300')
        elif distancia < 100:
            print('A sua distância até o alvo é menor que 100')
        if c == 5:
            print(f'Sua distância até o alvo foi de |{distancia:.2f}|')
            break

        if distancia < 1:
            print('\033[31mUSAR HACK NÃO É PERMITIDO!\033[m')

input("ENTER para finalizar")
print()
print('Finalizando...')
sleep(3)
print()
print('**Obrigado por jogar, volte sempre!**')
plt.close()
