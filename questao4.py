valores = {'SP' : 67836.43,
'RJ' : 36678.66,
'MG' : 29229.88,
'ES' : 27165.48,
'Outros' : 19849.53
}
total = 0
for i in valores:
    total += valores[i]

print('Contribuição para o valor total:')
for j in valores:
    percentual = (valores[j]/total) * 100
    print(f'{j}: {percentual:.2f}%')

