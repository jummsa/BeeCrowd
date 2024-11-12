# Função para calcular o número de variações possíveis para cada senha
def calcular_variacoes(senha):
    substituicoes = {'a': 3, 'e': 3, 'i': 3, 'o': 3, 's': 3}  # 3 opções: minúscula, maiúscula e número
    total_variacoes = 1
    
    for char in senha.lower():  # Processamos a senha em letras minúsculas
        if char in substituicoes:
            total_variacoes *= substituicoes[char]  # Letras especiais têm 3 variações
        else:
            total_variacoes *= 2  # Outras letras têm 2 variações (maiúscula e minúscula)
    
    return total_variacoes

# Entrada do número de casos de teste
T = int(input("Digite o número de casos de teste: "))

# Processa cada caso de teste
for _ in range(T):
    senha = input("Digite a senha: ").strip()
    variacoes = calcular_variacoes(senha)
    print(variacoes)
