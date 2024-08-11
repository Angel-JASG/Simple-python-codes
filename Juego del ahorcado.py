import random

Palabras = {
    'Maria': ["Empieza con M","Termina con A","Tiene 5 palabras","Es un nombre","En México es común"],
    'Angel': ["Empieza con A","Termina con L","Tiene 5 palabras","Es un nombre","En México es común"],
    'Conalep': ["Es un nombre de una preparatoria","Pueden encontrarse en México","Empieza con C","Termina con P","Tiene 7 palabras"],
    'Carlitos': ["Es alguien que no tiene beca","Es NEGRO!!!","Es de la conalep","Empieza con C","Termina con S","Tiene 8 palabras"],
    'Computadora': ["Es un dispositivo","Empieza con C","Termina con A","tiene 11 palabras","Se utiliza en oficinas"],
    'Python': ["Es un lenguaje de programación","Empieza con P","Termina con N","Tiene 6 palabras"],
}

def seleccion_palabra_pista(Palabras):
    palabra = random.choice(list(Palabras.keys()))
    pistas = Palabras[palabra]
    return palabra, pistas

def get_pista(pistas):
    return random.choice(pistas)

def game(palabra, pistas):
    palabra = palabra.lower()
    Palabras = list(palabra)
    L_P = ['_'] * len(palabra)
    intentos = 6
    print("Pista:", get_pista(pistas))
    while intentos > 0:
        print(" ".join(L_P))
        letra = input("Adivina la letra: ").lower()
        if len(letra) == 1 and letra.isalpha():
            if letra in palabra:
                print("Correcto!!")
                for i in range(len(palabra)):
                    if palabra[i] == letra:
                        L_P[i] = letra
                if '_' not in L_P:
                    print("Felicidades, has adivinado la palabara '{}'!".format(palabra))
                    break
            else:
                intentos -= 1
                print("incorrecto. Te quedan {} intentos.".format(intentos))
                if intentos > 0:
                    print("Nueva pista:", get_pista(pistas))
        else:
            print("Por favor, ingresa una sola letra.")
    if intentos == 0:
        print("Game over. La palabra era {}".format(palabra))

palabra, pistas = seleccion_palabra_pista(Palabras)

game(palabra, pistas)
