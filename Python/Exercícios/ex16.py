num = float(input('Entre com um numero real: '))
num2 = int(num) #ou pode ser num2 = num//1 (a variavel sera dividida por 1, dará ela mesma e o valor sera concatenado, ou sej, sem decimal.
print('O numero digitado foi {}, sua porção inteira é {:.0f}'.format(num, num2))
