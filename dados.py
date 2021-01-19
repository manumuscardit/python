import random
# Importo la libreria para usar random
minimo = 1
maximo = 6
# Defino el minimo y maximo de los dados
juga_devuelta = "si" 
# Por default es que si asi al ejecutar empieza while

while juga_devuelta == "si" or juga_devuelta == "s":
    # While loop, donde se elige numero random entre variables de dados
    print("Tirando los dados...")
    dado1 = random.randint(minimo, maximo)
    dado2 = random.randint(minimo, maximo)

    print("Te salieron los dados:")
    print(dado1)
    print(dado2)

    print("Por lo que la suma de los dados es:")
    # Suma variables
    print(dado1 + dado2)

    juga_devuelta = input("Queres tirar los dados otra vez?")
    if juga_devuelta == "no" or juga_devuelta == "n": 
        print("Saludos!")
    