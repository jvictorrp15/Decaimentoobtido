import math


VObtidos = [90, 72, 64, 46, 37, 30, 26, 21, 16, 13, 11, 10, 7, 6, 5, 5, 3, 1, 1, 1, 0]
DObtidos = []  # Lista vazia para armazenar os valores calculados de DObtidos

for i in VObtidos:
    # Cálculo do valor de x usando o logaritmo natural
    # O valor de x é dado pela divisão do elemento atual i pelo próximo elemento i+1
    if i < len(VObtidos):
        x = math.log(VObtidos[i] / VObtidos[i+1])
        DObtidos.append(x)  # Adiciona o valor de x à lista DObtidos

# Cálculo do valor médio de DObtidos
media_DObtidos = sum(DObtidos) / len(DObtidos)

# Cálculo do valor de lambda
lambda_valor = media_DObtidos

# Impressão do resultado de lambda
print(f'O lambda é igual a: {lambda_valor}')
