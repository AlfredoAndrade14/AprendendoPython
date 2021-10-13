primeiro = int(input("primeiro termo: "))
razao = int(input("razao: "))
pos = 1
while True:
  conta = primeiro + (pos - 1) * razao
  print("a{} = {}".format(pos, conta))
  if(pos == 10):
    break
  pos += 1
  
