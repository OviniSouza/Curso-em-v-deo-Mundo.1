frase = '   Beatriz é linda   '
#mostra do 2 ao 12 caracter
print(frase[3:13])
#conta quantas letras 'a' tem na frase
print(frase.count('a'))
#conta quantas letras 'B' maiúsculas tem na frase
print(frase.upper().count('B'))
#conta quantas letras tem na frase
print(len(frase))
#conta quantas letras tem desconsiderando espaços indesejados
print(len(frase.strip()))
#trocar palavras ou letras dentro da frase
print(frase.replace('linda', 'Perfeita'))
#mostrar se a palavra existe na frase
print('Beatriz' in frase)
#encontrar palavra dentro da frase
print(frase.find('Beatriz'))
#encontrar palavra em minúsculo dentro da frase
print(frase.lower().find('linda'))
#dividir frase
print(frase.split())
#mostrar a parte que quiser da frase dividida
dividido = frase.split()
print(dividido[0][0])
        #Frase 1, letra 1


#printar tds as linhas sem ter q escrever print varias vezes
#print('''Não sei o q lá
#Não sei o q lá
#Não sei o q lá
#Não sei o q lá
#Não sei o q lá
#Não sei o q lá
#Não sei o q lá
#Não sei o q lá
#Não sei o q lá
#Não sei o q lá
#Não sei o q lá'''