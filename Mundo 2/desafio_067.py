while True:
  num = int(input("Tabuada do número: "))
  if num == 0:
    break
  for c in range(10):
    print("{} x {} = {}".format(num, (c + 1), num*(c + 1)))
 
