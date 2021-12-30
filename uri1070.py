X = int(input())

if (X % 2 != 0):
    print(X)
    for i in range(5):
        X = X + 2
        print(X)
if (X % 2 == 0):
    X = X + 1
    print(X)
    for i in range(5):
        X = X+2
        print(X)
