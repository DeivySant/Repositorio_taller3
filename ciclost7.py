print("El programa recibira numeros enteros y finalizara si entra un numero impar ")
num = int(input("Ingresa un valor : "))

while (num % 2) == 0 :
    num = int(input("Ingresa otro valor : "))

else:
    print(f"El numero que permitio la salida fue : {num}")