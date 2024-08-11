
def start():
    print("¿a que quieres convetir?")
    con = input("Celsius(C) o Fahrenheit(F): ")
    if con == "C":
        ConC()
    else:
        ConF()
    pass

def ConC():
    print("Escribe la temperatura Fahrenheit: ")
    F = float(input())

    C = (F - 32) * 5/9  

    print("La temperatura de Fahrenheit a Celsius es de: ",C)
    pass

def ConF():
    print("Escribe la temperatura Celsius: ")
    C = float(input())

    F = (C * 9/5) + 32

    print("La temperatura de Celsius a Fahrenheit es de: ",F)
    pass

start()