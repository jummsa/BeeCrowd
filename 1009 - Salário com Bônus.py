NOME = (input())
SALARIO = float(input())
VENDAS = float(input())
COMISSAO = 0.15
TOTAL = ((VENDAS * COMISSAO) + SALARIO)
print(f'TOTAL = R$ {TOTAL:.2f}')
