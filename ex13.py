n = float(input('Quanto é o seu salário? R$'))
d = 0.15 * n
s = n + d
print('Ao receber um aumento de 15%, o seu salário passa a ser R${:.2f}'.format(s))