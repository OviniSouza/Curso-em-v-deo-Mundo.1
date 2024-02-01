print(19 // 2)
print(19%2)

verde = '\033[32m'
vermelho = '\033[31m'
fimcor = '\033[m'
print('-='*20)
print('{}Analisador de Triângulos{}'.format(verde, fimcor))
print('-='*20)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima {}PODEM{} formar um triâgulo!'.format(verde, fimcor))
else:
    print('Os segmentos acima {}NÃO PODEM{} formar um triângulo'.format(vermelho, fimcor))