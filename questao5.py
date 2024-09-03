def inverterString(palavra) -> str:
    invertida = ''
    for i in range(len(palavra)-1, -1, -1):
        invertida += palavra[i]

    return invertida

palavra = input('Digite uma palavra para ser invertida: ')

print(inverterString(palavra))