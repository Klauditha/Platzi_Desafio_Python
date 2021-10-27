def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuantos pesos "+ tipo_pesos +" tienes?: ")
    pesos = float(pesos)
    #valor_dolar = 3875
    dolares = pesos/valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")

menu = """
Bienvenido al conversor de monedas 👀

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """

opcion = input(menu)

if opcion == "1":
    conversor("colombianos",3875)
elif opcion == "2":
    conversor("argentinos",65)
elif opcion == "3":
    conversor("mexicanos",241)
else:
    print("Ingresa una opcion valida")
    
    

