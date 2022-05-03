nome = str(input('Digite o seu nome: ')).strip()
print('Analisando o seu nome...')
print('Seu nome em Caixa alta é {}'.format(nome.upper()))
print('Seu nome em Caixa baixa é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#ACIMA O FORMAT VAI CONTAR A QUANTIDADE DE CARACTERES ATRAVES DO LEN E SUBTRAIR PELO NUMERO...
#DE ESPAÇOS VAZIOS DEFINIDOS PELO NOME.COUNT.
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
#acima o .format(nome.find(' ')) identifica o espaço vazio na variável...
#possibilitando a contagem dos caracteres do primero nome.
separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))
