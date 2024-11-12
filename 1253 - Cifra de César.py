N = int(input())
c = 0

while c < N:
    cod = input()    
    deslocamento = int(input())    
   
    decodificado = ""    
   
    i = 0
    while i < len(cod):
        letra = cod[i]        
        nova_posicao = (ord(letra) - deslocamento)
       
        if nova_posicao < ord('A'):
            nova_posicao = nova_posicao + 26        
        decodificado = decodificado + chr(nova_posicao)
        i = i + 1    
   
    print(decodificado)    
   
    c = c + 1
