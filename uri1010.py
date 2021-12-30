linha1 = input().split(" ") 
linha2 = input().split(" ")
# aqui variáveis estão no type string
codigo1, numero_de_pecas_1, valor_de_peca_1 = linha1 
codigo2, numero_de_pecas_2, valor_de_peca_2 = linha2

valor_a_pagar = (float(valor_de_peca_1) * float(numero_de_pecas_1)) + (float(valor_de_peca_2) * float(numero_de_pecas_2))

print(f'VALOR A PAGAR: R$ {valor_a_pagar:.2f}')