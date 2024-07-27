print("Vamos a realizar una comparacion de numeros, donde el segundo debera ser mayor que el anterior")
num1 = int(input("Dame tu primer numero : "))
num2 = int(input("Dame tu segundo numero : "))

while (num1 >= num2 ):
    print(f"{num2} no es mayor que {num1}")
    num2 = int(input("Por favor ingrese otro numero "))
else:
    print(f"Tus numeros son {num1} y {num2}")
