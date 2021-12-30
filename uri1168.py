N = int(input())  # ler um numero que é a quantidade de linhas
i = 0
j = 0
leds = 0

for i in range(N):
    numero = str(input())  # transformo numero em letra para poder percorrer
    for j in range(len(numero)):  # j é a posição do caractere do número
        if numero[j] == '1':
            leds += 2
        if numero[j] == '2':
            leds += 5
        if numero[j] == '3':
            leds += 5
        if numero[j] == '4':
            leds += 4
        if numero[j] == '5':
            leds += 5
        if numero[j] == '6':
            leds += 6
        if numero[j] == '7':
            leds += 3
        if numero[j] == '8':
            leds += 7
        if numero[j] == '9':
            leds += 6
        if numero[j] == '0':
            leds += 6
    print(f'{leds} leds')
    leds = 0
