#print('\033[1;37;41mOlá Mundo!\033[m')
#\033[m no final pro background n ir até o fim da página
Nome = 'Meu Amor'
cores = {'Limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('Bom dia, boa tarde, boa noite. Você tá linda hoje, como sempre {}{}{}'.format(cores['pretoebranco'], Nome, cores['Limpa']))

a = 2
b = 5
print('Os valores a e b são respectivamente \033[1;32m{}\033[m e \033[1;32m{}\033[m!!!'.format(a, b))

nome = 'Beatriz'
print('Oi! Você ta linda hoje {}{}{}!'.format('\033[4;34m', nome, '\033[m'))