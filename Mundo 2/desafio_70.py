total = 0
maiorQueMil = 0
cont = 1
menor = 0

while True:
  nome = input("Nome produto: ")
  valor = int(input("Valor produto: "))
  op = input("0 para sair: ")
  
  if(cont == 1):
    menor = valor


  if(valor < menor):
    menor = valor
  
  if(valor > 1000):
    maiorQueMil += 1

  total += valor
  if(op == "0"):
    break


print("""Produto mais barato: R${}
Valor total da compra: R${}
Total de proutos mais caros que R$1000: {}""".format(menor, total, maiorQueMil))
