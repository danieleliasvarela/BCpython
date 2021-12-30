linha1 = input().split(" ")
N1, N2, N3, N4 = linha1

media = (2* float(N1) + 3* float(N2) + 4* float(N3) + float(N4))/10

print(f'Media: {media:.1f}')

situacao = 'a'

if media >= 7.0:
    print('Aluno aprovado.')
    
elif media < 5.0:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    nota_exame = float(input())
    print(f'Nota do exame: {nota_exame:.1f}')
    nova_media = (media + nota_exame)/2
    if nova_media >= 5.0:
        print('Aluno aprovado.')
        print(f'Media final: {nova_media:.1f}')
    else: 
        print('Aluno reprovado.')
        print(f'Media final: {nova_media:.1f}')