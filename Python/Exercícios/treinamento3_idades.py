num = 1
cont = 0
soma = 0
while num >=0:
    num = int(input())
    if num >= 0:
        cont = cont + 1
        soma = soma + num
media = soma / cont
print('{:.2f}'.format(media))
