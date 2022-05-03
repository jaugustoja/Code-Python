disp = float(input('Qual a distância percorrida com o carro? '))
dias = int (input('Qual a quantidade de dias alugado? '))
c1 = dias * 60
c2 = disp * 0.15
print('O carro rodou {:.2f}km e foi alugado por {:.0f}dias, o valor do aluguel é R${:.2f}'.format(disp, dias, (c1+c2)))
