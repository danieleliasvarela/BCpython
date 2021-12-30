N = int(input())
i = 0
j = 0
soma_de_impares = 0

for i in range(N):                  
    linha = input().split()         
    X, Y = linha
    X = int(X)                      
    Y = int(Y)                      
    
    if Y > X: 
        for j in range(int(X)+1, int(Y)):
            if j % 2 != 0:
                soma_de_impares += j
        print(soma_de_impares)
        soma_de_impares = 0

    if X > Y: 
        for j in range(int(Y)+1, int(X)):
            if j % 2 != 0:
                soma_de_impares += j
        print(soma_de_impares)
        soma_de_impares = 0

    if X == Y:
        soma_de_impares = 0
        print(soma_de_impares)
