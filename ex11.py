l = float(input('Quanto sua parede tem, em metros, de largura? '))
h = float(input('E quanto ela tem, em metros, de altura? '))
a = l * h
t = a / 2
print('Sua parede tem {} m² e precisa de {}L de tinta para ser pintada'.format(a, t))