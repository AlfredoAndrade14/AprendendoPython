#confederação nacional de natação 

from datetime import date 

age = int(input('em que ano você nasceu ? '))  
ano = date.today().year 
catg = ano - age

if catg < 9:
  print ('sua categoria é: Mirim') 

elif 9 <= catg < 14:
  print ('sua categoria é: Infantil')

elif 14 <= catg < 19:
  print ('sua categoria é: Junior')

elif 19 <= catg <= 20:
  print ('sua categoria é: Sênior') 

elif catg > 20:
  print ('sua categoria é: Master')
