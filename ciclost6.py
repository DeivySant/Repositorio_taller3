num = int(input("Dime cuantos numeros seran sumados "))

i = 0
suma = 0
while(i<num):
    nums = int(input("Dame un valor : "))
    suma = suma + nums
    i += 1

print(f"La suma de sus numeros es : {suma}")