todos_lista = []
lista_pares = []
lista_impares = []

while True:
    res = input("Deseja adicionar um número?[S/N] ").strip().capitalize()
    if res == 'N':
        break
    else:
        num = int(input('Digite um número: '))
        todos_lista.append(num)

for numero in todos_lista:
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)
        
print(f'Lista completa: {todos_lista} \nA lista de pares: {lista_pares} \nA lista de ímpares: {lista_impares}')
