import pandas as pd

df = pd.read_json('c:\\Users\\Alex\\Documents\\Target\\questao3\\dados.json')

dias = 0
total = 0
maior = df['valor'].iloc[0]
menor = df['valor'].iloc[0]

for i in df['valor']:
    
    if i > 0:
        total += i
        dias += 1
    
    if i > maior:
        maior = i
    
    elif i < menor:
        menor = i

mediaMensal = total/dias
dias_media = 0

for j in df['valor']:
    if j > mediaMensal:
        dias_media += 1


print(dias_media, maior, menor)
print(f'Média dias: {dias_media}, Maior: {maior}, Menor: {maior} ')