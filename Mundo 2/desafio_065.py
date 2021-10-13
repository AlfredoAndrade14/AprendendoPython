menor = 0
maior = 0
total = 0
vezes = 0

while True:
  num = int(input("Numero [0 para sair]: "))
  if num == 0:
    break
  if vezes == 0:
    maior = num
    menor = num
  
  if num < menor:
    menor = num
  if num > maior:
    maior = num
  
  total += num
  vezes += 1

media = total / vezes
print("""menor: {}
maior: {}
media: {} """.format(menor, maior, media))
