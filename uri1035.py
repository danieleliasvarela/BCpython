linha1 = input().split(" ")
A, B, C, D = linha1  # É CRIADA UMA LISTA COM OS NUMEROS

# CONVERTO OS ELEMENTOS DA LISTA PARA FLOAT ... STR → FLOAT

A = float(A)
B = float(B)
C = float(C)
D = float(D)

if (B > C) and (D > A) and (C+D) > (A+B) and ((C and D) > 0) and (A % 2 == 0):
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
