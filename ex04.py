n = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(n))
print('Só tem espaço? ', n.isspace())
print('Só tem número? ', n.isnumeric())
print('Só tem letra? ', n.isalpha())
print('Esta em maiúsculo? ', n.isupper())
print('Esta em minúsculo? ', n.islower())
print('Esta capitalizado(Letra maiúscula e minúscula) ? ', n.istitle())


