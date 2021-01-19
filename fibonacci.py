def fib(n):
# Funcion fibonacci
    if n == 1 or n == 0:
        return n
    else:
        return fib(n-1) + fib(n-2)

numero = int(input("Ingresa un numero: "))

if numero < 0:
    print("Numero invalido")
    i= 0

print("Sucesion de fibonacci")

for i in range(0, numero + 1):
    print("Numero", i,"Final", fib(i))

# Funcion foro
# a, b = 0, 1
#     # if n < 2:
#     #     return n
#     # return fib(n-1) + fib(n-2)
# for x in range(36):
#     print("iteracion", x ,"resultado", b)
#     a, b = b, a+b

