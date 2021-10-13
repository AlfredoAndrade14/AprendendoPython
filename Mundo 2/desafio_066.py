soma = 0
total = 0
while True:
  num = int(input())
  if num == 999:
    break
  total += 1
  soma += num
print("""total de tentativas: {}
soma dos números: {}""".format(total, soma) )
 
