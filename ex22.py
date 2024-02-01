nome = str(input('Digite sem nome completo: ')).strip()
                                 #.strip tira os espaços
print('Analisando seu nome...')

print('Seu nome em letras maiúsculas é {}'.format(nome.upper()))
print('Seu nome em letras minúsculas é {}'.format(nome.lower()))
div = nome.split()
print('Olá {}. Seu nome tem {} letras no total (Sem contar os espaços)'.format(div[0], len(nome) - nome.count(' ')))
                                                                             #nome.count(' ') vai desconsiderar os espaços
print('Seu primeiro nome tem {} letras'.format(len(div[0])))