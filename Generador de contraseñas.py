import random
import string

print("Quieres generar una contraseña?")
S = input("Si(S) o No(N): ")

if S == "S" or "s":
    print("Pida la longitud deseada para la contraseña: ")
    Lon = int(input())
    
    Caract = string.ascii_letters + string.digits + string.punctuation
    Contra = ''.join(random.choice(Caract) for _ in range(Lon))

    print('Tu contraseña generada es: ',Contra)
else:
    exit() 