nome_vendedor = (input())
salario_fixo = float(input())
ganho_vendas = float(input())

salario_total = 0.15*ganho_vendas + salario_fixo
print(f'TOTAL = R$ {salario_total:.2f}')
