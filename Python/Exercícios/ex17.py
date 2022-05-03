import math
co = float(input('Medida do cateto oposto: '))
ca = float(input('Medida cateto adjacente: '))
hip = math.hypot(ca, co)
print('A hipotenusa é {:.2f}'.format(hip))
