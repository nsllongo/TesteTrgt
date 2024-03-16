def inversao(p):
    str_invert = ''
    for letra in p:
        str_invert = letra + str_invert
    return str_invert

string = input('Insira uma palavra:')
print(f'String invertida {inversao(string)}')