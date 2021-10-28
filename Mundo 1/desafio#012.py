V = float(input('Qual o valor do produto? R$'))
C1 = (5 / 100) * V
C2 = V - C1
print(f'O produto que custava R${V}, na promoção com um desconto de de 5% vai custar R${C2:.2F}!')
