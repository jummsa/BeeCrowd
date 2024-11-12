def identificar_numero(palavra):
    # Definimos as palavras corretas para comparação
    if len(palavra) == 3:
        # Para palavras de comprimento 3, verificar "one" e "two"
        if (palavra[0] == 'o' and palavra[1] == 'n') or \
           (palavra[0] == 'o' and palavra[2] == 'e') or \
           (palavra[1] == 'n' and palavra[2] == 'e'):
            return 1  # "one" é mais parecido
        else:
            return 2  # "two" é a outra opção
    elif len(palavra) == 5:
        return 3  # Palavra de comprimento 5 só pode ser "three"

# Entrada de dados
n = int(input("Digite o número de palavras: "))
for _ in range(n):
    palavra = input("Digite a palavra: ").strip()
    print(identificar_numero(palavra))
