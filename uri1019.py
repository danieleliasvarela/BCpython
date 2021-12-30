N = int(input())
# converter a divisao de real pra inteiro trocando tipo de variável
hora1 = N/3600
hora2 = int(hora1)
# converter a divisao de real pra inteiro trocando tipo de variável
minuto1 = (N%3600) / 60
minuto2 = int(minuto1)
# converter a divisao de real pra inteiro trocando tipo de variável
segundo1 = (N%3600) % 60
segundo2 = int(segundo1)
# colocar nomes decentes nas variáveis
horas = hora2
minutos = minuto2
segundos = segundo2

print(f'{horas}:{minutos}:{segundos}')





