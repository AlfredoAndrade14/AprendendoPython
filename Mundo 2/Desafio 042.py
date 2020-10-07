print('Condição de existência de um triângulo')
a=float(input('Primeiro segmento: '))
b=float(input('Segundo segmento: '))
c=float(input('Terceiro segmento: '))
if a<b+c and b<c+a and c<b+a:
    if a==b and b==c:
        print('Estes 3 segmentos formam um triângulo e, esse é um triângulo Equilátero.')
    elif a==b and b!=a or a==c and a!=b:
        print('Estes 3 segmentos formam um triângulo e, esse é um triângulo Isósceles.')
    else:
        print('Estes 3 segmentos formam um triângulo e, esse é um triângulo Escaleno.')
else:
    print('Estes segmentos não formam um triângulo.')
