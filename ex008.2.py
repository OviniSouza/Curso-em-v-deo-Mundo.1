n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2)/2
if m >= 6:
    print('Parabéns!! Você tem {} pontos de média e está APROVADO'.format(m))
else:
    print('Ta de sacanagem... Ficou com {} de média?! Putz, precisa estudar mais'.format(m))