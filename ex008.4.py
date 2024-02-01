from math import trunc
vel = float(input('A quantos Km/h o carro passou?'))
if vel >= 81:
    real = vel - 80
    multa = real * 7
    print('Você foi multado por excesso de velocidade! O limite é de 80Km/h e você estava á {}, por isso recebeu uma multa de R${}'.format(trunc(vel), multa))