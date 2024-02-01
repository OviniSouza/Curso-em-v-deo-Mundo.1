v = float(input('Distância da viagem em Km: '))

if v <= 200:
    p1 = (v * 0.50)
    print('Para uma viajem de {} Km, o preço é R${:.2f}'.format(v, p1))
else:
    p2 = (v * 0.45)
    print('Para uma viajem de {}Km, o preço é R${:.2f}'.format(v, p2))

