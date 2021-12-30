linha1 = input().split(' ')
a, b, c = linha1

a = int(a)
b = int(b)
c = int(c)

if a > b and b > c:
    print(f'{c}\n{b}\n{a}\n')
elif a > c and c > b:
    print(f'{b}\n{c}\n{a}\n')
elif b > a and a > c:
    print(f'{c}\n{a}\n{b}\n')
elif b > c and c > a:
    print(f'{a}\n{c}\n{b}\n')
elif c > a and a > b:
    print(f'{b}\n{a}\n{c}\n')
else:
    print(f'{a}\n{b}\n{c}\n')
print(a)
print(b)
print(c)