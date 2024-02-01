#nome = input('Qual é o seu nome? ')
#print('Prazer em te conhecer {}!'.format(nome))
#{:x} - faz ficar 20 espaços antes da '!'
#{:>x} - faz o nome ficar a 20 espaços do 'conhecer'
#{:^x} - faz ficar centralizado no espaço de resposta

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
#divisão inteira
di = n1 // n2
#potencia
e = n1 ** n2
print('A soma é {} \nO produto é {} \nA divisão é {:.3f}'.format(s, m, d))#pode colocar ", end=''" para passar para a proxima linha antes desse parênteses
#":.3f" significa que tem 3 casas decimais flutuantes
# esse "end" significa q não vai passar p outra linha
# "\n" passa pra proxima linha
print('a divisão inteira é {} \nA potência é {}'.format(di, e))