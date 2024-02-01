import random
n = input('Estou pensando em um número entre 1 e 5, tente adivinhar: ')

lista = [1, 2, 3, 4, 5]
r = random.choice(lista)

if r == n:
    print('Você acertou! O número que pensei era exatamente {}!'.format(r))
else:
    print('Você errou! O número que pensei era {}!'.format(r))
