N = float(input())
a = N/100
A = int(a)
b = (N % 100)/50
B = int(b)
c = ((N % 100) % 50)/20
C = int(c)
d = (((N % 100) % 50) % 20)/10
D = int(d)
e = ((((N % 100) % 50) % 20) % 10)/5
E = int(e)
f = (((((N % 100) % 50) % 20) % 10) % 5)/2
F = int(f)
g = (((((N % 100) % 50) % 20) % 10) % 5)/1
G = int(g)
h = (((((N % 100) % 50) % 20) % 10) % 5) % 1/0.5
H = int(h)
i = ((((((N % 100) % 50) % 20) % 10) % 5) % 1) % 0.5 / 0.25
I = int(i)
j = (((((((N % 100) % 50) % 20) % 10) % 5) % 1) % 0.5) % 0.25/0.10
J = int(j)
k = ((((((((N % 100) % 50) % 20) % 10) % 5) % 1) % 0.5) % 0.25) % 0.10 / 0.05
K = int(k)
l = (((((((((N % 100) % 50) % 20) % 10) % 5) % 1) % 0.5) % 0.25) %0.10) % 0.05 / 0.01
L = int(l)
print('NOTAS:')
print(f'{A} nota(s) de R$ 100.00')
print(f'{B} nota(s) de R$ 50.00')
print(f'{C} nota(s) de R$ 20.00')
print(f'{D} nota(s) de R$ 10.00')
print(f'{E} nota(s) de R$ 5.00')
print(f'{F} nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{G} moeda(s) de R$ 1.00')
print(f'{H} moeda(s) de R$ 0.50')
print(f'{I} moeda(s) de R$ 0.25')
print(f'{J} moeda(s) de R$ 0.10')
print(f'{K} moeda(s) de R$ 0.05')
print(f'{L} moeda(s) de R$ 0.01')
