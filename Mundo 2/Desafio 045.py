from random import randint
from time import sleep
itens = ('Pedra', 'Tesoura', 'Papel')
print('''Vamos jogar Jokenpo!
Escolha sua jogada:
[ 0 ] para Pedra
[ 1 ] para tesoura
[ 2 ] para papel''')
e= int(input('Qual será sua jogada? '))
computador= randint(0, 2)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!!!!!')
sleep(1)
print('*'*31)
print('O Jogador escolheu {}!'.format(itens[e]))
print('O Computador escolheu {}!'.format(itens[computador]))
print('*'*31)

if computador == 0:  # CPU jogou pedra
    if e == 0:
        print('Empate')
    elif e == 1:
        print('O jogador PERDEU')
    elif e == 2:
        print('O jogador GANHOU')
    else:
        print('Jogada inválida.')
elif computador == 1:  # CPU jogou tesoura
    if e == 0:
        print('O jogador VENCEU')
    elif e == 1:
        print('Empate')
    elif e == 2:
        print('O jogador PERDEU')
    else:
        print('Jogada inválida.')
elif computador == 2:  # CPU jogou papel
    if e == 0:
        print('O jogador PERDEU!')
    elif e == 1:
        print('O jogador VENCEU')
    elif e == 2:
        print('Empate')
    else:
        print('Jogada inválida.')
