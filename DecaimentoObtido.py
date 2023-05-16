import math

VObtidos = [450, 367, 318, 266, 219, 177, 147, 121, 99, 86, 72, 59, 43, 32, 26, 22, 17, 14, 11, 9, 4]
DObtidos = []

for i in VObtidos:
    x = (math.log(i / VObtidos[i+1]))
    DObtidos.append(x)

print(f'O lambda é igual a: {-(sum(DObtidos) / len(DObtidos))}')
