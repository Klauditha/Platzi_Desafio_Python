from datetime import datetime

def execution_time(func):
    def wrapper(*args,**kwargs):
        initial_time = datetime.now()
        func(*args,**kwargs)
        final_time = datetime.now()
        time_lapsed = final_time - initial_time
        print("Pasaron "+ str(time_lapsed.total_seconds())+ " segundos")
    return wrapper

@execution_time
def random_func():
    for _ in range(1,10000000):
        pass
    
#random_func()

@execution_time
def suma (a : int, b: int) -> int:
    return a + b


@execution_time
def saludo(nombre="Cesar"):
    print("Hola "+ nombre)


suma(5,5)
random_func()
saludo("Facundo")