import time

def start():

    Version = ""

    print("Selecciona la version de calculadora que quieres ejecutar...")

    print("Versiones disponibes: 0.5")

    Version = input("Ingresa la Version: ").strip().lower()

    if Version == "0.5":
        Cal0_5()
    else:
        print("esa version no existe")
        time.sleep(3)
        start()

    pass

def Cal0_5():
    print("calculadora verison: 0.5")
    
    def procces0_5():
        print("¿Que operacion quieres hacer?")
        Signo0_5 = input("Ingresa tu signo +,-,* y /: ").strip().lower()

        print("Ingresa tu primer digito")
        l1Digito0_5 = float(input("Digito: "))
        print("Ingresa tu segundo digito")
        l2Digito0_5 = float(input("2 Digito: "))

        if Signo0_5 == "x" and "X" and "*":
            print(l1Digito0_5," ",Signo0_5," ",l2Digito0_5," = ",l1Digito0_5 * l2Digito0_5)
        elif Signo0_5 == "-":
            print(l1Digito0_5," ",Signo0_5," ",l2Digito0_5," = ",l1Digito0_5 - l2Digito0_5)
        elif Signo0_5 == "+":
            print(l1Digito0_5," ",Signo0_5," ",l2Digito0_5," = ",l1Digito0_5 + l2Digito0_5)
        elif Signo0_5 == "/":
            print(l1Digito0_5," ",Signo0_5," ",l2Digito0_5," = ",l1Digito0_5 / l2Digito0_5)
        else:
            print("operacion no reconocida")

        print("Quieres hacer otra operación?")
        option = input("Y/y para sí, cualquier otra tecla para no: ").strip().lower()

        if option == "Y" and "y":
            Cal0_5()
        else:
            exit()
        pass

    procces0_5()




start()