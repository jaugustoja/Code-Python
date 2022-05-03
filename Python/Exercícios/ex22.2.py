name = str(input('Digite o seu nome: ')).strip()#desconsidera os espaços antes e depois.
print('Seu nome em caixa alta é {}'.format(name.upper()))
print('Seu nome em caixa baixa é {}'.format(name.lower()))
print('Seu nome tem {} letras'.format(len(name) - name.find(' ')))
s = name.split()
print('Seu primeiro nome é {} e tem {} letras'.format(s[0],len(s[0])))
#len conta a quantidade de caracteres
#strip elimina os espaços antes e depois da entrada
#find encontra o especificado e nesse contexto desconta da contagem feita pelo len
#split divide a variavel em pedaços de acordo com a separação e espaços.
#s[0] e len[0] especificam a primeira palavra separada pelo split. posição 0.

