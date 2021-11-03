
def divisors(num):
    try:
        if num < 0:
            raise ValueError("Debe ingresar numeros positivos")
        divisor = []
        for i in range(1,num+1):
            if num % i == 0:
                divisor.append(i)
        return divisor
    except ValueError as ve:
        print(ve)
        return 0
def run():
    num = input("Ingresa un numero: ")
    assert num.isnumeric() , "Debes ingresar un numero"
    print(divisors(int(num)))
    print("Termino mi programa")

if __name__ == '__main__':
    run()