def primo(num):
    if num <= 1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def GP(limit_up):
    primos = []
    for num in range(2,limit_up + 1):
        if primo(num):
            primos.append(num)
    return primos


def main():
    print("Generador de números primos")
    while True:
        try:
            limit_up = int(input("Ingresa el limite superior: "))
            if limit_up <= 1:
                print("Ingresa numero mayor a 1.")
                continue
            primos = GP(limit_up)
            print("Los números primos hasta el límite superior son:", primos)
        except ValueError:
            print("Por favor ingresa un numero entero.")
        continuar = input("¿Deseas generar de nuevo numeros primos hasta el limite superior? (s/n): ")
        if continuar != "s":
            break


if __name__ == "__main__":
    main()