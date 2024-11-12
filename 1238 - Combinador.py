def combinar_strings(s1, s2):
    resultado = ""
    # Alterna entre as letras de s1 e s2
    for i in range(max(len(s1), len(s2))):
        if i < len(s1):
            resultado += s1[i]
        if i < len(s2):
            resultado += s2[i]
    return resultado

# Lê o número de casos de teste
n = int(input())

# Para cada caso, lê as duas strings, combina e imprime o resultado
for _ in range(n):
    s1, s2 = input().split()
    print(combinar_strings(s1, s2))
