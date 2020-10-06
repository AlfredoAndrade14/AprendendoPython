matrix = [[], [], []]
for l in range (0, 3):
  for c in range (0, 3):
    matrix[l].append(int(input(f'Insert [{l}, {c}]: ')))
print ()
for l in range (0,3):
  for c in range (0, 3):
    print (f'[{matrix[l][c]:^5}]', end = '')
  print()
