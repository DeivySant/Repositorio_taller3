frase = input("Por favor ingresa tu frase : ")
longitud_texto = len(frase)
i = longitud_texto - 1

while i >= 0:
    print(frase[i])
    i = i-1