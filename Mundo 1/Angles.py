from math import radians, sin, cos, tan
an = float(input('Input your angle: '))
angle = radians(an)
sen = sin(angle)
cos = cos(angle)
tan = tan(angle)
print (f'The angle {an} presents:\nSen: {sen:.3f}\nCos: {cos:.3f}\nTan: {tan:.3f}')
