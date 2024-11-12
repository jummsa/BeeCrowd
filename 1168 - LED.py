N = int(input())
leds_digito = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

i = 0


while i < N:    
    num = input()    
    leds_t = 0
    
    for digito in num:        
        leds_t = leds_t + leds_digito[int(digito)]
    
    print(f"{leds_t} leds")      
    i = i + 1
