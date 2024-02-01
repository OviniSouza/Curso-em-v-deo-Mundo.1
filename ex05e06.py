n = int(input('Digite um número: '))
a = n - 1
s = n + 1
d = n * 2
t = n * 3
#raiz quadrada
r = n ** (1/2)
print('O antecessor de {} é {} e o seu sucessor  é {}'.format(n, a, s))
print('O dobro de {} é {} \nO seu triplo é {} \nSua raiz quadrada é {:.3f}'.format(n, d, t, r))
# tmb pode ser ".format(n, (n*2), (n*3), (n**(1/2)))"