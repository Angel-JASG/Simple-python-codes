import random

def lanzar(num_dados,lados):
    resultados = []
    for _ in range(num_dados):
        resultado = random.randint(1,lados)
        resultados.append(resultado)
    return resultados

def main():
    print("Simulador de dados")
    while True:
        try:
            num_dados = int(input("Numero de dados: "))
            lados = int(input("Cantidad de lados que tendra los dados: "))
            if num_dados < 0:
                print("Por favor ingrse numeros positivos mayores a 0.")
                continue
            resultados = lanzar(num_dados,lados)
            print("El resultado del lanzamiento es:",resultados)
        except ValueError:
            print("Por favor ingrese numeros enteros.")
        continuar = input("¿Deseas lanzar los dados de nuevo? (s/n): ").lower()
        if continuar != "s":
            break

if __name__ == "__main__":
    main()