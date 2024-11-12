def processar_atalhos(texto):
    resultado = ""
    italico_aberto = False
    negrito_aberto = False

    for char in texto:
        if char == "_":
            # Alterna entre abrir e fechar a tag <i>
            if italico_aberto:
                resultado += "</i>"
            else:
                resultado += "<i>"
            italico_aberto = not italico_aberto
        elif char == "*":
            # Alterna entre abrir e fechar a tag <b>
            if negrito_aberto:
                resultado += "</b>"
            else:
                resultado += "<b>"
            negrito_aberto = not negrito_aberto
        else:
            # Adiciona o caractere normal ao resultado
            resultado += char

    return resultado

# Leitura das linhas de entrada
while True:
    try:
        linha = input()
        print(processar_atalhos(linha))
    except EOFError:
        break
