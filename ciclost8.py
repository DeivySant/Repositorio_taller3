while True :
    print("CALCULADORA DIGITAL XD ")
    print("------Opciones------- : ")
    print("------1. SUMA-------- ")
    print("------2. RESTA------- ")
    print("--3. MULTIPLICACION-- ")
    print("-----4. DIVISION----- ")
    print("----5. PAR O IMPAR--- ")
    print("------6. SALIR-------")
    opci = int(input("Por favor selecciona una opcion : "))

    if opci == 1:
        print("------SUMA------")
        num1 = int(input("Por favor ingresa un valor : "))
        num2 = int(input("Por favor ingresa otro valor : "))
        suma = num1 + num2
        print("------------------------------------")
        print(f"[{num1}] + [{num2}] = [{suma}]")
        print("------------------------------------")
        print (f"La suma de sus numeros es : {suma}")


    elif opci == 2 :
        print("RESTA")
        num1 = int(input("Por favor ingresa un valor : "))
        num2 = int(input("Por favor ingresa otro valor : "))

        resta = num1 - num2
        print("------------------------------------")
        print(f"[{num1}] - [{num2}] = [{resta}]")
        print("------------------------------------")
        print (f"La resta de sus numeros es : {resta}")

    elif opci == 3 :
        print("MULTIPLICACION")
        num1 = int(input("Por favor ingresa un valor : "))
        num2 = int(input("Por favor ingresa otro valor : "))

        mult = num1 * num2
        print("------------------------------------")
        print(f"[{num1}] * [{num2}] = [{mult}]")
        print("------------------------------------")
        print (f"La multiplicacion de sus numeros es : {mult}")

    elif opci == 4 :
        print("DIVISION")
        num1 = int(input("Por favor ingresa un valor : "))
        num2 = int(input("Por favor ingresa otro valor : "))
        if (num1 >0) and (num2 > 0):
            div = num1/num2
            print("------------------------------------")
            print(f"[{num1}] / [{num2}] = [{div}]")
            print("------------------------------------")
            print(f"La division de sus numeros es : {div}")
        else:
            print("No existe la divison por cero [0]")
            num2 = int(input("Por favor ingresa otro valores diferentes de cero [0]"))

    elif opci == 5 :
        print("PAR O IMPAR")
        num1 = int(input("Por favor ingresa un valor : "))
        if num1%2 == 0:
            print("------------------------------------")
            print(f"El numero {num1} es par ")
            print("------------------------------------")
        else:
            print("------------------------------------")
            print(f"El numero {num1} es impar")
            print("------------------------------------")
    elif opci == 6:
        break
       
    
print("¡Que tengas buen dia!")








