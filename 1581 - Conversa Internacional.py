N = int(input())

for _ in range(N):
    
    K = int(input())
    
    idiomas = set()
    
    for _ in range(K):
        idioma = input()
        idiomas.add(idioma)  
 
    if len(idiomas) == 1:
        print(idiomas.pop())  
    else:
        print("ingles")
