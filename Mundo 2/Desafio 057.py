homens = 0
idade = 0
mulher = 0
for p in range(1, 5):
    print('-'*5, '{}ª pessoa'.format(p), '-'*5)
    a = str(input('Nome: '.format(p)))
    b = float(input('Idade: '.format(p)))
    c = str(input('Sexo [M/F]: '.format(p)).lower())
    idade += b
    if homens < b and c == 'm':
        homens = b
        homem = a
    elif c == 'f' and b < 20:
        mulher += 1
media = idade / 4
print('A média de idade do grupo é {} anos.'.format(media))
print('O homem mais velho da lista tem {} anos e chama-se {}.'.format(homens, homem))
if mulher == 1:
    print('Ao todo, temos {} mulher com menos de 20 anos.'.format(mulher))
else:
    print('Ao todo, temos {} mulheres com menos de 20 anos.'.format(mulher))
