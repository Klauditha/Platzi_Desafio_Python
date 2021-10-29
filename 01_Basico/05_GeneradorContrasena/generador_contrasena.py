import random

def generar_contrasena():
    mayusculas = ['A','B','C','D','E','G','H']
    minusculas = ['a','b','c','d','e','f','g']
    simbolos = ['!','$','#','/','(',')']
    numeros = ['1','2','3','4']
    caracteres = mayusculas + minusculas + simbolos + numeros
    contrasena = []

    for i in range(15):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)
    contrasena = ''.join(contrasena)
    return contrasena

y
def run():
    contrasena = generar_contrasena()
    print("Tu nueva contraseña es : "+ contrasena)


if __name__ == '__main__':
    run()