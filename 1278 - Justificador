primeiro_caso = True  

while True:
    N = int(input())
    
    if N == 0:
        break

    if not primeiro_caso:
        print()  
    
    linhas = []
    
    maior_comprimento = 0
    
    i = 0
    while i < N:        
        linha = input()
        
        inicio = 0
        fim = len(linha) - 1

        while inicio <= fim and linha[inicio] == ' ':
            inicio = inicio + 1

        while fim >= inicio and linha[fim] == ' ':
            fim = fim - 1
        
        linha_sem_espacos = ""
        j = inicio
        while j <= fim:
            linha_sem_espacos += linha[j]
            j = j + 1
                    
        nova_linha = ""
        espaco = False
        j = 0
        while j < len(linha_sem_espacos):
            if linha_sem_espacos[j] != ' ':
                nova_linha += linha_sem_espacos[j]
                espaco = False
            elif not espaco:
                nova_linha = nova_linha + ' '
                espaco = True
            j = j + 1
        
        if len(nova_linha) > maior_comprimento:
            maior_comprimento = len(nova_linha)
        
        linhas.append(nova_linha)

        i = i + 1
    
    i = 0
    while i < len(linhas):
        espacos = maior_comprimento - len(linhas[i])        
        espacos_adicionados = 0
        while espacos_adicionados < espacos:
            print(' ', end="")
            espacos_adicionados = espacos_adicionados + 1
        print(linhas[i])
        i = i + 1

    primeiro_caso = False 
