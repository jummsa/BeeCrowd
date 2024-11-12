def transformar_dancante(sentenca):
    dancante = ""
    maiuscula = True  
    
    for char in sentenca:
        if char == " ":
            dancante += char
        else:
            if maiuscula:
                dancante += char.upper()
            else:
                dancante += char.lower()
            maiuscula = not maiuscula
    
    return dancante


while True:
    try:
        linha = input()
        if linha == "":
            break
        
       
        resultado = transformar_dancante(linha)
        print(resultado)
    except:
        break  
