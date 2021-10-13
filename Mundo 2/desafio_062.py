primeiro = int(input("primeiro termo: "))
razao = int(input("razao: "))
pos = 1
total = 10
while True:
  conta = primeiro + (pos - 1) * razao
  print("a{} = {}".format(pos, conta))
  if(pos == total):
    opcao = int(input("Mais? 0 para sair "))
    total += opcao
    if(opcao == 0):
      break
  pos += 1
  
