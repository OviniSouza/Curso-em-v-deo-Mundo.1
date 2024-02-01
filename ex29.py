v = int(input('A quantos Km/h o veículo passou?: '))

excesso = (v - 80)
multa = excesso * 7.00

if v <= 80:
    print('Tudo certo, pode prosseguir!')
else:
    print('Você foi multado em R${:.2f} por passar a {} Km/h onde o limite é 80Km/h'.format(multa, v))
    