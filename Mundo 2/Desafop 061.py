print('Progressão aritmética')
r = float(input('Razão: '))
a1 = float(input('Primeiro termo: '))
p = 0
termo = 0
while termo != 10 + p:
    an = a1 + (termo - 1) * r
    print(an)
    termo += 1
    if termo == 10 + p:
        p = int(input('Quantos termos a mais? '))
print('Fim')
