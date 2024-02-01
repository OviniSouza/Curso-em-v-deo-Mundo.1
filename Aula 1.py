# condições aninhadas
nome = str(input('Qual é o seu nome? '))
if nome == 'Beatriz':
    print('Que nome bonito!')
elif nome == 'Beah' or nome == 'Bea':
    print('Que nome bonito!')

elif nome in 'Pamella Patricia Patricia':
    print('Esse nome me parece familiar:')
else:
    print('Nome bonito, mas nem tanto')
print('Tenha um bom dia {}!'.format(nome))