s = float(input('Qual é o seu salário: '))

if s <= 1250:
    porcentagem = s * 0.15
    aumento = s + porcentagem
    print('Você teve um aumento de R${:.2f}'.format(aumento))
else:
    porcentagem = s * 0.10
    aumento = s + porcentagem
    print('Você teve um aumento de R${:.2f}'.format(aumento))