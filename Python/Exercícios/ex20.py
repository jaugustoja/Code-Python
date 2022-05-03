import random
a1 = str(input('Aluno A: '))
a2 = str(input('Aluno B: '))
a3 = str(input('Aluno C: '))
a4 = str(input('Aluno D: '))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem para aopresentação é {}'.format(lista))
