#maior e menor valor

import random 

numeros = (random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)) 

print (f'os números sorteados foram: {numeros}')   
print (f'o maior valor sorteado foi {max(numeros)}') 
print (f'o menor valor sorteado foi {min(numeros)}')
