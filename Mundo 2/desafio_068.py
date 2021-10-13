from random import randint

while True:
  numero = int(input("valor: "))
  escolha = input("escolha [P/I]: ")
  escolhaPc = randint(1, 100)
  soma = numero + escolhaPc
  if(soma%2 == 0 and escolha == "P"):
    print("Computador escolheu {}, você ganhou".format(escolhaPc))
  else:
    print("Computador escolheu {}, você perdeu".format(escolhaPc))
    break
