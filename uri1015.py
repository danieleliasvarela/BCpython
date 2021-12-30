import math

linha1 = input().split(" ")  # os espaços sao quebrados
linha2 = input().split(" ")  # os espaços sao quebrados

x1, y1 = linha1  # valores para receber
x2, y2 = linha2  # valores para receber

distancia = math.sqrt((float(x2)-float(x1))**2 + (float(y2)-float(y1))**2)

print(f'{distancia:.4f}')
