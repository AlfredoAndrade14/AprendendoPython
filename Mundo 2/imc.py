#índice de massa corporal

altura = float(input('informe a sua altura: ')) 
peso = float(input('informe seu peso: ')) 
imc = peso / (altura**2) 

if imc < 18.5:
  print ('você está abaixo do peso ideal, seu IMC é {:.2f}'.format(imc)) 

elif 18.5 <= imc <= 25:
  print ('você está no peso ideal, seu IMC é {:.2f}'.format(imc))

elif 25 <= imc <= 30:
  print ('seu IMC {:.2f}, indica sobrepeso'.format(imc)) 

elif 30 <= imc <= 40:
  print ('seu IMC {:.2f}, indica obesidade'.format(imc)) 

elif imc > 40:
  print ('seu IMC {:.2f} indica obesidade mórbida'.format(imc)) 
