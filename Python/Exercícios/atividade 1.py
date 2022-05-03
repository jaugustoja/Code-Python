valorp= float(input('preço da mercadoria: '))
qtd= float(input('quantidade: '))
total1= valorp * qtd
vdesconto1= total1 * 0.9
vdescontot= (qtd * 0.01) * total1
total2= vdesconto1 - vdescontot

if qtd <= 40:
    print(f'Total da compra: R$ {total1:.2f}')
    print(f'Total da compra com descontos: R$ {total2:.2f}')
    
else:
    print('Compra negada. Mais de 40 itens')
