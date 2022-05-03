import math
ang = float(input('Entre com o ângulo: '))
rad = math.radians(ang)
seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)
print('O ângulo {:.2f} tem seno de {:.2f}, cosseno de {:.2f} e tangente de {:.2f}'.format(ang, seno, cosseno, tangente))
