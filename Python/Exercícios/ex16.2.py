import math
num = float(input('Entre com um numero real: '))
num2 = math.trunc(num) #deste modo a variável é concatenada aravés da biblioteca de matecmatica do python
print('O numero digitado foi {}, sua porção inteira é {:.0f}'.format(num, num2))
