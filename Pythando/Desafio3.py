#Numeros impares
a = 1
for i in range(5):
    print(a, end = ' ')
    a += 2

print()

# O dobro do elemento anterior
b = 2
for i in range(7):
    print(b, end = ' ')
    b *= 2

print()

# Quadrado do índice
c = 0
for i in range(8):
    print(c ** 2, end = ' ')
    c += 1

print()

# Quadrado de números pares
d = 2 
for i in range (5):
    print(d**2, end = ' ')
    d += 2

print()

#Sequencia de Fibonnaci
a, b = 0, 1
for i in range(7):
    print(f'{b}', end = ' ')
    a, b = b, a + b
    
print()

#Numeros inteiros que começam com 'D'
print('2 10 12 16 17 18 19 200')
