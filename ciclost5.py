print("¡ CADA VEZ MAS GRANDES !")
num1 = int(input("Ingresa un numero : "))
num2 = int(input("Ingresa un numero mayor al anterior: "))

while (num2 > num1):
    num1 = num2
    num2 = int(input("Ingresa un numero mayor al anterior : "))

else:
    print(f"{num2} no es mayor que {num1}")