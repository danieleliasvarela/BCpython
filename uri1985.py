q = int(input())  # quantidade de pedidos
i = 1
VT = 0
for i in range(i, q+1):
    linha = input().split(" ")
    x, y = linha
    x = int(x)
    y = int(y)
    if x == 1001:
        x = 1.50
    elif x == 1002:
        x = 2.50
    elif x == 1003:
        x = 3.50
    elif x == 1004:
        x = 4.50
    else:
        x = 5.50
    VT += x*y  # VT = VT + x + y

print(f'{VT:.2f}')
