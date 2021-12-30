N = int(input())
a = N/100
A = int(a)
b = (N%100)/50
B = int(b)
c = ((N%100)%50)/20
C = int(c)
d = (((N%100)%50)%20)/10
D = int(d)
e = ((((N%100)%50)%20)%10)/5
E = int(e)
f = (((((N%100)%50)%20)%10)%5)/2
F = int(f)
g = (((((N%100)%50)%20)%10)%5)%2
G = int(g)
print(N)
print(f'{A} nota(s) de R$ 100,00')
print(f'{B} nota(s) de R$ 50,00')
print(f'{C} nota(s) de R$ 20,00')
print(f'{D} nota(s) de R$ 10,00')
print(f'{E} nota(s) de R$ 5,00')
print(f'{F} nota(s) de R$ 2,00')
print(f'{G} nota(s) de R$ 1,00')