dias = int(input('Por quantos dias o veículo foi alugado?: '))
dist = float(input('Quantos Quilômetros rodados?: '))
tempo = dias * 60,00
km = dist * 0.15
total = (dias * 60.00) + (dist * 0.15)
print('O total a pagar é R${} pelos dias e R${:.2f} pela distancia rodada. Totalizando R${}'.format(tempo, km, total))